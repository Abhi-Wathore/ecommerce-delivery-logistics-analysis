import pandas as pd

file_path = "data/interim/olist_orders_dataset.csv"
df = pd.read_csv(file_path)

# Find delivered orders missing customer delivery timestamps
problem_orders = df[
    (df["order_status"] == "delivered")
    & (df["order_delivered_customer_date"].isna())
]

print("DELIVERED ORDERS MISSING CUSTOMER DELIVERY TIMESTAMPS")
print("-" * 60)
print("Number of affected orders:", len(problem_orders))
print("\nAffected order details:\n")

print(
    problem_orders[
        [
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ]
    ].to_string(index=False)
)

# Save the findings for the data quality report
output_path = "reports/delivered_orders_missing_timestamps.csv"
problem_orders.to_csv(output_path, index=False)

print(f"\nFindings saved to: {output_path}")