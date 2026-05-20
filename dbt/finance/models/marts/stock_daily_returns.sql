with prices as (
    select * from {{ ref('stg_stock_prices') }}
),

returns as (
    select
        ticker,
        date,
        close,
        lag(close) over (
            partition by ticker
            order by date
        ) as prev_close,

        round(
            (close - lag(close) over (
                partition by ticker
                order by date
            )) / lag(close) over (
                partition by ticker
                order by date
            ) * 100,
        2) as daily_return_pct

    from prices
)

select
    ticker,
    date,
    close,
    prev_close,
    daily_return_pct
from returns
where prev_close is not null  -- exclude first row per ticker, no previous day to compare