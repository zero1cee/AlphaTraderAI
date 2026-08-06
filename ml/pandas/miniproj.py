from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "raw" / "gold.csv"

df = pd.read_csv(csv_path)

df["Range"] = df["High"] - df["Low"]
df["Change"] = df["Close"] - df["Open"]

print("=" * 40)
print("Gold Market Report")
print("=" * 40)

print("Highest Close :", df["Close"].max())
print("Lowest Close :", df["Close"].min())
print("Average Close :", round(df["Close"].mean(), 2))
print("Average Range :", round(df["Range"].mean(), 2))
print("Total Volume :", df["Volume"].sum())

print(df.columns)