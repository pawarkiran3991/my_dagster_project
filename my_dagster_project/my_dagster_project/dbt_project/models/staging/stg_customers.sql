{{ config(materialized='view') }}

with source_data as (
    select
        1 as customer_id,
        'John Doe' as customer_name,
        'john@example.com' as email,
        '2023-01-15'::date as created_date
    union all
    select
        2 as customer_id,
        'Jane Smith' as customer_name,
        'jane@example.com' as email,
        '2023-02-20'::date as created_date
    union all
    select
        3 as customer_id,
        'Bob Johnson' as customer_name,
        'bob@example.com' as email,
        '2023-03-10'::date as created_date
)

select * from source_data