import pandas as pd

raw_data_file_path = "../data/raw_sales.csv"

processed_sales_data_file_path = "../data/processed_sales.csv"

raw_data_df = pd.read_csv(raw_data_file_path)

processed_data_df = pd.read_csv(processed_sales_data_file_path)

print("Raw_Data Loaded Successfully")
print(raw_data_df.head())

print("Processed_Data Loaded successfully")
print(processed_data_df.head())
