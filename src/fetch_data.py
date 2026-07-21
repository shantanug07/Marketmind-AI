import yfinance as yf
import pandas as pd

ticker = input("Enter stock ticker (e.g., AAPL, TSLA, RELIANCE.NS): ").upper()

print(f"\nDownloading data for {ticker}...")

df = yf.download(ticker, period="1y")

if df.empty:
    print("Invalid ticker!")
    exit()

filename = f"data/{ticker}_stock_data.csv"
df.to_csv(filename)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print(f"\nData saved to {filename}")