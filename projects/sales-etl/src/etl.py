import pandas as pd 

#Load raw sales data - data ingestion and inspection 

df = pd.read_csv("../data/raw_sales.csv")

print("number of rows:", len(df))

print("columns:")
print(df.columns.tolist())


print("\nsample data:")
print(df.head())




#Clean column names

df.columns = (
    df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-","_" )
)

print("\ncleaned columns:")
print(df.columns.tolist())


#Parse date columns
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst = True, errors = 'coerce')
df["ship_date"] = pd.to_datetime(df["ship_date"], dayfirst = True, errors = 'coerce')

print("\ndate types:")
print(df[["order_date", "ship_date"]].dtypes)  #str to datetime

#print("\nnull dates after parsing:")
#print(df[["order_date", "ship_date"]].isna().sum())


#Do a simple business transform
#Write a processed dataset to data/processed_sales.csv
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days
print(df[["order_date", "ship_date", "shipping_days"]].head())


#write processed dataset
output_path = "../data/processed_sales.csv"
df.to_csv(output_path, index = False)
print(f"\nprocessed data written to: {output_path}")

