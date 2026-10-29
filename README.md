# E-commerce Delivery & Logistics Performance Analysis

## Project Overview

This project analyzes the Brazilian E-Commerce Public Dataset by Olist to understand order patterns, delivery performance, cancellation rates, order processing time, freight costs, and regional logistics performance.

The analysis is performed using Python and its data analysis and visualization libraries. The resulting KPI summaries, CSV files, and charts can support the team's Power BI dashboard.

**Project Role:** Python Analysis

## Objectives

- Analyze order status distribution and cancellation rates.
- Calculate average delivery duration using whole calendar days.
- Compare on-time and late deliveries.
- Measure delivery delays and order processing times.
- Analyze monthly order trends.
- Calculate freight costs and Average Order Value (AOV).
- Compare cancellation and delivery performance across customer states.
- Export summary tables and charts for Power BI visualization.

## Tools and Technologies

- **Python** — Data analysis and calculations
- **Pandas** — Data loading, cleaning, grouping, and aggregation
- **NumPy** — Numerical calculations and conditional operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical charts
- **Jupyter Notebook** — Interactive analysis and documentation
- **Power BI** — Dashboard development using exported summaries

## Datasets

The notebook uses four CSV files from the Olist Brazilian E-Commerce dataset.

| Dataset | Description | Rows |
|---|---|---:|
| Orders | Order status, purchase timestamps, approval, and delivery dates | 99,441 |
| Order Items | Product prices, freight costs, sellers, and order items | 112,650 |
| Customers | Customer IDs and customer-state information | 99,441 |
| Sellers | Seller IDs and seller-state information | 3,095 |

The analysis identifies **99,441 unique orders**, of which **98,666 orders have corresponding item-price records**.

## Project Structure

```text
Python_Analysis/
├── Python_analysis.ipynb
├── README.md
├── requirements.txt
├── reports/
│   └── python_analysis_summary.md
├── outputs/
│   ├── kpi_summary.csv
│   ├── order_status_summary.csv
│   ├── monthly_order_trends.csv
│   ├── regional_cancellation_summary.csv
│   ├── regional_delivery_summary.csv
│   └── regional_on_time_summary.csv
├── graphs/
    ├── order_status_distribution.png
    ├── on_time_vs_late_deliveries.png
    ├── monthly_order_trends.png
    ├── regional_cancellation_rate.png
    ├── regional_average_delivery_days.png
    ├── regional_on_time_delivery_rate.png
    └── regional_on_time_vs_late.png

```

## Analysis Performed

### 1. Data Loading and Quality Checks

- Loaded the four CSV datasets using Pandas.
- Examined dataset dimensions, columns, and data types.
- Checked missing values and duplicate rows.
- Converted relevant order timestamps to datetime format.
- Identified orders with available item-price records.

### 2. Order Status Distribution

Analyzed the number and percentage of orders in each status, including delivered, shipped, canceled, and other available statuses.

The notebook examines both the full order dataset and the subset of orders with item-price records.

### 3. Cancellation Analysis

Calculated the total number of canceled orders and the cancellation rate for:

- All unique orders.
- Orders with corresponding item-price records.

The two rates use different populations and should not be compared without considering their denominators.

### 4. Delivery Duration

Calculated delivery duration as the difference between the purchase date and the customer-delivery date, measured in **whole calendar days**.

Only delivered orders with valid purchase and delivery timestamps and nonnegative durations are included.

### 5. On-Time and Late Delivery Analysis

Compared actual customer-delivery timestamps against estimated delivery timestamps.

- **On time:** Actual delivery occurred on or before the estimated delivery date.
- **Late:** Actual delivery occurred after the estimated delivery date.

The notebook calculates the number of on-time and late orders and their respective percentages.

### 6. Delivery Delays and Processing Time

Calculated:

- Average actual-minus-estimated delivery time.
- Average delay among late orders.
- Average purchase-to-carrier handover time.
- Average purchase-to-approval time.

Negative processing intervals are excluded from the corresponding processing-time averages.

### 7. Monthly Order Trends

Grouped orders by purchase month and visualized changes in order volume over time.

### 8. Freight Costs and Average Order Value

Calculated order-level product and freight totals to analyze:

- Total freight cost.
- Average freight cost per order.
- Median freight cost per order.
- Total product value.
- Average product-only order value.
- Average order value including freight.

These calculations use orders with available item-price and freight data.

