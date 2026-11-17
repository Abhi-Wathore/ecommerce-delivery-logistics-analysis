# \# E-commerce Delivery and Logistics Performance Analysis

# 

# \*\*Technologies:\*\* Python, Pandas, SQL, SQLite, Power BI

# 

# \## 1. Project Overview

# 

# This project analyzes the Olist Brazilian E-Commerce Public Dataset to understand e-commerce delivery performance, logistics operations, and data quality.

# 

# Python and Pandas are used for data inspection and cleaning. SQL is used to validate records and relationships between datasets. Power BI can be used to build interactive dashboards and visualize delivery performance.

# 

# \## 2. Project Objectives

# 

# \- Inspect and clean the provided datasets.

# \- Identify missing values and duplicate records.

# \- Convert timestamp columns into consistent datetime formats.

# \- Validate relationships between customers, orders, order items, and sellers.

# \- Identify orders with missing delivery timestamps.

# \- Analyze late deliveries and order-status patterns.

# \- Prepare reliable data for visualization and further analysis.

# 

# \## 3. Technologies Used

# 

# \- \*\*Python:\*\* Data processing and automation.

# \- \*\*Pandas:\*\* Data inspection, cleaning, and timestamp conversion.

# \- \*\*SQLite:\*\* Database storage and SQL validation.

# \- \*\*SQL:\*\* Record-count checks, relationship validation, duplicate checks, and delivery analysis.

# \- \*\*Power BI:\*\* Delivery-performance dashboards and visualizations.

# 

# \## 4. Project Folder Structure

# 

# ```text

# ecommerce-delivery-logistics-analysis/

# │

# ├── data/

# │   ├── raw/                  # Original datasets (not tracked by Git)

# │   ├── interim/              # Cleaned datasets (not tracked by Git)

# │   ├── processed/            # Further-processed datasets

# │   └── ecommerce\_analysis.db # SQLite database (not tracked by Git)

# │

# ├── src/

# │   ├── data\_inspection.py

# │   ├── data\_cleaning.py

# │   ├── load\_sqlite.py

# │   ├── check\_database.py

# │   ├── validate\_timestamps.py

# │   ├── investigate\_missing\_deliveries.py

# │   └── run\_sql\_validation.py

# │

# ├── sql/

# │   └── data\_validation.sql

# │

# ├── reports/

# │   ├── data\_quality\_report.md

# │   ├── sql\_validation\_results.txt

# │   └── delivered\_orders\_missing\_timestamps.csv

# │

# ├── notebooks/

# ├── .gitignore

# └── README.md

# ```

# 

# \## 5. Datasets

# 

# The project uses four CSV files from the Olist Brazilian E-Commerce Public Dataset.

# 

# | Dataset | Number of Records |

# |---|---:|

# | Customers | 99,441 |

# | Orders | 99,441 |

# | Order Items | 112,650 |

# | Sellers | 3,095 |

# 

# The original datasets are stored in `data/raw/`. Cleaned versions are stored in `data/interim/`.

# 

# \## 6. Data Cleaning Process

# 

# The cleaning process is implemented in `src/data\_cleaning.py`.

# 

# The script:

# 1\. Reads the original CSV files.

# 2\. Checks and removes duplicate rows.

# 3\. Converts available timestamp columns to datetime values.

# 4\. Handles invalid timestamp values using Pandas' `errors="coerce"` option.

# 5\. Saves the cleaned datasets to `data/interim/`.

# 6\. Reports original row counts, duplicate rows removed, final row counts, and remaining missing values.

# 

# The original datasets are preserved in `data/raw/`.

# 

# \### Data Quality Summary

# 

# | Dataset | Records | Duplicate Rows Removed | Missing Values Remaining |

# |---|---:|---:|---:|

# | Customers | 99,441 | 0 | 0 |

# | Order Items | 112,650 | 0 | 0 |

# | Orders | 99,441 | 0 | 4,908 |

# | Sellers | 3,095 | 0 | 0 |

# 

# Missing values in the orders dataset are retained rather than filled with invented values.

# 

# \## 7. Timestamp Validation

# 

# Timestamp validation is performed using `src/validate\_timestamps.py`.

# 

# | Timestamp Column | Missing Before Conversion | Missing After Conversion | Invalid Timestamps |

# |---|---:|---:|---:|

# | Order Purchase Timestamp | 0 | 0 | 0 |

# | Order Approved At | 160 | 160 | 0 |

# | Order Delivered Carrier Date | 1,783 | 1,783 | 0 |

# | Order Delivered Customer Date | 2,965 | 2,965 | 0 |

# | Order Estimated Delivery Date | 0 | 0 | 0 |

# 

# No additional invalid timestamps were identified during validation. Missing-value counts remained unchanged.

# 

# \## 8. Investigation of Missing Delivery Timestamps

# 

# The script `src/investigate\_missing\_deliveries.py` identifies orders marked as delivered that have no customer delivery timestamp.

# 

# Key findings:

# 

