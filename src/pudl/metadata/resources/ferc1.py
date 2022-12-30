"""Table definitions for the FERC Form 1 data group."""
from typing import Any

from pudl.metadata.codes import CODE_METADATA

RESOURCE_METADATA: dict[str, dict[str, Any]] = {
    "balance_sheet_assets_ferc1": {
        "description": "Comparative Balance Sheet (Assets and Other Debits). Schedule 110.",
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "record_id",
                "asset_type",
                "ending_balance",
                "starting_balance",
                "ferc_account",
                "balance",
                "row_type_xbrl",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "asset_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "balance_sheet_liabilities_ferc1": {
        "description": "Comparative balance sheet (liabilities and other credits)",
        "schema": {
            "fields": [
                "record_id",
                "report_year",
                "utility_id_ferc1",
                "starting_balance",
                "ending_balance",
                "liability_type",
                "balance",
                "ferc_account",
                "row_type_xbrl",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "liability_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "depreciation_amortization_summary_ferc1": {
        "description": (
            "Depreciation and Amortization of Electric Plan (Account 403, 404, 405) "
            "Section A: Summary of depreciation and amortization changes. "
            "Schedule 336a of FERC Form 1."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "functional_classification",
                "ferc_account_label",
                "ferc_account",
                "depreciation_amortization_value",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "functional_classification",
                "ferc_account_label",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "electric_energy_sources_ferc1": {
        "description": (
            "Electric Energy Account, sources only. Schedule 401a. Amount of "
            "electricity the utility obtained from each of several sources, by year."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "energy_source_type",
                "row_type_xbrl",
                "energy_mwh",
                "record_id",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "energy_source_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "electric_energy_dispositions_ferc1": {
        "description": (
            "Electric Energy Account, dispositions only. Schedule 401a. Electricity "
            "utilities delived to end users, internal losses, etc."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "energy_disposition_type",
                "row_type_xbrl",
                "energy_mwh",
                "record_id",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "energy_disposition_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "electric_opex_ferc1": {
        "description": (
            "Operating and maintenance costs associated with producing electricty, "
            "reported in Schedule 320 of FERC Form 1."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "expense",
                "expense_type",
                "record_id",
                "ferc_account",
                "row_type_xbrl",
            ],
            "primary_key": ["utility_id_ferc1", "report_year", "expense_type"],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "electric_plant_depreciation_changes_ferc1": {
        "description": (
            "Accumulated provision for depreciation of electric utility plant "
            "(Account 108). Schedule 219 Section A: balances and changes during year."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "depreciation_type",
                "plant_classification_type",
                "utility_type",
                "utility_plant_value",
                "record_id",
                "balance",
                "ferc_account",
                "row_type_xbrl",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "depreciation_type",
                "plant_classification_type",
                "utility_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "ferc_accounts": {
        "description": "Account numbers from the FERC Uniform System of Accounts for Electric Plant, which is defined in Code of Federal Regulations (CFR) Title 18, Chapter I, Subchapter C, Part 101. (See e.g. https://www.law.cornell.edu/cfr/text/18/part-101).",
        "schema": {
            "fields": ["ferc_account_id", "ferc_account_description"],
            "primary_key": ["ferc_account_id"],
        },
        "sources": ["ferc1"],
        "etl_group": "static_ferc1",
        "field_namespace": "ferc1",
    },
    "fuel_ferc1": {
        "description": "Annual fuel cost and quanitiy for steam plants with a capacity of 25+ MW, internal combustion and gas-turbine plants of 10+ MW, and all nuclear plants. As reported on page 402 of FERC Form 1 and extracted from the f1_fuel table in FERC's FoxPro Database.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "fuel_type_code_pudl",
                "fuel_units",
                "fuel_consumed_units",
                "fuel_mmbtu_per_unit",
                "fuel_cost_per_unit_burned",
                "fuel_cost_per_unit_delivered",
                "fuel_cost_per_mmbtu",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "income_statement_ferc1": {
        "description": "Statement of Income. Schedule 114.",
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "utility_type",
                "income_type",
                "income",
                "balance",
                "ferc_account",
                "row_type_xbrl",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "utility_type",
                "income_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "plant_in_service_ferc1": {
        "description": (
            "Balances and changes to FERC Electric Plant in Service accounts, as "
            "reported on FERC Form 1, Schedule 204. Data originally from the "
            "f1_plant_in_srvce table "
            "in FERC's FoxPro database. Account numbers correspond to the FERC Uniform "
            "System of Accounts for Electric Plant, which is defined in Code of "
            "Federal Regulations (CFR) Title 18, Chapter I, Subchapter C, Part 101. "
            "(See e.g. https://www.law.cornell.edu/cfr/text/18/part-101). Each FERC "
            "respondent reports starting and ending balances for each account "
            "annually. Balances are organization wide, and are not broken down on a "
            "per-plant basis. End of year balance should equal beginning year balance "
            "plus the sum of additions, retirements, adjustments, and transfers."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "ferc_account_label",
                "ferc_account",
                "row_type_xbrl",
                "starting_balance",
                "additions",
                "retirements",
                "adjustments",
                "transfers",
                "ending_balance",
                "record_id",
            ],
            "primary_key": ["utility_id_ferc1", "report_year", "ferc_account_label"],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "plants_ferc1": {
        "description": "FERC 1 Plants and their associated manually assigned PUDL Plant IDs",
        "schema": {
            "fields": ["utility_id_ferc1", "plant_name_ferc1", "plant_id_pudl"],
            "primary_key": ["utility_id_ferc1", "plant_name_ferc1"],
            "foreign_key_rules": {
                "fields": [
                    ["utility_id_ferc1", "plant_name_ferc1"],
                ],
            },
        },
        "sources": ["ferc1"],
        "etl_group": "glue",
        "field_namespace": "ferc1",
    },
    "plants_hydro_ferc1": {
        "description": (
            "Hydroelectric generating plant statistics for large plants. Large plants "
            "have an installed nameplate capacity of more than 10 MW. As reported on "
            "FERC Form 1, Schedule 406 (pages 406-407), and extracted from the "
            "f1_hydro table in FERC's FoxPro database."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "project_num",
                "plant_type",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "net_capacity_favorable_conditions_mw",
                "net_capacity_adverse_conditions_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "capex_land",
                "capex_structures",
                "capex_facilities",
                "capex_equipment",
                "capex_roads",
                "asset_retirement_cost",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_water_for_power",
                "opex_hydraulic",
                "opex_electric",
                "opex_generation_misc",
                "opex_rents",
                "opex_engineering",
                "opex_structures",
                "opex_dams",
                "opex_plant",
                "opex_misc_plant",
                "opex_total",
                "opex_per_mwh",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "plants_pumped_storage_ferc1": {
        "description": (
            "Generating plant statistics for hydroelectric pumped storage plants with "
            "an installed nameplate capacity of 10+ MW. As reported in Scheudle 408 of "
            "FERC Form 1 and extracted from the f1_pumped_storage table in FERC's "
            "Visual FoxPro Database."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "project_num",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "plant_capability_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "energy_used_for_pumping_mwh",
                "net_load_mwh",
                "capex_land",
                "capex_structures",
                "capex_facilities",
                "capex_wheels_turbines_generators",
                "capex_equipment_electric",
                "capex_equipment_misc",
                "capex_roads",
                "asset_retirement_cost",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_water_for_power",
                "opex_pumped_storage",
                "opex_electric",
                "opex_generation_misc",
                "opex_rents",
                "opex_engineering",
                "opex_structures",
                "opex_dams",
                "opex_plant",
                "opex_misc_plant",
                "opex_production_before_pumping",
                "opex_pumping",
                "opex_total",
                "opex_per_mwh",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "plants_small_ferc1": {
        "description": (
            "Generating plant statistics for steam plants with less than 25 MW "
            "installed nameplate capacity and internal combustion plants, gas "
            "turbine-plants, conventional hydro plants, and pumped storage plants with "
            "less than 10 MW installed nameplate capacity. As reported on FERC Form 1 "
            "Schedule 410 (pages 410-411), and extracted from the FERC Visual FoxPro "
            "database table f1_gnrt_plant."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_name_ferc1",
                "plant_type",
                "license_id_ferc1",
                "construction_year",
                "capacity_mw",
                "peak_demand_mw",
                "net_generation_mwh",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_fuel",
                "opex_maintenance",
                "fuel_type",
                "fuel_cost_per_mmbtu",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "plants_steam_ferc1": {
        "description": (
            "Generating plant statistics for steam plants with a capacity of 25+ MW, "
            "internal combustion and gas-turbine plants of 10+ MW, and all nuclear "
            "plants. As reported in Schedule 402 of FERC Form 1 and extracted from the "
            "f1_gnrt_plant table in FERC's Visual FoxPro Database."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "plant_id_ferc1",
                "plant_name_ferc1",
                "plant_type",
                "construction_type",
                "construction_year",
                "installation_year",
                "capacity_mw",
                "peak_demand_mw",
                "plant_hours_connected_while_generating",
                "plant_capability_mw",
                "water_limited_capacity_mw",
                "not_water_limited_capacity_mw",
                "avg_num_employees",
                "net_generation_mwh",
                "capex_land",
                "capex_structures",
                "capex_equipment",
                "capex_total",
                "capex_per_mw",
                "opex_operations",
                "opex_fuel",
                "opex_coolants",
                "opex_steam",
                "opex_steam_other",
                "opex_transfer",
                "opex_electric",
                "opex_misc_power",
                "opex_rents",
                "opex_allowances",
                "opex_engineering",
                "opex_structures",
                "opex_boiler",
                "opex_plants",
                "opex_misc_steam",
                "opex_production_total",
                "opex_per_mwh",
                "asset_retirement_cost",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "power_purchase_types_ferc1": {
        "description": "Coding table defining different types of electricity power purchases.",
        "schema": {
            "fields": ["code", "label", "description"],
            "primary_key": ["code"],
            "foreign_key_rules": {"fields": [["purchase_type_code"]]},
        },
        "encoder": CODE_METADATA["power_purchase_types_ferc1"],
        "sources": ["ferc1"],
        "etl_group": "static_ferc1",
        "field_namespace": "ferc1",
    },
    "purchased_power_ferc1": {
        "description": (
            "Purchased Power (Account 555) including power exchanges (transactions "
            "involving a balancing of debits and credits for energy, capacity, etc.) "
            "and any settlements for imbalanced exchanges. Reported on pages 326-327 "
            "of FERC Form 1. Extracted from the f1_purchased_pwr table in FERC's "
            "Visual FoxPro database."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "seller_name",
                "purchase_type_code",
                "tariff",
                "billing_demand_mw",
                "non_coincident_peak_demand_mw",
                "coincident_peak_demand_mw",
                "purchased_mwh",
                "received_mwh",
                "delivered_mwh",
                "demand_charges",
                "energy_charges",
                "other_charges",
                "total_settlement",
            ]
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "transmission_statistics_ferc1": {
        "description": (
            "Transmission Line Statistics. Schedule 422 of FERC Form 1. Information "
            "describing transmission lines, the cost of lines, annual operating and "
            "capital expenses, etc."
        ),
        "schema": {
            "fields": [
                "record_id",
                "utility_id_ferc1",
                "report_year",
                "start_point",
                "end_point",
                "operating_voltage_kv",
                "designed_voltage_kv",
                "supporting_structure_type",
                "transmission_line_length_miles",
                "transmission_line_and_structures_length_miles",
                "num_transmission_circuits",
                "conductor_size_and_material",
                "capex_land",
                "capex_other",
                "capex_total",
                "opex_operations",
                "opex_maintenance",
                "opex_rents",
                "opex_total",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "utilities_ferc1": {
        "description": "This table maps two manually assigned utility IDs: a PUDL ID and a FERC1 ID. The PUDL ID maps EIA and FERC1 utilities. The FERC1 ID maps the older DBF respondent IDs to new XBRL entity IDs. This table is generated from a table stored in the PUDL repository: src/package_data/glue/utility_id_pudl.csv",
        "schema": {
            "fields": ["utility_id_ferc1", "utility_name_ferc1", "utility_id_pudl"],
            "primary_key": ["utility_id_ferc1"],
            "foreign_key_rules": {"fields": [["utility_id_ferc1"]]},
        },
        "sources": ["ferc1"],
        "etl_group": "glue",
        "field_namespace": "ferc1",
    },
    "utilities_ferc1_dbf": {
        "description": "This table maps the assign utility ID FERC1 to the native utility ID from the FERC1 DBF inputs - originally reported as respondent_id.",
        "schema": {
            "fields": ["utility_id_ferc1", "utility_id_ferc1_dbf"],
            "primary_key": ["utility_id_ferc1_dbf"],
        },
        "sources": ["ferc1"],
        "etl_group": "glue",
        "field_namespace": "ferc1",
    },
    "utilities_ferc1_xbrl": {
        "description": "This table maps the assign utility ID FERC1 to the native utility ID from the FERC1 XBRL inputs - originally reported as entity_id.",
        "schema": {
            "fields": ["utility_id_ferc1", "utility_id_ferc1_xbrl"],
            "primary_key": ["utility_id_ferc1_xbrl"],
        },
        "sources": ["ferc1"],
        "etl_group": "glue",
        "field_namespace": "ferc1",
    },
    "utility_plant_summary_ferc1": {
        "description": (
            "Summary of utility plant and accumulated provisions for depreciation, "
            "amortization and depletion of utilty plant assets reported annually at "
            "the end of the report year. Schedule 200 of FERC Form 1."
        ),
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "utility_type",
                "utility_type_other",
                "utility_plant_asset_type",
                "row_type_xbrl",
                "utility_plant_value",
                "record_id",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "utility_type",
                "utility_plant_asset_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "retained_earnings_ferc1": {
        "description": "Retained Earnings - The structed part of schedule 118.",
        "schema": {
            "fields": [
                "utility_id_ferc1",
                "report_year",
                "record_id",
                "earnings_type",
                "amount",
                "starting_balance",
                "ending_balance",
                "balance",
                "ferc_account",
                "row_type_xbrl",
            ],
            "primary_key": [
                "utility_id_ferc1",
                "report_year",
                "earnings_type",
            ],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1",
        "field_namespace": "ferc1",
    },
    "retained_earnings_appropriations_ferc1": {
        "description": "Retained Earnings - some of the unstructed part of schedule 118.",
        "schema": {
            "fields": ["utility_id_ferc1", "report_year", "utility_type", "record_id"],
        },
        "sources": ["ferc1"],
        "etl_group": "ferc1_disabled",
        "field_namespace": "ferc1",
    },
}
"""FERC Form 1 resource attributes by PUDL identifier (``resource.name``).

Keys are in alphabetical order.

See :func:`pudl.metadata.helpers.build_foreign_keys` for the expected format of
``foreign_key_rules``.
"""
