{{ config(materialized='table') }}

with customers as (
    select * from {{ ref('stg_customers') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

customer_orders as (
    select
        c.customer_id,
        c.customer_name,
        c.email,
        c.created_date,
        count(o.order_id) as total_orders,
        coalesce(sum(o.order_amount), 0) as total_spent,
        max(o.order_date) as last_order_date
    from customers c
    left join orders o on c.customer_id = o.customer_id
    group by c.customer_id, c.customer_name, c.email, c.created_date
)

select * from customer_orders