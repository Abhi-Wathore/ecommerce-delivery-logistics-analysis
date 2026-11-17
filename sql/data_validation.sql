-- =====================================================
-- PROJECT: E-commerce Delivery and Logistics Analysis
-- PURPOSE: Data validation and relationship checks
-- DATASET: Olist Brazilian E-Commerce
-- =====================================================


-- 1. Check total records in each table

SELECT 'customers' AS table_name, COUNT(*) AS total_records
FROM customers

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'order_items', COUNT(*)
FROM order_items

UNION ALL

SELECT 'sellers', COUNT(*)
FROM sellers;


-- 2. Validate orders against customers

SELECT COUNT(*) AS matched_orders
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id;


-- 3. Find orders without matching customers
-- Expected result: 0

SELECT COUNT(*) AS unmatched_orders
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;


-- 4. Validate order items against orders

SELECT COUNT(*) AS matched_order_items
FROM order_items i
INNER JOIN orders o
    ON i.order_id = o.order_id;


-- 5. Find order items without matching orders
-- Expected result: 0

SELECT COUNT(*) AS unmatched_order_items
FROM order_items i
LEFT JOIN orders o
    ON i.order_id = o.order_id
WHERE o.order_id IS NULL;


-- 6. Validate order items against sellers

SELECT COUNT(*) AS matched_seller_items
FROM order_items i
INNER JOIN sellers s
    ON i.seller_id = s.seller_id;


-- 7. Find order items without matching sellers
-- Expected result: 0

SELECT COUNT(*) AS unmatched_seller_items
FROM order_items i
LEFT JOIN sellers s
    ON i.seller_id = s.seller_id
WHERE s.seller_id IS NULL;


-- 8. Check duplicate order IDs in orders

SELECT order_id, COUNT(*) AS occurrences
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;


-- 9. Check duplicate customer IDs in customers

SELECT customer_id, COUNT(*) AS occurrences
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 10. Check duplicate seller IDs in sellers

SELECT seller_id, COUNT(*) AS occurrences
FROM sellers
GROUP BY seller_id
HAVING COUNT(*) > 1;


-- 11. Check missing delivery dates by order status

SELECT
    order_status,
    COUNT(*) AS missing_delivery_dates
FROM orders
WHERE order_delivered_customer_date IS NULL
GROUP BY order_status
ORDER BY missing_delivery_dates DESC;


-- 12. Count delivered orders with missing delivery dates

SELECT COUNT(*) AS delivered_orders_missing_delivery_date
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NULL;


-- 13. Count orders delivered after the estimated date

SELECT COUNT(*) AS late_delivered_orders
FROM orders
WHERE order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
  AND order_delivered_customer_date > order_estimated_delivery_date;