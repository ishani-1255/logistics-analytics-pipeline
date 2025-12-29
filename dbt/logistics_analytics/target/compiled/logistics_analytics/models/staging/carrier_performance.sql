select
    carrier,
    count(*) as total_shipments,
    round(avg(delivery_days), 2) as avg_delivery_days,
    round(100.0 * avg(is_delayed), 2) as delay_rate_pct
from "logistics"."main"."stg_shipments"
group by carrier