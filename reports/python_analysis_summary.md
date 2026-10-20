**Python Analysis Summary – E-commerce Delivery & Logistics Project**

I have completed the initial Python analysis using Pandas, NumPy, Matplotlib, and Seaborn.

**Key findings:**
- Total orders: 99,441
- Cancellation rate: 0.63%
- Average delivery time: 12.56 days
- On-time delivery rate: 91.89%
- Average freight cost per order: R$22.82 BRL

I also analyzed monthly order trends, order status distribution, processing time, freight costs, and state-wise delivery performance.

**Missing Value Handling**

The orders dataset contains missing values in the approval, carrier handover, and customer delivery date columns. These missing values were investigated rather than automatically replaced.

Missing timestamps were retained because their actual values cannot be determined reliably from the available data. For delivery-related calculations, only records containing the required valid timestamps were included. Negative delivery durations were excluded as invalid records.

This approach avoids introducing artificial dates and helps maintain the reliability of the analysis.

**Deliverables:** Python notebook, 6 summary CSV files, and 6 visualization graphs for the project repository and further Power BI dashboard development.
