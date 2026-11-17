\# DATA QUALITY REPORT



\*\*Project:\*\* E-commerce Delivery and Logistics Performance Analysis  

\*\*Dataset:\*\* Olist Brazilian E-Commerce Public Dataset  

\*\*Prepared by:\*\* Lavanya  

\*\*Role:\*\* Data Cleaning and SQL



\## 1. Datasets Inspected



| Dataset | Records | Missing Values | Duplicate Rows Removed |

|---|---:|---:|---:|

| `olist\_customers\_dataset.csv` | 99,441 | 0 | 0 |

| `olist\_order\_items\_dataset.csv` | 112,650 | 0 | 0 |

| `olist\_orders\_dataset.csv` | 99,441 | 4,908 | 0 |

| `olist\_sellers\_dataset.csv` | 3,095 | 0 | 0 |



\## 2. Missing Values in Orders Dataset



| Column | Missing Values |

|---|---:|

| `order\_approved\_at` | 160 |

| `order\_delivered\_carrier\_date` | 1,783 |

| `order\_delivered\_customer\_date` | 2,965 |

| \*\*Total missing cells\*\* | \*\*4,908\*\* |



Missing timestamps were preserved rather than replaced with guessed values.



\## 3. Timestamp Conversion Validation



Five timestamp columns were checked before and after conversion.



| Timestamp Column | Missing Before | Missing After | Invalid Timestamps |

|---|---:|---:|---:|

| `order\_purchase\_timestamp` | 0 | 0 | 0 |

| `order\_approved\_at` | 160 | 160 | 0 |

| `order\_delivered\_carrier\_date` | 1,783 | 1,783 | 0 |

| `order\_delivered\_customer\_date` | 2,965 | 2,965 | 0 |

| `order\_estimated\_delivery\_date` | 0 | 0 | 0 |



\*\*Result:\*\* No invalid timestamps were detected during validation. Missing-value counts remained unchanged after conversion.



\## 4. SQL and Data Validation Results



\- \*\*Customer IDs:\*\* All 99,441 orders have matching customer IDs in the customers dataset.

\- \*\*Order IDs:\*\* All 112,650 order items have matching order IDs in the orders dataset.

\- \*\*Seller IDs:\*\* All order-item seller IDs match records in the sellers dataset.

\- \*\*Duplicate order IDs:\*\* None found in the orders dataset.

\- \*\*Duplicate customer IDs:\*\* None found in the customers dataset.

\- \*\*Duplicate `(order\_id, order\_item\_id)` combinations:\*\* None found in the order-items dataset.

\- \*\*Purchase and estimated delivery dates:\*\* No purchase timestamps occur after the estimated delivery dates.

\- \*\*Purchase and actual delivery dates:\*\* No actual customer delivery timestamps occur before purchase timestamps.



\## 5. Delivery Performance Findings



\- Orders delivered after the estimated delivery date: \*\*7,827\*\*

\- Orders missing customer delivery timestamps: \*\*2,965\*\*



\### Missing Customer Delivery Timestamps by Order Status



| Order Status | Missing Customer Delivery Timestamps |

|---|---:|

| Shipped | 1,107 |

| Canceled | 619 |

| Unavailable | 609 |

| Invoiced | 314 |

| Processing | 301 |

| Delivered | 8 |

| Created | 5 |

| Approved | 2 |

| \*\*Total\*\* | \*\*2,965\*\* |



\## 6. Investigation of Eight Delivered Orders



Eight orders are marked as `delivered` but have missing customer delivery timestamps.



Findings:



\- All eight orders have estimated delivery dates.

\- Seven orders have carrier delivery timestamps.

\- One order is missing both the carrier delivery timestamp and the customer delivery timestamp.

\- All eight orders have corresponding order-item records.

\- Each affected order has one order item with recorded price and freight charges.



\*\*Conclusion:\*\* The available timestamps are insufficient to determine the actual customer delivery time for these eight orders. Their delivery punctuality cannot be confirmed from the available timestamps alone.



Affected order details are saved in:



`reports/delivered\_orders\_missing\_timestamps.csv`



These records have been preserved. No dates were invented, and no records were deleted solely because timestamps were missing.



\## 7. Cleaning Approach



\- Original CSV files are preserved in `data/raw/`.

\- Cleaned datasets are saved in `data/interim/`.

\- Exact duplicate rows were checked; none were found in the four datasets.

\- Date and timestamp columns were converted using Pandas.

\- Missing values were preserved and documented.

\- SQL queries were used to validate table relationships and data quality.

\- Identified anomalies were documented for further investigation.



\## 8. Scripts and Outputs



| File | Purpose |

|---|---|

| `src/data\_inspection.py` | Inspects datasets and identifies data quality issues. |

| `src/data\_cleaning.py` | Cleans datasets and converts timestamp columns. |

| `src/validate\_timestamps.py` | Validates timestamp conversions and missing-value counts. |

| `src/investigate\_missing\_deliveries.py` | Identifies delivered orders missing customer delivery timestamps. |

| `sql/data\_validation.sql` | Contains SQL validation queries. |

| `reports/sql\_validation\_results.txt` | Stores SQL validation results. |

| `reports/delivered\_orders\_missing\_timestamps.csv` | Contains details of the eight affected orders. |



\## 9. Current Validation Status



\- Data cleaning script executed successfully.

\- Expected row counts were retained in all four cleaned datasets.

\- No duplicate rows were removed because none were found.

\- Timestamp validation reported zero invalid timestamps.

\- Existing missing values were preserved.

\- Eight delivered orders with missing customer delivery timestamps were identified and documented.

\- SQL queries were previously executed; final verification and README documentation remain to be completed before submitting the pull request.



\## 10. Cleaned Dataset Location



The cleaned CSV files are available in `data/interim/`.



The original, unmodified datasets remain in `data/raw/`.



\*\*END OF REPORT\*\*

