# ecommerce-delivery-logistics-analysis
E-commerce Order and Delivery Performance Analysis

### Project Objective 

 The objective of this project is to analyze e-commerce order and delivery data to evaluate operational performance, identify delivery delays, understand order trends, and examine shipping costs.

The project uses customer, seller, order, and order-item datasets to develop meaningful business insights through data cleaning, SQL-based data integration, Python analysis, and an interactive Power BI dashboard.

The analysis will focus on key performance indicators (KPIs), including total orders, order-status distribution, average delivery time, on-time delivery rate, late delivery rate, monthly order trends, and freight costs.

The final goal is to support data-driven decision-making by identifying potential operational issues and recommending improvements in delivery performance, shipping efficiency, and order management.

### Project Scope

--> Validate and prepare the four supplied CSV datasets.

--> Integrate related datasets using appropriate keys.

--> Analyze order volumes, order statuses, delivery performance, and freight costs.

--> Build and validate an interactive Power BI dashboard.

--> Document the methodology, findings, testing results, assumptions, and limitations.

### Expected Business Value

The analysis is intended to help stakeholders monitor delivery reliability, identify trends in order demand, understand shipping expenses, and make informed decisions about logistics and operational efficiency.

### My Role: Documentation & Testing
My responsibility in this project is Documentation & Testing.

 The purpose of this role is to make the project understandable, organized, testable, and reliable. I document the workflow, explain the data-cleaning decisions, record testing results, and verify that the outputs are consistent with the project's objectives.

### Responsibilities

1 Maintain the project README and documentation.

2 Document the datasets, columns, and data-cleaning requirements.

3 Record missing-value and duplicate checks.

4 Document SQL relationship-validation results.

5 Verify important Python analysis outputs against the available results.

6 Maintain a testing checklist and record identified issues.

7 Document anomalies that require further investigation.

8 Ensure that conclusions are supported by actual analysis results.

9 Record limitations and recommend further testing.

10 Keep documentation consistent with the code and project deliverables.

### Dataset Description table

| Dataset | Actual Rows | Columns | Purpose |
|---|---:|---:|---|
| `olist_orders_dataset.csv` | 99,441 | 8 | Order details, status, purchase and delivery dates |
| `olist_customers_dataset.csv` | 99,441 | 5 | Customer identifiers, locations, and states |
| `olist_order_items_dataset.csv` | 112,650 | 7 | Items per order, sellers, item prices, and freight |
| `olist_sellers_dataset.csv` | 3,095 | 4 | Seller identifiers and locations |

### Dataset descriptions

1 Customers Dataset
  Contains customer identifiers and customer location information. It helps connect orders to customers and supports location-based analysis.
  
2 Orders Dataset
  Contains order identifiers, customer identifiers, order statuses, purchase timestamps, approval timestamps, delivery timestamps, and estimated delivery dates. This is the primary dataset for delivery-performance analysis.
  
3  Order Items Dataset
  Contains order-item identifiers, product identifiers, seller identifiers, shipping-limit dates, product prices, and freight charges.
  
4  Sellers Dataset
  Contains seller identifiers and seller location information. It supports seller-level and geographic logistics analysis.
  
--> The four datasets are related through identifiers such as customer_id, order_id, and seller_id.

### Dataset Relationships
Dataset: Brazilian E-Commerce Public Dataset by Olist

- **Orders → Customers:** Join using `customer_id`.
- **Orders → Order Items:** Join using `order_id`.
- **Order Items → Sellers:** Join using `seller_id`.

!!! Important data-grain distinction: an order is not the same as an order item. One order can contain multiple items, so joining the order table directly to order items can increase the number of rows. This can distort order counts or other KPIs unless you use the correct aggregation.

### Tools and Technologies

1 Python: Data inspection and analysis.

2 Pandas: Data loading, filtering, missing-value checks, and transformations.

3 NumPy: Numerical operations.

4 Matplotlib: Data visualization.

5 Seaborn: Statistical visualization.

6 SQL / SQLite: Data validation, relationship checks, and quality testing.

7 Jupyter Notebook / Google Colab: Execution and documentation of Python analysis.

8 GitHub: Version control, project documentation, and collaboration.

9 Power BI: Planned dashboard and presentation of analytical findings.

### Data Cleaning and Preparation