# \- Eight delivered orders have missing customer delivery timestamps.

# \- Seven of these orders have carrier delivery timestamps.

# \- One order is missing both carrier and customer delivery timestamps.

# \- All eight affected orders have corresponding order-item records.

# \- Actual customer delivery dates cannot be confirmed from the missing timestamps.

# 

# The affected records are exported to `reports/delivered\_orders\_missing\_timestamps.csv`.

# 

# These records are flagged for investigation rather than assigned estimated or fabricated delivery dates.

# 

# \## 9. SQL Validation

# 

# SQL queries are maintained in `sql/data\_validation.sql`.

# 

# The validation covers:

# 1\. Total records in each table.

# 2\. Orders matched to customers.

# 3\. Orders without matching customers.

# 4\. Order items matched to orders.

# 5\. Order items without matching orders.

# 6\. Order items matched to sellers.

# 7\. Order items without matching sellers.

# 8\. Duplicate order IDs.

# 9\. Duplicate customer IDs.

# 10\. Duplicate seller IDs.

# 11\. Missing customer delivery timestamps grouped by order status.

# 12\. Delivered orders missing customer delivery timestamps.

# 13\. Orders delivered after their estimated delivery dates.

# 

# \### SQL Validation Results

# 

# All 13 SQL queries executed successfully against the SQLite database.

# 

# | Validation | Result |

# |---|---:|

# | Customers | 99,441 |

# | Orders | 99,441 |

# | Order Items | 112,650 |

# | Sellers | 3,095 |

# | Orders without matching customers | 0 |

# | Order items without matching orders | 0 |

# | Order items without matching sellers | 0 |

# | Duplicate order IDs | 0 |

# | Duplicate customer IDs | 0 |

# | Duplicate seller IDs | 0 |

# | Delivered orders missing customer delivery timestamps | 8 |

# | Orders delivered after estimated delivery date | 7,827 |

# 

# Detailed query outputs are saved in `reports/sql\_validation\_results.txt`.

# 

# \## 10. Missing Delivery Timestamps by Order Status

# 

# | Order Status | Missing Customer Delivery Timestamps |

# |---|---:|

# | Shipped | 1,107 |

# | Canceled | 619 |

# | Unavailable | 609 |

# | Invoiced | 314 |

# | Processing | 301 |

# | Delivered | 8 |

# | Created | 5 |

# | Approved | 2 |

# | \*\*Total\*\* | \*\*2,965\*\* |

# 

# Missing delivery timestamps are documented as data-quality findings. They are not automatically interpreted as proof of a delivery failure.

# 

# \## 11. Setup and Execution

# 

# Run these commands from the project root directory.

# 

# \### Prerequisites

# 

# \- Python installed

# \- Pandas installed

# 

# Install Pandas if required:

# 

# ```bash

# python -m pip install pandas

# ```

# 

# \### Step 1: Inspect the Data

# 

# ```bash

# python src/data\_inspection.py

# ```

# 

# \### Step 2: Clean the Datasets

# 

# ```bash

# python src/data\_cleaning.py

# ```

# 

# \### Step 3: Load the Cleaned Data into SQLite

# 

# ```bash

# python src/load\_sqlite.py

# ```

# 

# \### Step 4: Validate Timestamps

# 

# ```bash

# python src/validate\_timestamps.py

# ```

# 

# \### Step 5: Investigate Missing Delivery Timestamps

# 

# ```bash

# python src/investigate\_missing\_deliveries.py

# ```

# 

# \### Step 6: Verify the Database Connection

# 

# ```bash

# python src/check\_database.py

# ```

# 

# \### Step 7: Run SQL Validation

# 

# ```bash

# python src/run\_sql\_validation.py

# ```

# 

# The SQL validation output is saved to `reports/sql\_validation\_results.txt`.

# 

# \## 12. Reports and Outputs

# 

# \- `reports/data\_quality\_report.md` — Summary of data quality and cleaning findings.

# \- `reports/sql\_validation\_results.txt` — Results from all 13 SQL validation queries.

# \- `reports/delivered\_orders\_missing\_timestamps.csv` — Orders requiring investigation because customer delivery timestamps are missing.

# \- `data/interim/` — Cleaned CSV datasets.

# \- `data/ecommerce\_analysis.db` — SQLite database containing the four datasets.

# 

# Generated datasets and the SQLite database are excluded from Git using `.gitignore`.

# 

# \## 13. Current Status

# 

# \- Data cleaning script executed successfully.

# \- Four datasets loaded into SQLite.

# \- Timestamp validation completed.

# \- Eight delivered orders with missing customer delivery timestamps identified and documented.

# \- All 13 SQL validation queries executed successfully.

# \- README documentation updated.

# 

# \## 14. Team Contribution

# 

# \*\*Responsibility:\*\* Data Cleaning and SQL

# 

# Tasks include data inspection, duplicate checks, timestamp conversion and validation, missing-value investigation, SQLite loading, SQL relationship validation, and preparation of data-quality reports.

