# Python Analysis Report

## E-commerce Delivery & Logistics Performance Analysis

### 1. Project Overview

This project analyzes the Brazilian E-Commerce Public Dataset by Olist to understand order trends, delivery performance, order cancellations, processing times, freight costs, and regional differences.

The Python analysis was performed to calculate key performance indicators (KPIs), identify patterns in order fulfillment, and prepare summary tables and visualizations for an interactive Power BI dashboard.

### 2. Objectives

- Analyze order status distribution and cancellation rates.
- Calculate average delivery duration.
- Measure on-time and late delivery rates.
- Evaluate delivery delays and order processing times.
- Identify monthly order trends.
- Analyze freight costs and average order value.
- Compare delivery performance and cancellations across customer states.
- Export analysis results for Power BI visualization.

### 3. Tools and Technologies

- **Python** — Data analysis and calculations
- **Pandas** — Data cleaning, manipulation, grouping, and aggregation
- **NumPy** — Numerical calculations and conditional classification
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical charts and comparisons
- **Google Colab** — Development and execution environment

### 4. Datasets Used

Four datasets were used in the analysis:

| Dataset     | Records | Purpose                                                                    |
| ----------- | ------: | -------------------------------------------------------------------------- |
| Orders      |  99,441 | Order status, purchase dates, delivery dates, and estimated delivery dates |
| Order Items | 112,650 | Product prices and freight costs                                           |
| Customers   |  99,441 | Customer location and state-level analysis                                 |
| Sellers     |   3,095 | Seller location information                                                |

The initial data-quality checks found no duplicate rows in the four datasets. Missing values were present in some order timestamps, particularly carrier handover and customer delivery dates. These values were not arbitrarily imputed; calculations used the records with the required data.

### 5. Analysis Performed

**5.1 Order Status and Cancellation Analysis**

- Analyzed the distribution of orders by status.
- Calculated cancellation rates for the full order dataset and the subset with item-price records.
- Created a bar chart showing order status distribution.

**5.2 Delivery Duration Analysis**

- Calculated the average delivery duration in whole calendar days.
- Restricted the calculation to delivered orders with valid purchase and customer delivery timestamps.
- Excluded negative delivery durations.

**5.3 On-Time and Late Delivery Analysis**

- Compared actual customer delivery timestamps with estimated delivery timestamps.
- Classified eligible delivered orders as on time or late.
- Calculated on-time and late delivery percentages.
- Visualized the comparison using a bar chart.

**5.4 Delivery Delay and Processing Time**

- Calculated the difference between actual and estimated delivery dates.
- Measured average delay among orders delivered after their estimated dates.
- Calculated average purchase-to-carrier handover time and purchase-to-approval time.

**5.5 Monthly Order Trends**

- Grouped orders by purchase month.
- Analyzed changes in order volume over time.
- Created a line chart to visualize monthly order trends.

**5.6 Freight Cost and Average Order Value**

- Calculated total, average, and median freight costs per order.
- Calculated total product value.
- Calculated average order value with and without freight charges.

**5.7 Customer-State Performance**

- Calculated cancellation rates by customer state.
- Compared average delivery duration across customer states.
- Calculated on-time and late delivery rates by customer state.
- Created regional bar charts to highlight differences between states.

### 6. Key Findings

| Key Performance Indicator                    |              Result |
| -------------------------------------------- | ------------------: |
| Total unique orders                          |              99,441 |
| Orders with item-price records               |              98,666 |
| Canceled orders — full dataset               |                 625 |
| Cancellation rate — full dataset             |               0.63% |
| Cancellation rate — orders with item data    |               0.47% |
| Average delivery duration                    | 12.50 calendar days |
| Eligible delivered orders evaluated          |              96,470 |
| On-time deliveries                           |              88,644 |
| Late deliveries                              |               7,826 |
| On-time delivery rate                        |              91.89% |
| Late delivery rate                           |               8.11% |
| Average actual minus estimated delivery time |         −11.18 days |
| Average delay among late orders              |           9.55 days |
| Average purchase-to-carrier time             |         77.79 hours |
| Average purchase-to-approval time            |         10.42 hours |
| Total freight cost                           |      R$2,251,909.54 |
| Average freight per order                    |             R$22.82 |
| Median freight per order                     |             R$17.17 |
| Total product value                          |     R$13,591,643.70 |
| Average product-only order value             |            R$137.75 |
| Average order value including freight        |            R$160.58 |

*Note: The full-dataset cancellation rate and the rate for orders with item data use different populations. Delivery KPIs use only eligible delivered orders. The average actual-minus-estimated delivery time is negative because orders were delivered earlier than estimated on average.*

### 7. Visualizations Created

The analysis produced visualizations for:

- Order status distribution
- On-time versus late deliveries
- Monthly order trends
- Customer-state cancellation rates
- Average delivery duration by customer state
- On-time delivery rates by customer state
- On-time versus late delivery rates for selected customer states

These visualizations help communicate the analysis findings and support the development of a Power BI dashboard.

### 8. Output Files

The analysis generated CSV summary tables for use in Power BI, including:

- `kpi_summary.csv`
- `order_status_summary.csv`
- `monthly_order_trends.csv`
- `regional_cancellation_summary.csv`
- `regional_delivery_summary.csv`
- `regional_on_time_summary.csv`

Chart images were also saved during notebook execution. The final repository should include the required exported files in clearly named output and graphs folders.

### 9. Conclusion

The analysis found that 91.89% of eligible delivered orders arrived on or before their estimated delivery timestamps, while 8.11% arrived late. The average delivery duration was 12.50 calendar days. Freight costs totaled R$2.25 million across the orders with item data, with an average freight cost of R$22.82 per order.

Monthly trends, order status distribution, and customer-state comparisons provide further insight into order fulfillment and logistics performance. These findings can help identify areas for further investigation, improve delivery planning, and monitor logistics costs.

The generated summary tables and visualizations are intended to support an interactive Power BI dashboard.

**Scope limitation:** Regional findings represent customer-state performance, not carrier performance, because carrier identifiers were not available in the analyzed datasets. The analysis describes observed patterns and does not establish the causes of late deliveries or cancellations.

### 10. Repository Structure

A suggested organization for the GitHub repository is:

```text
Ecommerce-Delivery-Logistics-Analysis/Python_Analysis/
│
├── Python_analysis.ipynb
|
├── reports
│   └── Python_Analysis_Report.md
│
├── outputs/
│   ├── kpi_summary.csv
│   ├── order_status_summary.csv
│   ├── monthly_order_trends.csv
│   ├── regional_cancellation_summary.csv
│   ├── regional_delivery_summary.csv
│   └── regional_on_time_summary.csv
│
├── graphs/
│   ├── order_status_distribution.png
│   ├── on_time_vs_late_deliveries.png
│   ├── monthly_order_trends.png
│   ├── regional_cancellation_rate.png
│   ├── regional_average_delivery_days.png
│   └── regional_on_time_delivery_rate.png
│
└── README.md
```


