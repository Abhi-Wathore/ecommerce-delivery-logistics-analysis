# Olist E-Commerce Sales & Delivery Performance Dashboard

A single-page Power BI dashboard that analyses sales and delivery performance for the **Olist Brazilian E-Commerce** dataset. It tracks order volume, revenue, freight, seller counts and, most importantly, how well orders are delivered against the estimated delivery date.

- **File:** `Dashboard.pbix`
- **Tool:** Microsoft Power BI Desktop
- **Page size:** 1920 × 1080 (16:9, fit to page) with a custom background image
- **Data period:** 27 Sep 2016 – 26 Sep 2018 (order purchase date range in the date slicer)

---

## Dashboard Overview

The page is organised as: KPI cards across the top, delivery-performance visuals in the middle, and time-trend visuals along the bottom. Filters (slicers) sit on the left edge and top-right.

### KPI Cards

| KPI | Measure |
|---|---|
| Total Orders | `Total Orders` |
| Total Freight | `Total Freight` |
| Delivered Orders | `Delivered Orders` |
| Average Delivery Days | `Average Delivery Days` |
| On Time Delivery % | `On Time Delivery %` |
| Total Sales | `Total Sales` |
| Total Sellers | `Total Sellers` |

### Charts

| Visual | Type | What it shows |
|---|---|---|
| Delivery performance | Pie chart | Total Orders split by Delivery Performance (On Time / Late / Not Delivered) |
| Sales by price band | Treemap | Total Sales by Price Category |
| Delay severity | Donut chart | Late Orders by Delivery Delay Category |
| Delivery rate | Gauge | Delivered Orders against Total Orders, with On Time Deliveries |
| Orders vs. delivered (monthly) | Line & clustered column combo | Total Orders and Delivered Orders by purchase month |
| Order growth | Area chart | Total Orders by order-approval year |
| Monthly revenue | Column chart | Total Sales by purchase month |

### Slicers (Filters)

- **Order status** (top)
- **Order date** – between-range slider on `order_purchase_timestamp`
- **Year** – from the order purchase date hierarchy
- **Seller state** – dropdown
- **Customer city** – dropdown

---

## Data Model

Four source tables loaded from CSV files (Olist public dataset), plus auto-generated date tables.

| Table | Rows (approx.) | Key columns |
|---|---|---|
| `olist_orders_dataset` | 99,441 | `order_id`, `customer_id`, `order_status`, purchase / approved / carrier / delivered / estimated dates |
| `olist_order_items_dataset` | ~112,000 | `order_id`, `order_item_id`, `product_id`, `seller_id`, `price`, `freight_value`, `shipping_limit_date` |
| `olist_customers_dataset` | 99,441 | `customer_id`, `customer_unique_id`, `customer_city`, `customer_state`, `customer_zip_code_prefix` |
| `olist_sellers_dataset` | 3,095 | `seller_id`, `seller_city`, `seller_state`, `seller_zip_code_prefix` |

### Relationships

```
olist_customers_dataset ──(1:1, both directions)── olist_orders_dataset ──(1:M)── olist_order_items_dataset ──(M:1)── olist_sellers_dataset
        customer_id                                       order_id                          seller_id
```

| From | To | Cardinality | Cross-filter |
|---|---|---|---|
| `olist_orders_dataset[customer_id]` | `olist_customers_dataset[customer_id]` | 1:1 | Both |
| `olist_order_items_dataset[order_id]` | `olist_orders_dataset[order_id]` | Many-to-one | Single |
| `olist_order_items_dataset[seller_id]` | `olist_sellers_dataset[seller_id]` | Many-to-one | Single |

---

## DAX Measures

All measures are stored in the `olist_customers_dataset` table.

| Measure | Logic |
|---|---|
| **Total Orders** | Distinct count of `order_id` |
| **Delivered Orders** | Distinct orders where `order_status = "delivered"` |
| **Total Sales** | Sum of item `price` |
| **Total Freight** | Sum of `freight_value` |
| **Total Items** | Row count of order items |
| **Total Sellers** | Distinct count of `seller_id` |
| **Total Customers** | Distinct count of `customer_unique_id` |
| **Seller Orders** | Distinct count of `order_id` in the order items table |
| **Average Delivery Days** | Average of the `Delivery Days` calculated column |
| **On Time Orders / On Time Deliveries** | Distinct orders where `Delivery Performance = "On Time"` |
| **Late Orders** | Distinct orders where `Delivery Performance = "Late"` |
| **On Time Delivery %** | Delivered orders (with delivered and estimated dates present) that arrived on or before the estimated date, divided by all such delivered orders |

## Calculated Columns

| Column | Table | Logic |
|---|---|---|
| **Delivery Days** | Orders | Days from purchase to customer delivery (delivered orders only) |
| **Delivery Performance** | Orders | `Not Delivered`, `On Time` (delivered on or before the estimate) or `Late` |
| **Delivery Delay Category** | Orders | For late orders only: `1-2 Days`, `3-5 Days`, `6-10 Days`, `Above 10 Days` |
| **Price Category** | Order Items | `Low` (≤ 50), `Medium` (≤ 150), `High` (≤ 500), `Premium` (> 500) |

---

## Getting Started

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
2. Download the Olist dataset from Kaggle: *Brazilian E-Commerce Public Dataset by Olist*. You need these four files:
   - `olist_orders_dataset.csv`
   - `olist_order_items_dataset.csv`
   - `olist_customers_dataset.csv`
   - `olist_sellers_dataset.csv`
3. Open `Dashboard.pbix`.
4. The queries point to a local path (`D:\internship\PROJECTS\Praveen\`). Update it under **Home → Transform data → Data source settings → Change Source**, or edit the `Source` step of each query in Power Query.
5. Click **Refresh**.

---

## Key Questions This Dashboard Answers

- How many orders were placed, and how many were actually delivered?
- What share of deliveries arrive on time, and how late are the late ones?
- How long does delivery take on average?
- How do sales and order volume trend month to month and year to year?
- Which price bands drive the most revenue?
- How do results differ by seller state, customer city and order status?

---

## Project Structure

```
Dashboard.pbix
├── Report        – 1 page ("Dashboard"), 19 visuals, custom background image
├── Data Model    – 4 data tables + auto date tables, 3 relationships
├── Measures      – 13 DAX measures
└── Power Query   – 4 CSV import queries
```

## Dataset Credit

Data: *Brazilian E-Commerce Public Dataset by Olist* (Kaggle), released under CC BY-NC-SA 4.0.


