with prices as (
    select * from {{ ref('stg_stock_prices') }}
),

moving_averages as (
    select
        ticker,
        date,
        close,

        round(avg(close) over (
            partition by ticker
            order by date
            rows between 49 preceding and current row
        ), 2) as ma_50,

        round(avg(close) over (
            partition by ticker
            order by date
            rows between 199 preceding and current row
        ), 2) as ma_200

    from prices
)

select * from moving_averages