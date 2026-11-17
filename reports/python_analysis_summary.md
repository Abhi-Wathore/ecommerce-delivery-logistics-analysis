# Python Analysis Summary Report
## E-commerce Delivery & Logistics Performance Analysis

### 1. Project Overview

This project analyzes the Olist Brazilian E-Commerce dataset to evaluate order patterns, cancellation rates, delivery performance, logistics processing time, freight costs, and regional performance.

Python was used to process the datasets, calculate key performance indicators (KPIs), identify trends, and create visualizations. The resulting summary tables and charts are intended to support the team's Power BI dashboard.

**Role:** Python Analysis  
**Notebook:** `Python_analysis.ipynb`  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

### 2. Objectives

The main objectives of the analysis were to:

- Examine order status distribution and cancellation rates.
- Calculate average delivery duration.
- Measure on-time and late delivery performance.
- Analyze delivery delays and order processing time.
- Identify monthly order trends.
- Evaluate freight costs and average order value.
- Compare cancellation and delivery performance across customer states.
- Export summary tables and charts for Power BI integration.

### 3. Datasets Used

Four datasets were used for the analysis.

| Dataset | Number of Rows | Purpose |
|---|---:|---|
| Orders | 99,441 | Order status and purchase, approval, and delivery timestamps |
| Order Items | 112,650 | Product prices, freight values, and order items |
| Customers | 99,441 | Customer information and state-level analysis |
| Sellers | 3,095 | Seller information and dataset inspection |

The analysis identified 99,441 unique orders in the full orders dataset and 98,666 orders with corresponding item-price records.

### 4. Data Preparation and Quality Checks

The following preparation and validation activities were performed:

- Loaded the four CSV files into Pandas DataFrames.
- Examined dataset dimensions, column names, and data types.
- Checked for missing values and duplicate rows.
- Converted order timestamp columns into datetime format.
- Identified records eligible for each KPI calculation.
- Aggregated item prices and freight values at the order level.
- Combined order and customer information for regional analysis.
- Excluded invalid or negative time intervals from relevant processing and delivery calculations.

The orders dataset contained missing timestamps, including 160 missing approval timestamps, 1,783 missing carrier-delivery timestamps, and 2,965 missing customer-delivery timestamps. These missing values were considered when selecting records for the corresponding calculations.

### 5. Key Performance Indicators

The following results are documented in the current analysis and should be verified against the team's final validated dataset before submission.

| KPI | Result |
|---|---:|
| Total unique orders | 99,441 |
| Orders with item-price records | 98,666 |
| Canceled orders (all orders) | 625 |
| Cancellation rate (all orders) | 0.63% |
| Canceled orders (with item data) | 461 |
| Cancellation rate (with item data) | 0.47% |
| Average delivery duration | 12.50 calendar days |
| Eligible delivered orders for on-time/late analysis (orders_with_items) | 96,470 |
| On-time deliveries (orders_with_items, full timestamps) | 88,644 |
| Late deliveries (orders_with_items, full timestamps) | 7,826 |
| On-time delivery rate (orders_with_items, %) | 91.89% |
| Late delivery rate (orders_with_items, %) | 8.11% |
| Eligible orders (full timestamps, full dataset) | 96,476 |
| On-time orders (full timestamps, full dataset) | 88,649 |
| Late orders (full timestamps, full dataset) | 7,827 |
| On-time delivery rate (full timestamps, %) | 91.89 |
| Late delivery rate (full timestamps, %) |8.11 |
| Average actual-minus-estimated delivery time | -11.18 days |
| Average delay among late orders | 9.55 days |
| Average purchase-to-approval time | 10.42 hours |
| Average purchase-to-carrier handover time | 77.79 hours |
| Total freight cost | R$2,251,909.54 |
| Average freight per order | R$22.82 |
| Median freight per order | R$17.17 |
| Total product value | R$13,591,643.70 |
| Product-only Average Order Value | R$137.75 |
| Average Order Value including freight | R$160.58 |

### 6. Analysis Performed

#### 6.1 Order Status and Cancellation Analysis

Order counts and percentages were calculated for the available order statuses. Cancellation rates were calculated separately for all unique orders and for orders with item-price records.

The full dataset contains 625 canceled orders, corresponding to a cancellation rate of 0.63%. The subset with item-price records contains 461 canceled orders, corresponding to a rate of 0.47%.

#### 6.2 Delivery Duration Analysis

Delivery duration was calculated as the difference between the purchase date and the customer-delivery date, measured in whole calendar days. Delivered orders with valid timestamps and nonnegative delivery durations were included.

The documented average delivery duration was 12.50 calendar days.

#### 6.3 On-Time and Late Delivery Analysis

Actual customer-delivery timestamps were compared with estimated delivery timestamps.

