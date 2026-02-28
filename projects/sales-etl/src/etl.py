import pandas as pd

# 1) LOAD
input_path = "../data/raw_sales.csv"
df = pd.read_csv(input_path)

print("Loaded rows:", len(df))
print("Columns:", df.columns.tolist())

# Standardize column names early
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("-", "_")
)

# 2) CLEAN
# Remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print("Removed duplicates:", before - len(df))

# Parse dates (do before removing null dates)
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], dayfirst=True, errors="coerce")

# Remove rows that cannot support the business transform
# (because shipping_days needs both dates)
before = len(df)
df = df.dropna(subset=["order_date", "ship_date"])
print("Removed rows with missing dates:", before - len(df))

# 3) TRANSFORM
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

# Optional: remove negative shipping days if dataset has bad records
before = len(df)
df = df[df["shipping_days"] >= 0]
print("Removed negative shipping_days rows:", before - len(df))

print(df[["order_date", "ship_date", "shipping_days"]].head())

# 4) WRITE
output_path = "../data/processed_sales.csv"
df.to_csv(output_path, index=False)
print(f"Processed data written to: {output_path}")