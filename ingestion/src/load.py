import pandas as pd
from sqlalchemy import text
from config import get_engine

def create_raw_schema(engine):
    """Create raw schema if it doesn't exist"""
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))

def load_prices(df: pd.DataFrame):
    engine = get_engine()
    create_raw_schema(engine)
    
    df.to_sql(
        name="stock_prices",
        schema="raw",
        con=engine,
        if_exists="replace",
        index=False
    )
    
    print(f"Loaded {len(df)} rows into raw.stock_prices")