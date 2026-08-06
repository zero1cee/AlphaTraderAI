from pathlib import Path
import pandas as pd

# Get project root
BASE_DIR = Path(__file__).resolve().parents[2]

# CSV file path
csv_path = BASE_DIR / "data" / "raw" / "gold.csv"

# Read CSV
df = pd.read_csv(csv_path)

print("=" * 50)
print("Gold Market Dataset")
print("=" * 50)

print(df)

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe())