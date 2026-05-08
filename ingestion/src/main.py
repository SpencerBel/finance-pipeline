from extract import extract_prices
from load import load_prices

# Airflow will call this script as part of DAG
if __name__ == "__main__":
    print("Starting ingestion...")
    df = extract_prices(period="1y")
    load_prices(df)
    print("Ingestion complete.")