# Tables name
- orders
- customers
- cat_name_trans
- order_items
- products
- sellers
- geolocation
- order_payments
- order_reviews

# Exective questions
- How can we identify our most valuable customers and what factors drive their repeat purchases?
- Which regions or sellers have the highest delivery delays, and how do these delays impact customer review scores?
- Which product categories contribute the most to revenue and which are underperforming when accounting for returns and reviews?
- Which sellers are driving the most revenue per month, and what differentiates our top sellers from lower performers?
- Which customer regions have the highest growth potential, based on purchase frequency and average order value?


# Northstar
 1. How can we identify our most valuable customers and what factors drive their repeat purchases?

  Northstar Metric: Customer Lifetime Value (CLV)

  Supporting Metrics:
   - Repeat Purchase Rate = (Customers with 2+ purchases / Total customers) × 100
   - Average Order Value (AOV) = Total revenue / Number of orders
   - Purchase Frequency = Total orders / Unique customers
   - Customer Retention Rate = ((Customers at end of period - New customers during period) / Customers at start of period) × 100

  Data Requirements:
   - Customer identifiers (customer_id)
   - Order timestamps (order_purchase_timestamp)
   - Order values (price from order_items)
   - Customer segmentation data

  2. Which regions or sellers have the highest delivery delays, and how do these delays impact customer review scores?

  Northstar Metric: Delivery Performance Index = (On-time deliveries / Total deliveries) × Average review score

  Supporting Metrics:
   - Delivery Delay Rate = (Late deliveries / Total deliveries) × 100
   - Average Delivery Delay = Average (Actual delivery date - Estimated delivery date)
   - Review Score Correlation = Correlation between delivery delays and review scores
   - Regional Performance Score = Average review score by region

  Data Requirements:
   - Delivery dates (order_delivered_customer_date, order_estimated_delivery_date)
   - Seller information (seller_id)
   - Geographic data (customer_state, seller_state)
   - Review scores (review_score)

  3. Which product categories contribute the most to revenue and which are underperforming when accounting for returns and reviews?

  Northstar Metric: Category Profitability Index = (Category Revenue × Average Review Score) / Category Order Volume

  Supporting Metrics:
   - Revenue by Category = SUM(price) by product_category_name
   - Return Rate by Category = (Returned items / Total items) × 100
   - Category Review Score = Average(review_score) by product_category_name
   - Category Growth Rate = ((Current period revenue - Previous period revenue) / Previous period revenue) × 100

  Data Requirements:
   - Product information (product_category_name)
   - Order values (price from order_items)
   - Review scores (review_score)
   - Order timestamps for trend analysis

  4. Which sellers are driving the most revenue per month, and what differentiates our top sellers from lower performers?

  Northstar Metric: Seller Revenue Efficiency = Monthly Revenue per Seller / Average Delivery Time

  Supporting Metrics:
   - Monthly Seller Revenue = SUM(price) by seller_id per month
   - Seller Review Score = Average(review_score) by seller_id
   - Seller Delivery Performance = (On-time deliveries / Total deliveries) × 100 by seller_id
   - Seller Order Volume = Number of orders by seller_id

  Data Requirements:
   - Seller identifiers (seller_id)
   - Order values (price from order_items)
   - Delivery dates (order_delivered_customer_date, order_estimated_delivery_date)
   - Review scores (review_score)
   - Order timestamps

  5. Which customer regions have the highest growth potential, based on purchase frequency and average order value?

  Northstar Metric: Regional Growth Potential Index = (Purchase Frequency × Average Order Value) × (1 - Market Saturation)

  Supporting Metrics:
   - Regional Purchase Frequency = Total orders by region / Unique customers by region
   - Regional Average Order Value = Total revenue by region / Number of orders by region
   - Market Penetration Rate = (Customers in region / Total population in region) × 100
   - Regional Revenue Growth = ((Current period revenue - Previous period revenue) / Previous period revenue) × 100 by region

  Data Requirements:
   - Customer geographic data (customer_state from geolocation)
   - Order values (price from order_items)
   - Order timestamps
   - Customer identifiers (customer_id)

# Detailed Recommendations for Tracking and Measuring Success

  Based on the Northstar matrices defined above, here are my recommendations for implementation:

  1. Data Integration & Dashboard Development
   - Create a unified data model that joins all tables (orders, order_items, products, sellers, geolocation, payments, reviews)
   - Develop executive dashboards with drill-down capabilities for each Northstar metric
   - Implement automated data pipelines to refresh metrics daily/weekly

  2. Customer Value Tracking System
   - Implement a CLV calculation model that updates monthly based on customer behavior
   - Segment customers into value tiers (High/Medium/Low) based on CLV percentiles
   - Set up alerts for significant changes in repeat purchase rates

  3. Delivery Performance Monitoring
   - Create real-time delivery tracking that compares estimated vs. actual delivery dates
   - Develop heat maps showing regional delivery performance
   - Establish correlation analysis between delivery delays and customer satisfaction scores

  4. Product Category Performance Framework
   - Build category performance scorecards with revenue, review scores, and return rates
   - Implement trend analysis to identify emerging and declining categories
   - Create early warning systems for underperforming categories

  5. Seller Performance Benchmarking
   - Develop seller leaderboards with multiple performance dimensions
   - Create seller segmentation models (Top/Mid/Bottom tier)
   - Establish benchmarks for delivery performance and customer satisfaction by seller

  6. Regional Growth Analysis
   - Implement geographic analysis tools to identify high potential regions
   - Create predictive models for regional growth based on current trends
   - Develop market penetration tracking by region

  7. Success Measurement & KPIs
   - Set quarterly targets for each Northstar metric
   - Establish feedback loops to validate metric improvements with business outcomes
   - Create A/B testing frameworks to measure impact of initiatives on Northstar metrics

  These Northstar matrices and recommendations will provide a comprehensive framework for data-driven decision making and strategic planning for the Olist e-commerce platform.