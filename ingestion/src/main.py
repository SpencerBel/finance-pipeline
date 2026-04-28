from extract import extract_prices
from load import load_prices

if __name__ == "__main__":
    print("Starting ingestion...")
    df = extract_prices(period="1y")
    load_prices(df)
    print("Ingestion complete.")