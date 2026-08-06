from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "raw" / "gold.csv"

df = pd.read_csv(csv_path)

# print(df)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.duplicated())
# print(df.duplicated().sum())


# high_close = df[df["Close"] > 3370]

# print(high_close)


# sorted_df = df.sort_values(by="Close", ascending=False)

# print(sorted_df)


df["Range"] = df["High"] - df["Low"]
print(df)
df["Change"] = df["Close"] - df["Open"]
print(df)

output_path = BASE_DIR / "data" / "processed" / "gold_clean.csv"

df.to_csv(output_path, index=False)

print("Saved successfully!")