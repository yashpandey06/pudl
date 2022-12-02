"""Dagster repositories for PUDL."""
from dagster import (
    define_asset_job,
    load_assets_from_modules,
    repository,
    with_resources,
)

import pudl
from pudl.etl import eia_raw_dfs, fuel_receipts_costs_aggs_eia
from pudl.glue.ferc1_eia import glue
from pudl.io_managers import pudl_sqlite_io_manager
from pudl.settings import dataset_settings
from pudl.workspace.datastore import datastore

logger = pudl.logging_helpers.get_logger(__name__)


@repository
def pudl_repository():
    """Dagster repository for all PUDL assets."""
    # TODO (bendnorman): Collect assets in a more graceful way so we
    # don't have to import every new collection of assets.
    return [
        *with_resources(
            [
                eia_raw_dfs,
                fuel_receipts_costs_aggs_eia,
                glue,
                *load_assets_from_modules(
                    [pudl.transform.eia], group_name="eia_harvested_dfs"
                ),
                *load_assets_from_modules(
                    [pudl.static_assets], group_name="static_assets"
                ),
                *load_assets_from_modules(
                    [pudl.output.output_assets], group_name="output_assets"
                ),
            ],
            resource_defs={
                "datastore": datastore,
                "pudl_sqlite_io_manager": pudl_sqlite_io_manager,
                "dataset_settings": dataset_settings,
            },
        ),
        define_asset_job(name="pudl"),
    ]
