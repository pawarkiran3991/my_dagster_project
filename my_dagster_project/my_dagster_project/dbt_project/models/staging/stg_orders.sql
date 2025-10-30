{{ config(materialized='view') }}

with source_data as (
    select
        1 as order_id,
        1 as customer_id,
        100.00 as order_amount,
        '2023-01-20'::date as order_date,
        'completed' as status
    union all
    select
        2 as order_id,
        2 as customer_id,
        250.50 as order_amount,
        '2023-02-25'::date as order_date,
        'completed' as status
    union all
    select
        3 as order_id,
        1 as customer_id,
        75.25 as order_amount,
        '2023-03-15'::date as order_date,
        'pending' as status
)

select * from source_data