The purpose of data cleaning is to improve data reliability before calculating delivery metrics or creating visualizations.

Step 1: Load the datasets
The four CSV files are loaded into Pandas DataFrames:

customers
orders
order_items
sellers

The initial row and column counts are checked to confirm that the expected datasets have been loaded.

Step 2: Check missing values

Missing values are checked using:
data.isnull().sum()
| Column                           | Missing values |
|----------------------------------|---------------:|
| `order_approved_at`              |            160 |
| `order_delivered_carrier_date`   |          1,783 |
| `order_delivered_customer_date`  |          2,965 |
| **Total missing cells**          |      **4,908** |


Cleaning decision: Missing delivery dates are not automatically filled with invented values. Some orders may not have reached the corresponding delivery stage, while delivered orders with missing delivery dates require investigation.

Step 3: Check duplicate records

Duplicate rows are checked using:
data.duplicated().sum()

The initial inspection found zero duplicate rows in each of the four datasets.
SQL checks also found zero duplicate identifiers in the checked primary-key columns:

orders.order_id
customers.customer_id
sellers.seller_id

Duplicate checks help prevent repeated records from distorting counts and analytical results.

Step 4: Standardization 

The order-status column is standardized by converting its values to lowercase and removing surrounding whitespace.
This helps prevent inconsistent labels from affecting status-based grouping and analysis.

Step 5: Preserve original data

The initial inspection and validation workflow preserves the original CSV files.

No records are deleted and no missing delivery dates are artificially filled during this inspection. Any future removal or correction should be supported by a documented reason and verified against the original data.

Step 6: Prepare data for analysis

Before calculating delivery metrics, the analysis selects delivered orders and excludes records without valid purchase or customer-delivery timestamps from the delivery-duration calculation.

This ensures that the average delivery-time metric is calculated only for orders with the necessary dates.

### Key columns and relationships

1.  orders.order_id → order_items.order_id
2.  orders.customer_id → customers.customer_id
3.  order_items.seller_id → sellers.seller_id

### KPI Definitions and Raw-Data Baselines

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

### Data Validation and Testing

SQL validation is used to check record counts, table relationships, identifier uniqueness, and delivery-date consistency.
 Relationship Validation

| Test                                  | Expected Result          | Actual Result   |
|---------------------------------------|--------------------------|-----------------|
| Orders matched to customers           | All orders matched       | 99,441 matched  |
| Orders without matching customers     | 0                        | 0               |
| Order items matched to orders         | All order items matched  | 112,650 matched |
| Order items without matching orders   | 0                        | 0               |
| Order items matched to sellers        | All order items matched  | 112,650 matched |
| Order items without matching sellers  | 0                        | 0               |

These results indicate that the checked customer, order, and seller relationships are consistent.

### Identifier Uniqueness Tests

| Test                   | Result |
|------------------------|-------:|
| Duplicate order IDs    | 0      |
| Duplicate customer IDs | 0      |
| Duplicate seller IDs   | 0      |

### Date validation

The available data-quality report records the following results:

No invalid dates were detected in the inspected date columns.
No purchase dates were later than estimated delivery dates.
No actual delivery timestamps were earlier than purchase timestamp

### Excel Data Validation Formulas

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

### Python Analysis and Results
The Python notebook uses Pandas to load the datasets, inspect their quality, convert date columns, standardize order statuses, and calculate average delivery time.

Average delivery time

The notebook filters orders with the status delivered, removes records missing the required purchase or customer-delivery dates, and calculates the difference between the two timestamps.

Formula:

Delivery time = Actual customer delivery timestamp − Purchase timestamp

The time difference is converted into days.

### Recorded Results

| Metric                             | Result     |
| ---------------------------------- | ----------:|
| Delivered orders with valid dates | 96,470     |
| Average delivery time              | 12.56 days |

### Late-delivery analysis

The SQL validation results identify 7,827 delivered orders whose actual customer-delivery dates are later than their estimated delivery dates.
This metric can be used to investigate delivery delays and assess logistics performance.

### Missing delivery-date analysis

A total of 2,965 orders have missing customer-delivery dates.

### Missing Delivery Dates by Order Status

