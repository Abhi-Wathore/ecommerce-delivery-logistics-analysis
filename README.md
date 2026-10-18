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

Dataset description

Dataset	                        Actual rows       Columns	        Purpose
olist_orders_dataset.csv	       99,441	            8	          Order details, status, purchase and delivery dates
olist_customers_dataset.csv	     99,441	            5         	Customer identifiers, locations, and states
olist_order_items_dataset.csv 	 112,650	          7	          Items per order, sellers, item prices, and freight
olist_sellers_dataset.csv        3,095	            4	          Seller identifiers and locations

**These are the row counts in datasets, before any cleaning or filtering.**

!!! Important data-grain distinction: an order is not the same as an order item. One order can contain multiple items, so joining the order table directly to order items can increase the number of rows. This can distort order counts or other KPIs unless you use the correct aggregation.

Key columns and relationships

1.  orders.order_id → order_items.order_id
2.  orders.customer_id → customers.customer_id
3.  order_items.seller_id → sellers.seller_id

KPI definitions — use these in your documentation

  KPI	                            Professional definition	                                                    Raw-data baseline

Total orders	                 Count of distinct order_id values in the orders dataset	                         99,441

Delivered orders	             Count of orders with status delivered	                                           96,478

Average delivery time	         Average of actual delivery timestamp minus purchase timestamp, measured in days	 12.56 days

On-time delivery rate	         Eligible delivered orders delivered on or before the 
                                estimate date ÷ eligible delivered orders × 100	                                 91.89%

Late delivery rate	           Eligible delivered orders delivered after the 
                                estimated date ÷ eligible delivered orders × 100	                               8.11%

Total freight cost	            Sum of freight_value across order-item rows	                                     ₹2,251,909.54*

Average freight per order	      Total freight for each order, then average across orders with item records	      22.82*

Monthly order trend	            Count of distinct orders grouped by purchase month	                            To calculate

Order-status distribution	      Count and percentage of orders by order_status	                                To calculate

Excel data validation — your first findings

update after cleaning..................................

Excel validation formulas

  Validation	                Example formula
  
Total order rows	          =COUNTA(Orders[order_id])
Unique order IDs	          =ROWS(UNIQUE(Orders[order_id]))
Duplicate order IDs	        =COUNTA(Orders[order_id])-ROWS(UNIQUE(Orders[order_id]))
Missing order IDs	          =COUNTBLANK(Orders[order_id])
Total freight	              =SUM(OrderItems[freight_value])
Delivered order count	      =COUNTIF(Orders[order_status],"delivered")