- On-time deliveries were completed on or before the estimated delivery timestamp.
- Late deliveries occurred after the estimated delivery timestamp.

Two calculations were included in the analysis to support comparison between the Python results and the SQL validation results.

Method 1: Analysis using orders_with_items

Among 96,470 eligible delivered orders, 88,644 were on time and 7,826 were late. This corresponds to an on-time delivery rate of 91.89% and a late-delivery rate of 8.11%.

Method 2: Full-dataset analysis using timestamp comparison

Using the full orders dataset and including all orders with both actual and estimated delivery timestamps, 96,476 orders were evaluated. Of these, 88,649 were on time and 7,827 were late. The on-time delivery rate was 91.89%, while the late-delivery rate was 8.11%.

Comparison and validation

The results differ slightly because the first method uses orders_with_items and the second uses the full orders dataset without filtering by order status. The second method follows the same timestamp conditions as the SQL validation query.

For consistent reporting, the analysis should clearly identify which method is used for the final dashboard KPIs. The dataset, filters, and timestamp comparison rules should be consistent across Python, SQL, and Power BI.

#### 6.4 Delivery Delay and Processing Time

The analysis measured the difference between actual and estimated delivery times, average delay among late orders, purchase-to-approval time, and purchase-to-carrier handover time.

The documented average actual-minus-estimated delivery time was -11.18 days, indicating that actual deliveries occurred earlier than estimated on average under this calculation.

The average delay among late orders was 9.55 days.

#### 6.5 Monthly Order Trends

Orders were grouped by purchase month to identify changes in order volume over time. The monthly summary includes total orders, canceled orders, and cancellation rates.

#### 6.6 Freight Costs and Average Order Value

Order-item records were aggregated to calculate freight and product-value metrics.

The analysis documented total freight of R$2,251,909.54 and an average freight cost of R$22.82 per eligible order. The product-only average order value was R$137.75, increasing to R$160.58 when freight was included.

#### 6.7 Regional Performance Analysis

Orders were combined with customer-state information to evaluate cancellation rates, average delivery duration, and on-time delivery rates across states.

Regional summary tables and charts were generated to help identify geographical differences in logistics performance.

### 7. Visualizations

The analysis includes visualizations for:

- Order status distribution.
- On-time versus late deliveries.
- Monthly order trends.
- Cancellation rates by customer state.
- Average delivery duration by customer state.
- On-time delivery rates by customer state.
- On-time versus late delivery counts by customer state.

These visualizations provide an accessible view of order patterns and regional delivery performance.

### 8. Output Files

The notebook is designed to generate CSV summaries for use in further analysis and Power BI.

| Output file | Purpose |
|---|---|
| `kpi_summary.csv` | Consolidated KPI results |
| `order_status_summary.csv` | Order status counts and percentages |
| `monthly_order_trends.csv` | Monthly order and cancellation trends |
| `regional_cancellation_summary.csv` | Cancellation performance by customer state |
| `regional_delivery_summary.csv` | Delivery duration by customer state |
| `regional_on_time_summary.csv` | On-time and late delivery performance by customer state |

The notebook also generates PNG charts for the analyses listed in the visualization section.

### 9. Key Observations

Based on the documented results:

1. The full dataset contains 99,441 unique orders.
2. Total orders with item-price records are 98,666.
3. The cancellation rate across all orders is 0.63%.
4. The cancellation rate across all orders (with item data) is 0.47%.
5. The on-time delivery rate among eligible delivered orders is 91.89%.
6. Late deliveries account for 8.11% of eligible delivered orders.
7. The average delivery duration is 12.50 whole calendar days.
8. Freight costs represent an additional component of the average order value.
9. Regional analysis provides a basis for comparing logistics performance across customer states.

These observations describe the calculated results and do not independently establish the causes of delivery delays or cancellations.

### 10. Limitations

- Missing timestamps limit the number of orders eligible for some calculations.
- Different KPIs use different populations, particularly all orders versus orders with item-price records.
- Whole-calendar-day delivery duration differs from fractional elapsed-time calculations.
- Regional analysis is based on customer state and does not directly measure individual carrier performance.
- The findings are descriptive and do not establish causal relationships.
- Results depend on the exact cleaned and validated dataset used.

### 11. Conclusion

The Python analysis provides a structured assessment of order status, cancellation rates, delivery duration, delivery timeliness, processing times, freight costs, average order value, and regional logistics performance.

The documented results indicate that 91.89% of eligible delivered orders were on time, while 8.11% were late. The freight and order-value calculations provide additional insight into the cost of fulfilling orders.

The generated KPI summaries and visualizations can support the team's Power BI dashboard and help identify areas for further investigation.

---

**Project:** E-commerce Delivery & Logistics Performance Analysis  
**Analysis:** Python Analysis  
**Report file:** `python_analysis_summary.md`
