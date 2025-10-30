from pathlib import Path

from dagster import Definitions, ScheduleDefinition
from dagster_dbt import DbtCliResource
from dagster_snowflake import SnowflakeResource

from assets import (
    my_dbt_assets,
    customer_analytics_report,
    snowflake_connection_test,
    analytics_job,
    dbt_project,
    snowflake_resource,
)

# Create dbt CLI resource
dbt_resource = DbtCliResource(
    project_dir=dbt_project,
    dbt_executable=Path("C:/Users/kirpawar/DAGSTER_PLUS/.venv/Scripts/dbt.exe")
)

# Define schedule for the analytics pipeline
analytics_schedule = ScheduleDefinition(
    job=analytics_job,
    cron_schedule="0 8 * * *"  # Run daily at 8 AM
)

defs = Definitions(
    assets=[
        my_dbt_assets,
        customer_analytics_report,
        snowflake_connection_test,
    ],
    jobs=[analytics_job],
    schedules=[analytics_schedule],
    resources={
        "dbt": dbt_resource,
        "snowflake": snowflake_resource,
    },
)
