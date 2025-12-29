select
    shipment_id,
    carrier,
    origin,
    destination,

    cast(order_date as date) as order_date,
    cast(delivery_date as date) as delivery_date,
    cast(expected_delivery_date as date) as expected_delivery_date,

    distance_km,

    datediff(
        'day',
        cast(order_date as date),
        cast(delivery_date as date)
    ) as delivery_days,

    case
        when cast(delivery_date as date) > cast(expected_delivery_date as date)
            then 1
        else 0
    end as is_delayed

FROM read_parquet('/opt/airflow/data/parquet/shipments.parquet')
