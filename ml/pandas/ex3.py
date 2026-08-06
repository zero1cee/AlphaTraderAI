from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "raw" / "gold.csv"

df = pd.read_csv(csv_path)

print(df.head())

# Feature Engineering
df["Change"] = df["Close"] - df["Open"]
df["Range"] = df["High"] - df["Low"]
df["Return"] = df["Change"] / df["Open"]
df["SMA_3"] = df["Close"].rolling(window=3).mean()

df["Direction"] = (df["Change"] > 0).map({
    True: "UP",
    False: "DOWN"
})

print("\nReturn (%):")
print((df["Return"] * 100).round(2))

print(f"\nAverage Range: {df['Range'].mean():.2f}")

print("\nFinal Dataset:")
print(df)

output = BASE_DIR / "data" / "processed" / "gold_features.csv"

df.to_csv(output, index=False)

print("\nFeatures saved successfully!")