import pandas as pd
from pathlib import Path

# Define project folders
RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/interim")

# Create the output folder if it doesn't exist
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

# List of datasets
files = [
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_sellers_dataset.csv",
]

# Process each dataset
for filename in files:
    print(f"\nProcessing: {filename}")

    # Read the original dataset
    df = pd.read_csv(RAW_DIR / filename)

    # Remove exact duplicate rows, if any
    original_rows = len(df)
    df = df.drop_duplicates()
    removed_rows = original_rows - len(df)

    # Convert date and timestamp columns to datetime
    date_columns = [
        "shipping_limit_date",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column], errors="coerce"
            )

    # Save the cleaned dataset to the interim folder
    output_path = CLEAN_DIR / filename
    df.to_csv(
        output_path,
        index=False,
        date_format="%Y-%m-%d %H:%M:%S",
    )

    print(f"Original rows: {original_rows}")
    print(f"Duplicate rows removed: {removed_rows}")
    print(f"Final rows: {len(df)}")
    print(f"Missing values remaining: {df.isna().sum().sum()}")
    print(f"Saved to: {output_path}")

print("\nData-cleaning process completed!")