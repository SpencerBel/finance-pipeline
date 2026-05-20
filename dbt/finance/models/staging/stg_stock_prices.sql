with source as (
    select * from {{ source('raw', 'stock_prices') }}
),

staged as (
    select
        ticker,
        date::date                    as date,
        round(open::numeric, 2)       as open,
        round(high::numeric, 2)       as high,
        round(low::numeric, 2)        as low,
        round(close::numeric, 2)      as close,
        volume::bigint                as volume
    from source
    where close is not null  -- exclude any rows with missing close price
)

select * from staged