### 9. Regional Performance

Merged order information with customer-state data to compare:

- Cancellation rates by customer state.
- Average delivery duration by customer state.
- On-time and late delivery rates by customer state.

Regional charts highlight states with high cancellation rates, longer delivery durations, and high on-time delivery rates.

## Key Findings

The current notebook's documented results are:

| KPI | Result |
|---|---:|
| Total unique orders | 99,441 |
| Orders with item-price records | 98,666 |
| Canceled orders (full dataset) | 625 |
| Cancellation rate (full dataset) | 0.63% |
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
| Average purchase-to-carrier handover time | 77.79 hours |
| Average purchase-to-approval time | 10.42 hours |
| Total freight cost | R$2,251,909.54 |
| Average freight per order | R$22.82 |
| Median freight per order | R$17.17 |
| Total product value | R$13,591,643.70 |
| Product-only Average Order Value | R$137.75 |
| Average Order Value including freight | R$160.58 |



## KPI Definitions and Methodology

- **Cancellation rate:** Canceled unique orders divided by total unique orders in the specified population, multiplied by 100.
- **Delivery duration:** Whole calendar days between purchase and customer delivery. This differs from elapsed-time calculations that retain fractional days.
- **On-time delivery rate:** On-time delivered orders divided by delivered orders with both actual and estimated delivery timestamps, multiplied by 100.
- **Late delivery rate:** Late delivered orders divided by the same eligible delivery population, multiplied by 100.
- **Average delivery delay:** Mean of actual delivery time minus estimated delivery time, expressed in days. A negative result means delivery occurred earlier than estimated on average.
- **Average delay among late orders:** Mean delay for orders whose actual delivery timestamp was later than the estimated timestamp.
- **Average freight per order:** Total order-level freight divided by the number of eligible orders with item and freight data.
- **Product-only AOV:** Total product value divided by eligible orders with item data.
- **AOV including freight:** Total product value plus freight divided by the same eligible order population.

## How to Run the Notebook

### Requirements

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Steps

1. Download or clone the project repository.
2. Place the four required CSV files in a local folder.
3. Open `Python_analysis.ipynb` in Jupyter Notebook.
4. Update the `DATA_DIR` variable in the first loading cell to point to your dataset folder.
5. Run the notebook cells from top to bottom.
6. Review the generated KPIs, summary tables, and charts.
7. Verify the results against the team's validated data.
8. Upload the final notebook and required output files to the project repository.

### Configurable Dataset Path

Each team member should use the path to their own local dataset folder. For example:

```python
from pathlib import Path

DATA_DIR = Path(
    r"F:\jyoti\Tableau\Qveto\olist_cleaned_data_updated"
)
```

For improved portability, the notebook can use an environment variable named `OLIST_DATA_DIR` and retain a default path when the variable is not set. This allows team members to change the dataset location without modifying the analysis logic.

## Output Files

The notebook exports the following CSV summaries:

- `kpi_summary.csv`
- `order_status_summary.csv`
- `monthly_order_trends.csv`
- `regional_cancellation_summary.csv`
- `regional_delivery_summary.csv`
- `regional_on_time_summary.csv`

It also generates PNG charts for order status, monthly order trends, on-time versus late deliveries, and regional performance.

These outputs can be used as inputs for the team's Power BI dashboard.

## Limitations

- Missing timestamps reduce the number of records eligible for some delivery calculations.
- Different KPIs use different order populations; the full order dataset and the subset with item-price records must be distinguished.
- Whole-calendar-day delivery duration differs from fractional elapsed-day duration.
- Regional analysis describes performance by customer state, not by individual carrier.
- The analysis identifies descriptive patterns but does not establish the causes of cancellations or delivery delays.
- Results depend on the exact version of the cleaned and validated datasets used.

## Conclusion

The analysis evaluates order status, cancellations, delivery duration, delivery timeliness, processing time, freight costs, and customer-state performance.

The documented results show an on-time delivery rate of 91.89% and a late-delivery rate of 8.11% among eligible delivered orders. Freight and order-value metrics provide additional insight into logistics costs.

The exported KPI tables and charts can support an interactive Power BI dashboard and help the team identify areas for further investigation and improvement.

---

**Project:** E-commerce Delivery & Logistics Performance Analysis  
**Role:** Python Analysis  
**Status:** Validate the final outputs against the team's approved dataset before submission.