| Order Status | Missing Delivery Dates |
| ------------ | ---------------------: |
| Shipped      |                  1,107 |
| Canceled     |                    619 |
| Unavailable  |                    609 |
| Invoiced     |                    314 |
| Processing   |                    301 |
| Delivered    |                      8 |
| Created      |                      5 |
| Approved     |                      2 |
| **Total**    |              **2,965** |

### Testing Checklist
 Completed Checks

- [ ] Confirm the four datasets load successfully.
- [ ] Verify the expected row and column counts.
- [ ] Check for missing values.
- [ ] Check for duplicate rows.
- [ ] Check duplicate order, customer, and seller identifiers.
- [ ] Validate order-to-customer relationships.
- [ ] Validate order-item-to-order relationships.
- [ ] Validate order-item-to-seller relationships.
- [ ] Convert the inspected date columns to datetime.
- [ ] Standardize order-status text.
- [ ] Calculate average delivery time for records with valid dates.
- [ ] Identify late deliveries.
- [ ] Identify delivered orders with missing delivery dates.
- [ ] Preserve original CSV files during the documented inspection.

### Further Checks Recommended

- [ ] Investigate all eight delivered orders with missing customer-delivery dates.
- [ ] Verify the final cleaning rules against the original CSV files.
- [ ] Check for negative, zero, or unusually large delivery durations.
- [ ] Validate price and freight-value ranges.
- [ ] Confirm that all final Python analysis outputs match their documented results.
- [ ] Test monthly order trends and order-status distributions.
- [ ] Test state-wise delivery and freight-cost summaries.
- [ ] Validate customer-review analysis when the relevant dataset is included.
- [ ] Verify exported summary tables and charts.
- [ ] Confirm that the final dashboard uses the intended cleaned datasets.

### Issues and Anomalies Identified

Issue 1: Missing delivery dates
Some orders do not have customer-delivery timestamps.

Impact: These records cannot be used to calculate actual delivery duration without the required dates.

Action: Preserve the missing values, distinguish legitimate missing dates from potential anomalies, and investigate where necessary.

Issue 2: Delivered orders with missing delivery dates
Eight orders have the status delivered but lack customer-delivery timestamps.

Impact: Their actual delivery durations cannot be calculated from the available timestamps.

Action: Investigate the records and verify the original source before making corrections or removing records.

Issue 3: Late deliveries
The validation results identify 7,827 orders delivered after their estimated dates.

Impact: Delivery delays may affect customer satisfaction and logistics performance.

Action: Analyze delay duration, delivery locations, and other relevant factors before drawing business conclusions.

###  Project Workflow

1 Collect the original CSV datasets.

2 Load the datasets into Python and SQLite.

3 Inspect data structure, missing values, and duplicates.

4 Validate relationships and identifier uniqueness.

5 Standardize date columns and order-status text.

6 Investigate anomalies and document cleaning decisions.

7 Calculate delivery-performance metrics in Python.

8 Perform additional SQL and numerical validation.

9 Prepare summary tables and visualizations.

10 Export verified outputs for Power BI.

11 Test the final results and update project documentation.

12 Commit the final deliverables to GitHub.

### Project Deliverables

The project documentation and analysis artifacts include:

1 01_python_analysis.ipynb — Python data inspection and delivery-time analysis.

2 data_validation.sql — SQL validation queries.

3 sql_validation_results.txt — Recorded SQL validation results.

4 data_quality_report.txt — Data-quality findings and cleaning decisions.

5 README.md — Project overview, methodology, testing, results, and limitations.

### Limitations

The average delivery-time result applies only to delivered orders with valid required timestamps.
Late-delivery counts alone do not explain the reasons for delays.
The eight delivered orders with missing customer-delivery dates require investigation.

###  Conclusion

The initial inspection of the Olist datasets established a baseline for data quality and delivery-performance analysis.

The four inspected tables contain 99,441 customer records, 99,441 order records, 112,650 order-item records, and 3,095 seller records. The recorded SQL checks found no unmatched customer, order, or seller relationships and no duplicate primary identifiers in the checked tables.

The Python notebook calculated an average delivery time of 12.56 days for 96,470 delivered orders with valid purchase and customer-delivery timestamps. The SQL results identified 7,827 late deliveries and eight delivered orders with missing customer-delivery dates.

These findings provide a foundation for further logistics analysis. Additional anomaly investigation, testing, and implementation of the remaining analysis objectives are required before the project can be considered fully complete.

### Contribution:









