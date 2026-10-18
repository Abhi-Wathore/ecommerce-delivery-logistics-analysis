# ecommerce-delivery-logistics-analysis
E-commerce Order and Delivery Performance Analysis

Project Objective

 The objective of this project is to analyze e-commerce order and delivery data to evaluate operational performance, identify delivery delays, understand order trends, and examine shipping costs.

The project uses customer, seller, order, and order-item datasets to develop meaningful business insights through data cleaning, SQL-based data integration, Python analysis, and an interactive Power BI dashboard.

The analysis will focus on key performance indicators (KPIs), including total orders, order-status distribution, average delivery time, on-time delivery rate, late delivery rate, monthly order trends, and freight costs.

The final goal is to support data-driven decision-making by identifying potential operational issues and recommending improvements in delivery performance, shipping efficiency, and order management.

Project Scope

--> Validate and prepare the four supplied CSV datasets.

--> Integrate related datasets using appropriate keys.

--> Analyze order volumes, order statuses, delivery performance, and freight costs.

--> Build and validate an interactive Power BI dashboard.

--> Document the methodology, findings, testing results, assumptions, and limitations.

Expected Business Value

The analysis is intended to help stakeholders monitor delivery reliability, identify trends in order demand, understand shipping expenses, and make informed decisions about logistics and operational efficiency.

## Dataset Description

| Dataset | Actual Rows | Columns | Purpose |
|---|---:|---:|---|
| `olist_orders_dataset.csv` | 99,441 | 8 | Order details, status, purchase and delivery dates |
| `olist_customers_dataset.csv` | 99,441 | 5 | Customer identifiers, locations, and states |
| `olist_order_items_dataset.csv` | 112,650 | 7 | Items per order, sellers, item prices, and freight |
| `olist_sellers_dataset.csv` | 3,095 | 4 | Seller identifiers and locations |

### Dataset Relationships

- **Orders → Customers:** Join using `customer_id`.
- **Orders → Order Items:** Join using `order_id`.
- **Order Items → Sellers:** Join using `seller_id`.

**These are the row counts in datasets, before any cleaning or filtering.**

!!! Important data-grain distinction: an order is not the same as an order item. One order can contain multiple items, so joining the order table directly to order items can increase the number of rows. This can distort order counts or other KPIs unless you use the correct aggregation.

Key columns and relationships

1.  orders.order_id → order_items.order_id
2.  orders.customer_id → customers.customer_id
3.  order_items.seller_id → sellers.seller_id

## KPI Definitions and Raw-Data Baselines

| KPI | Professional Definition | Raw-Data Baseline |
|---|---|---:|
| Total Orders | Count of distinct `order_id` values in the orders dataset. | 99,441 |
| Delivered Orders | Count of orders with status `delivered`. | 96,478 |
| Average Delivery Time | Average time between the purchase timestamp and actual customer delivery timestamp, measured in days. | 12.56 days |
| On-Time Delivery Rate | Eligible delivered orders delivered on or before the estimated delivery date divided by eligible delivered orders, multiplied by 100. | 91.89% |
| Late Delivery Rate | Eligible delivered orders delivered after the estimated delivery date divided by eligible delivered orders, multiplied by 100. | 8.11% |
| Total Freight Cost | Sum of `freight_value` across all order-item records. | 2,251,909.54 |
| Average Freight per Order | Total freight cost aggregated for each order, averaged across orders with item records. | 22.82 |
| Monthly Order Trend | Count of distinct orders grouped by the month of the purchase timestamp. | To be calculated |
| Order-Status Distribution | Count and percentage of distinct orders grouped by `order_status`. | To be calculated |

**Notes:**
- Delivery-time and delivery-rate calculations exclude delivered-status orders with missing actual delivery timestamps or estimated delivery dates, as applicable.
- The baseline values must be recalculated after data cleaning and validated against the SQL, Python, and Power BI outputs.

Excel data validation

update after cleaning..................................

## Excel Data Validation Formulas

| Validation | Example Formula | Purpose |
|---|---|---|
| Total Order Rows | `=COUNTA(Orders[order_id])` | Counts non-empty order IDs in the Orders table. |
| Unique Order IDs | `=ROWS(UNIQUE(Orders[order_id]))` | Counts distinct order IDs. |
| Duplicate Order IDs | `=COUNTA(Orders[order_id])-ROWS(UNIQUE(Orders[order_id]))` | Calculates the difference between non-empty order IDs and unique IDs. |
| Missing Order IDs | `=COUNTBLANK(Orders[order_id])` | Counts blank cells in the order ID column. |
| Total Freight Cost | `=SUM(OrderItems[freight_value])` | Calculates the total freight value across order-item records. |
| Delivered Order Count | `=COUNTIF(Orders[order_status],"delivered")` | Counts orders whose status is `delivered`. |

### Validation Objective

The purpose of these checks is to verify data completeness, uniqueness, and numerical accuracy before the datasets are used for SQL analysis, Python calculations, and Power BI dashboard development.



