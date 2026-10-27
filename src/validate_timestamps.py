import pandas as pd

file_path = "data/interim/olist_orders_dataset.csv"
df = pd.read_csv(file_path)

timestamp_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

print("TIMESTAMP VALIDATION RESULTS")
print("-" * 50)

for column in timestamp_columns:
    original = df[column]
    converted = pd.to_datetime(original, errors="coerce")

    missing_before = original.isna().sum()
    missing_after = converted.isna().sum()
    invalid = missing_after - missing_before

    print(f"\nColumn: {column}")
    print(f"Missing before conversion: {missing_before}")
    print(f"Missing after conversion: {missing_after}")
    print(f"Invalid timestamps: {invalid}")

print("\nTimestamp validation completed!")