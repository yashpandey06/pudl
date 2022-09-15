"""Extract, clean, and normalize the EPACAMD-EIA crosswalk.

This module defines functions that read the raw EPACAMD-EIA crosswalk file and cleans
up the column names.

The crosswalk file was a joint effort on behalf on EPA and EIA and is published on the
EPA's github account at www.github.com/USEPA/camd-eia-crosswalk".
"""
import logging

import pandas as pd

from pudl.helpers import remove_leading_zeros_from_numeric_strings, simplify_columns
from pudl.metadata.fields import apply_pudl_dtypes
from pudl.workspace.datastore import Datastore

logger = logging.getLogger(__name__)


def extract(ds: Datastore) -> pd.DataFrame:
    """Extract the EPACAMD-EIA Crosswalk from the Datastore."""
    logger.info("Extracting the EPACAMD-EIA crosswalk from Zenodo")
    with ds.get_zipfile_resource("epacamd_eia", name="epacamd_eia.zip").open(
        "camd-eia-crosswalk-master/epa_eia_crosswalk.csv"
    ) as f:
        return pd.read_csv(f)


def transform(
    epacamd_eia: pd.DataFrame,
    generators_entity_eia: pd.DataFrame,
    boilers_entity_eia: pd.DataFrame,
    processing_all_eia_years: bool,
) -> dict[str, pd.DataFrame]:
    """Clean up the EPACAMD-EIA Crosswalk file.

    The crosswalk is a static file: there is no year field. The plant_id_eia and
    generator_id fields, however, are foreign keys from an annualized table. If the
    fast ETL is run (on one year of data) the test will break because the crosswalk
    tables with plant_id_eia and generator_id contain values from various years. To
    keep the crosswalk in alignment with the available eia data, we'll restrict it
    based on the generator entity table which has plant_id_eia and generator_id so long
    as it's not using the full suite of avilable years. If it is, we don't want to
    restrict the crosswalk so we can get warnings and errors from any foreign key
    discrepancies. This isn't an ideal solution, but it works for now.

    Args:
        epacamd_eia: The result of running this module's extract() function.
        generators_entity_eia: The generators_entity_eia table.
        boilers_entity_eia: The boilers_entitiy_eia table.
        processing_all_years: A boolean indicating whether the years from the
            Eia860Settings object match the EIA860 working partitions. This indicates
            whether or not to restrict the crosswalk data so the tests don't fail on
            foreign key restraints.

    Returns:
        A dictionary containing the cleaned EPACAMD-EIA crosswalk DataFrame.
    """
    logger.info("Transforming the EPACAMD-EIA crosswalk")

    column_rename = {
        "camd_plant_id": "plant_id_epa",
        "camd_unit_id": "emissions_unit_id_epa",
        "camd_generator_id": "generator_id_epa",
        "eia_plant_id": "plant_id_eia",
        "eia_boiler_id": "boiler_id",  # Eventually change to boiler_id_eia
        "eia_generator_id": "generator_id",  # Eventually change to generator_id_eia
    }

    # Basic column rename, selection, and dtype alignment.
    crosswalk_clean = (
        epacamd_eia.pipe(simplify_columns)
        .rename(columns=column_rename)
        .filter(list(column_rename.values()))
        .pipe(remove_leading_zeros_from_numeric_strings, col_name="generator_id")
        .pipe(
            remove_leading_zeros_from_numeric_strings, col_name="emissions_unit_id_epa"
        )
        .pipe(apply_pudl_dtypes, "eia")
        .dropna(subset=["plant_id_eia"])
    )

    # Restrict crosswalk for tests if running fast etl
    if not processing_all_eia_years:
        logger.info(
            "Selected subset of avilable EIA years--restricting EPACAMD-EIA Crosswalk \
            to chosen subset of EIA years"
        )
        crosswalk_clean = pd.merge(
            crosswalk_clean,
            generators_entity_eia[["plant_id_eia", "generator_id"]],
            on=["plant_id_eia", "generator_id"],
            how="inner",
        )
        crosswalk_clean = pd.merge(
            crosswalk_clean,
            boilers_entity_eia[["plant_id_eia", "boiler_id"]],
            on=["plant_id_eia", "boiler_id"],
            how="inner",
        )

    return {"epacamd_eia": crosswalk_clean}
