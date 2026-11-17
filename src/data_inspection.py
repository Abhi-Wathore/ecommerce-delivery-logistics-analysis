import pandas as pd
from pathlib import Path

data_folder = Path("data/raw")

files = [
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_sellers_dataset.csv",
]

for file in files:
    print("\n" + "=" * 50)
    print("DATASET:", file)
    print("=" * 50)

    df = pd.read_csv(data_folder / file)

    print("\nRows and columns:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nTotal missing values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 records:")
    print(df.head())