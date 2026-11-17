import pandas as pd
import sqlite3
from pathlib import Path

# Project paths
DATA_DIR = Path("data/interim")
DB_PATH = Path("data/ecommerce_analysis.db")

# Create the database directory if needed
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Connect to SQLite database
connection = sqlite3.connect(DB_PATH)

# CSV files and corresponding SQL table names
datasets = {
    "olist_customers_dataset.csv": "customers",
    "olist_order_items_dataset.csv": "order_items",
    "olist_orders_dataset.csv": "orders",
    "olist_sellers_dataset.csv": "sellers",
}

try:
    for filename, table_name in datasets.items():
        print(f"Loading {filename}...")

        # Read the cleaned CSV file
        df = pd.read_csv(DATA_DIR / filename)

        # Load data into SQLite
        df.to_sql(table_name, connection, if_exists="replace", index=False)

        print(f"Table '{table_name}' created: {len(df)} rows")

    print("\nAll four datasets loaded successfully!")
    print(f"Database location: {DB_PATH}")

finally:
    connection.close()