# E-commerce Delivery & Logistics Performance Analysis

A team data analytics project using the **Brazilian E-Commerce Public Dataset by Olist** to examine order activity, delivery performance, logistics-related costs, and data quality.

## Project at a Glance

| Item | Details |
|---|---|
| Project | E-commerce Delivery & Logistics Performance Analysis |
| Dataset | Brazilian E-Commerce Public Dataset by Olist |
| Tools | Python, Pandas, NumPy, Matplotlib, Seaborn, SQL, SQLite, Power BI |
| Dashboard file | `Dashboard.pbix` |
| Python notebook | `Python_analysis.ipynb` |

## Dataset Access

The original Olist CSV files are stored in Google Drive because of repository file-size considerations.

**[Access the raw dataset on Google Drive](https://drive.google.com/drive/folders/1412ahQ_Og__4_SDY6jv55iPk0M2rSJhF?usp=drive_link)**

The source files should remain unchanged. Store cleaned intermediate data in `data/interim/` and final analytical outputs in `data/processed/`. Do not publish personal or sensitive customer information in a public repository.

The analysis and dashboard described below use these four source tables:

| Dataset | Approximate rows | Main fields used |
|---|---:|---|
| Orders | 99,441 | Order ID, customer ID, status, purchase and delivery timestamps |
| Order Items | 112,650 | Order ID, item ID, product ID, seller ID, price, freight |
| Customers | 99,441 | Customer ID, customer city, customer state |
| Sellers | 3,095 | Seller ID, seller city, seller state |

## Project Objectives

- Inspect and document the source datasets and their quality.
- Examine order-status distribution and cancellations.
- Measure delivery duration, on-time delivery, and late delivery.
- Calculate processing-time and freight-cost metrics where the required fields are available.
- Compare delivery and cancellation patterns across customer states.
- Provide reproducible analysis outputs that can support a Power BI dashboard.
- Translate observed patterns into operational questions and recommendations without claiming unsupported causation.

## Repository Structure

```text
ecommerce-delivery-logistics-analysis/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
├── outputs/
├── powerbi/
├── reports/
│   └── figures/
├── docs/
├── sql/
├── src/
├── Dashboard.pbix
├── Python_analysis.ipynb
├── README.md
└── requirements.txt
```

Keep original source files unchanged. Keep reusable Python scripts under `src/`, SQL queries under `sql/`, notebooks under `notebooks/`, generated charts under `reports/figures/`, and final datasets under `data/processed/`. Update this tree if the actual repository layout differs.

## Data Cleaning and SQL Validation

The data-cleaning workflow documented by the team includes:

- Inspecting dataset dimensions, columns, and data types.
- Checking duplicate records and missing values.
- Converting available timestamp fields to datetime.
- Preserving missing values rather than filling them with invented values.
- Loading the four source tables into SQLite.
- Validating key relationships between orders, customers, order items, and sellers.

### Data-quality summary

| Dataset | Records | Duplicate rows removed | Missing values remaining |
|---|---:|---:|---:|
| Customers | 99,441 | 0 | 0 |
| Order Items | 112,650 | 0 | 0 |
| Orders | 99,441 | 0 | 4,908 |
| Sellers | 3,095 | 0 | 0 |

Missing values in the orders dataset were retained rather than filled with assumed values.

### Timestamp validation

| Timestamp column | Missing values |
|---|---:|
| Order purchase timestamp | 0 |
| Order approved at | 160 |
| Order delivered carrier date | 1,783 |
| Order delivered customer date | 2,965 |
| Order estimated delivery date | 0 |

The documented validation did not identify additional invalid timestamps. Missing-value counts remained unchanged.

### Missing delivery timestamp investigation

The documented investigation identified eight orders marked as delivered without a customer-delivery timestamp:

- Seven had a carrier-delivery timestamp.
- One was missing both carrier and customer-delivery timestamps.
- All eight had corresponding order-item records.

These records were flagged for investigation; no delivery dates were fabricated.

### SQL validation

The team documented 13 SQL validation queries covering table row counts, key relationships, duplicate IDs, missing delivery timestamps, and orders delivered after their estimated dates.

| Validation | Documented result |
|---|---:|
| Customers | 99,441 |
| Orders | 99,441 |
| Order Items | 112,650 |
| Sellers | 3,095 |
| Orders without matching customers | 0 |
| Order items without matching orders | 0 |
| Order items without matching sellers | 0 |
| Duplicate order IDs | 0 |
| Duplicate customer IDs | 0 |
| Duplicate seller IDs | 0 |
| Delivered orders missing customer-delivery timestamps | 8 |
| Orders delivered after estimated delivery date | 7,827 |

The team documentation states that all 13 SQL queries executed successfully. Keep the detailed query output in `reports/sql_validation_results.txt` if that file is included in the submitted repository.

## Python Analysis

The Python notebook documents analysis of:

1. Data loading and quality checks.
2. Order-status distribution.
3. Cancellation rates for the full order population and the subset with item-price records.
4. Delivery duration in whole calendar days.
5. On-time and late deliveries.
6. Delivery delay and order-processing intervals.
7. Monthly order trends.
8. Freight costs and average order value.
9. Regional comparisons by customer state.

### Documented Python results

| KPI | Result |
|---|---:|
| Total unique orders | 99,441 |
| Orders with item-price records | 98,666 |
| Canceled orders, full dataset | 625 |
| Cancellation rate, full dataset | 0.63% |
| Canceled orders, with item data | 461 |
| Cancellation rate, with item data | 0.47% |
| Average delivery duration | 12.50 calendar days |
| Eligible delivered orders with item data and full timestamps | 96,470 |
| On-time deliveries in that population | 88,644 |
| Late deliveries in that population | 7,826 |
| On-time delivery rate in that population | 91.89% |
| Late delivery rate in that population | 8.11% |
| Average actual-minus-estimated delivery time | -11.18 days |
| Average delay among late orders | 9.55 days |
| Average purchase-to-carrier handover time | 77.79 hours |
| Average purchase-to-approval time | 10.42 hours |
| Total freight cost | R$2,251,909.54 |
| Average freight per order | R$22.82 |
| Median freight per order | R$17.17 |
| Total product value | R$13,591,643.70 |
| Product-only average order value | R$137.75 |
| Average order value including freight | R$160.58 |

**Population note:** The full dataset and the subset of orders with item-price records are different populations. KPI denominators must be stated and should not be mixed. The notebook also documents full-dataset on-time and late counts separately.

## Power BI Dashboard

The documented Power BI report is a single-page dashboard built for a 1920 × 1080 (16:9) page.

### KPI cards

- Total Orders
- Total Freight
- Delivered Orders
- Average Delivery Days
- On Time Delivery %
- Total Sales
- Total Sellers

### Visuals

| Visual | Type | Purpose |
|---|---|---|
| Delivery performance | Pie chart | Orders split into on-time, late, and not delivered |
| Sales by price band | Treemap | Sales by price category |
| Delay severity | Donut chart | Late orders by delay category |
| Delivery rate | Gauge | Delivered orders against total orders |
| Orders vs. delivered by month | Line and clustered column chart | Monthly order and delivery counts |
| Order growth | Area chart | Order counts by approval year |
| Monthly revenue | Column chart | Sales by purchase month |

### Filters

- Order status
- Order purchase date
- Purchase year
- Seller state
- Customer city

### Data model

The dashboard documentation describes four CSV source tables and three relationships:

- Orders to Customers: one-to-one, both-direction filtering.
- Order Items to Orders: many-to-one, single-direction filtering.
- Order Items to Sellers: many-to-one, single-direction filtering.

### Dashboard refresh instructions

The dashboard's Power Query sources were documented as using a machine-specific local folder path. Before refreshing on another computer:

1. Open `Dashboard.pbix` in Power BI Desktop.
2. Go to **Home → Transform data → Data source settings**.
3. Update the CSV source paths, or edit the `Source` step in Power Query.
4. Refresh the report.
5. Verify dashboard totals against the validated analysis outputs.

## KPI Definitions

- **Cancellation rate:** Cancelled unique orders divided by total unique orders in the stated population, multiplied by 100.
- **Delivery duration:** Whole calendar days between purchase and customer delivery for eligible delivered orders.
- **On-time delivery rate:** On-time delivered orders divided by delivered orders with both actual and estimated delivery timestamps, multiplied by 100.
- **Late delivery rate:** Late delivered orders divided by the same eligible delivery population, multiplied by 100.
- **Average delivery delay:** Mean of actual delivery time minus estimated delivery time. A negative value indicates delivery earlier than the estimate on average.
- **Average delay among late orders:** Mean delay for orders delivered after the estimated timestamp.
- **Product-only AOV:** Product value divided by eligible orders with item data.
- **AOV including freight:** Product value plus freight divided by the same eligible order population.

## Running the Python Notebook

Install the documented Python dependencies:

```bash
python -m pip install pandas numpy matplotlib seaborn jupyter
```

Then:

1. Download or access the four required CSV files.
2. Place them in a local dataset folder.
3. Open `Python_analysis.ipynb` in Jupyter Notebook.
4. Update the `DATA_DIR` variable in the data-loading cell to point to the local dataset folder.
5. Run the notebook from top to bottom.
6. Review the generated KPI tables and charts.

The notebook documentation also suggests using an `OLIST_DATA_DIR` environment variable to make the dataset path portable across team members' computers.

## Outputs

The Python analysis documentation lists these summary outputs:

- `kpi_summary.csv`
- `order_status_summary.csv`
- `monthly_order_trends.csv`
- `regional_cancellation_summary.csv`
- `regional_delivery_summary.csv`
- `regional_on_time_summary.csv`

It also lists PNG charts for order status, monthly trends, on-time versus late deliveries, and regional performance. Include these files in the repository only if they have actually been generated and checked.

## Limitations

- Missing timestamps reduce the number of records eligible for delivery calculations.
- Different KPIs use different populations; denominators must be documented.
- Whole-calendar-day duration differs from elapsed-time duration.
- Regional analysis is based on customer state and does not establish individual carrier performance.
- Descriptive associations do not prove the causes of cancellations or delays.
- Results depend on the exact dataset version and cleaning process used.
- The dashboard's local data-source paths must be updated before refresh on another computer.

## Conclusion

The project documentation describes analysis of order status, cancellations, delivery duration, delivery timeliness, processing intervals, freight costs, and customer-state patterns. The documented Python results report a 91.89% on-time delivery rate and an 8.11% late-delivery rate for the eligible delivered-order population with item data and complete timestamps.

These results can support operational review, subject to validation against the final approved dataset and the dashboard.

## Dataset Credit

Data: *Brazilian E-Commerce Public Dataset by Olist* (Kaggle), released under CC BY-NC-SA 4.0.

---

**Project:** E-commerce Delivery & Logistics Performance Analysis  
**Repository:** `ecommerce-delivery-logistics-analysis`
