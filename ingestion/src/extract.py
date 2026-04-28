import yfinance as yf
import pandas as pd

TICKERS = ["AAPL", "GOOGL", "MSFT", "TSLA", "SPY"]

def extract_prices(period="1y"):
    frames = []
    
    for ticker in TICKERS:
        print(f"Extracting {ticker}...")
        df = yf.download(ticker, period=period, auto_adjust=True, progress=False)
        df = df.reset_index()
        # Flatten MultiIndex columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0].lower() for col in df.columns]
        else:
            df.columns = [c.lower() for c in df.columns]
        df["ticker"] = ticker
        frames.append(df)
    
    combined = pd.concat(frames, ignore_index=True)
    print(f"Extracted {len(combined)} rows across {len(TICKERS)} tickers")
    return combined