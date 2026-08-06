from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "raw" / "gold.csv"

df = pd.read_csv(csv_path)


df["Change"] = df["Close"] - df["Open"]

df["Range"] = df["High"] - df["Low"]

df["Return"] = (df["Close"] - df["Open"]) / df["Open"]


print("=" * 50)
print("FEATURE ENGINEERING REPORT")
print("=" * 50)

print(f"Total Rows      : {len(df)}")
print(f"Average Open    : {df['Open'].mean():.2f}")
print(f"Average Close   : {df['Close'].mean():.2f}")
print(f"Average Change  : {df['Change'].mean():.2f}")
print(f"Average Range   : {df['Range'].mean():.2f}")
print(f"Average Return  : {df['Return'].mean() * 100:.2f}%")
print(f"Highest Close   : {df['Close'].max():.2f}")
print(f"Lowest Close    : {df['Close'].min():.2f}")

print("=" * 50)


print("\nFirst 5 Rows:\n")
print(df.head())


output_path = BASE_DIR / "data" / "processed" / "gold_features.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print(f"\nEngineered dataset saved to:\n{output_path}")