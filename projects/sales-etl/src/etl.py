import pandas as pd 

#Load raw sales data

df = pd.read_csv("../data/raw_sales.csv")

print("number of rows:", len(df))

print("columns:")
print(df.columns.tolist())


print("\nsample data:")
print(df.head())