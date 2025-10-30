
import os
import pandas as pd
from pathlib import Path

from dagster import (
    AssetExecutionContext,
    ConfigurableResource,
    Definitions,
    asset,
    define_asset_job,
)
from dagster_dbt import (
    DbtCliResource,
    DbtProject,
    build_dbt_asset_selection,
    dbt_assets,
)
from dagster_snowflake import SnowflakeResource


# Define the dbt project
dbt_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "dbt_project").resolve(),
    profiles_dir=Path(__file__).joinpath("..", "dbt_project").resolve(),
)

# Define dbt assets
@dbt_assets(
    manifest=dbt_project.manifest_path,
    project=dbt_project,
)
def my_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


# Snowflake resource configuration
snowflake_resource = SnowflakeResource(
    account="PHWYUBU-GR70594",
    user="KPAWAR9428",
    authenticator="externalbrowser",
    role="ACCOUNTADMIN",
    warehouse="COMPUTE_WH",
    database="DBT_SNF",
    schema="DBT_SNF_SC",
)


@asset(deps=[my_dbt_assets])
def customer_analytics_report(context: AssetExecutionContext, snowflake: SnowflakeResource) -> pd.DataFrame:
    """
    Generate analytics report from the customer summary table created by dbt.
    """
    query = """
    SELECT 
        customer_name,
        total_orders,
        total_spent,
        last_order_date,
        CASE 
            WHEN total_spent > 200 THEN 'High Value'
            WHEN total_spent > 100 THEN 'Medium Value'
            ELSE 'Low Value'
        END as customer_segment
    FROM customer_summary
    ORDER BY total_spent DESC
    """
    
    with snowflake.get_connection() as conn:
        df = pd.read_sql(query, conn)
        context.log.info(f"Generated analytics report with {len(df)} customers")
        return df


@asset
def snowflake_connection_test(snowflake: SnowflakeResource) -> dict:
    """
    Test Snowflake connection and return basic information.
    """
    query = "SELECT CURRENT_VERSION() as snowflake_version, CURRENT_USER() as current_user"
    
    with snowflake.get_connection() as conn:
        result = pd.read_sql(query, conn)
        return {
            "snowflake_version": result.iloc[0]["SNOWFLAKE_VERSION"],
            "current_user": result.iloc[0]["CURRENT_USER"],
            "connection_status": "successful"
        }


# Define a job that runs all assets
analytics_job = define_asset_job(
    name="analytics_pipeline",
    selection=build_dbt_asset_selection([my_dbt_assets]).downstream(),
)
