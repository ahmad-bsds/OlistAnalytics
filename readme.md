# 🛍️ Olist Store – Data Analytics Case Study
This project analyzes data from the Olist Store, a Brazilian e-commerce marketplace that connects thousands of sellers with customers across the country. The analysis was driven by stakeholder-focused business questions aimed at uncovering key growth drivers, improving delivery performance, optimizing payment behavior, and understanding customer and seller dynamics. Using SQL and Python, we cleaned and explored the dataset, identified trends, and generated actionable insights. The entire workflow, including SQL scripts, EDA, and visual dashboards, has been documented and shared to support data-driven decision-making across teams.

📌 **Note:** I’ve documented all analysis steps, SQL queries, and exploratory notes in Notion for better readability and traceability.
🔗 \[Access the complete Notion workspace here]\({[notion link here](https://www.notion.so/Olist-Store-250959537bd080a19c94e5e0db724c68?source=copy_link)})

---

## 🏢 Project Background

Olist is a leading Brazilian e-commerce marketplace enabling small and medium-sized businesses to sell their products through major marketplaces.

* **Industry:** E-commerce / Online Marketplace
* **Active Years in Data:** 2016–2018
* **Scale:**

  * 99,441 unique customers
  * 3,095 sellers
  * 112,650 products sold
* **Business Model:** Marketplace platform connecting sellers to customers, handling sales, payments, and logistics coordination
* **Goal of Analysis:** Identify key drivers of growth, customer experience, and operational efficiency

Insights and recommendations are provided on the following key areas:

* **Category 1:** Product & Category Performance

* **Category 2:** Customer Behavior & Retention

* **Category 3:** Seller Performance & Reviews

* **Category 4:** Payment Behavior & Operational Logistics

* 📝 SQL scripts used for data cleaning and transformations are available in the `/sql_cleaning` folder.

* 📝 SQL scripts for business-targeted questions are available in the `/sql_analysis` folder.

* 📊 An interactive dashboard has been created for the internal teams to explore KPIs and trends (\[see dashboard link]\({notion link here})).

---

## 🗃️ Data Structure & Initial Checks

The main database schema is built around the `orders` table and links customers, sellers, products, payments, and reviews:

**Tables Overview**

* `customers` – customer demographics and locations
* `orders` – core order transactions
* `order_items` – line-level order data with product, seller, and pricing info
* `products` – product metadata
* `sellers` – seller information
* `geolocation` – city and state mappings
* `order_payments` – payments by method and installment
* `order_reviews` – customer feedback and satisfaction


---

## 📌 Executive Summary

### Overview of Findings

Our analysis reveals strong growth dynamics but also structural challenges impacting customer experience:

* **São Paulo** is the largest customer hub with >15% of orders, but **average delivery time exceeds 8 days**, hurting satisfaction.
* The **top four product categories drive 36% of revenue**, showing revenue concentration risk.
* **Peak demand** occurs from **5 AM to midnight**, especially at **11 AM, 2 PM, 4 PM, and 9 PM** on early weekdays, requiring inventory/logistics optimization.
* **75% of customers pay by credit card**, and **installment payments drive higher order values**.


---

## 📊 Insights Deep Dive

### Category 1: Product & Category Performance

* **Top Category:** Bed, Bath & Table leads sales; top four categories contribute 36% of total GMV.
* **Sales Growth:** Orders have grown consistently year over year, peaking in 2018.
* **Seasonality:** Q2 is strongest, Q4 is weakest — indicating seasonal promotions may be underutilized.


---

### Category 2: Customer Behavior & Retention

* 99,441 customers placed 99,441 orders (1:1 ratio shows almost no repeat buyers → retention opportunity).
* Customers cluster heavily in São Paulo, followed by Rio de Janeiro, Brasília, and Belo Horizonte.
* Peak shopping hours are 11 AM, 2 PM, 4 PM, and 9 PM, suggesting when to run campaigns.


---

### Category 3: Seller Performance & Reviews

* 3,095 sellers completed 98,666 orders.
* The **top 10 sellers account for over 10% of all orders** each.
* Some high-volume sellers have **below-average review scores**, showing scale ≠ quality.

---

### Category 4: Payment Behavior & Logistics

* **Credit card is used in 75% of orders**, followed by debit card.
* **Installments boost order values** (avg R\$130 with 3 installments vs R\$118 for 1 installment).
* Delivery delays are concentrated in São Paulo (>8 days avg) and require logistics improvement.


---

## 💡 Recommendations

1. Optimize logistics in São Paulo with local hubs, faster couriers, and strict SLAs.  
2. Diversify markets and products by expanding to Tier-2 cities and emerging categories.  
3. Strengthen seller ecosystem with stricter onboarding, audits, and support programs.  
4. Promote credit card installments to lift AOV and resolve payment anomalies.  

---

## ⚠️ Assumptions & Caveats

During data cleaning, several data quality issues were noted and handled as follows:

| Table        | Column                           | Issue          | Rowcount | Solvable? | Magnitude | Resolution                                                                                                                                    |
| ------------ | -------------------------------- | -------------- | -------- | --------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| orders       | order\_approved\_at              | Null values    | 160      | N         | \~0.1%    | Column not needed for analysis, following stakeholder questions.                                                                              |
| orders       | order\_delivered\_carrier\_date  | Null values    | 1783     | N         | \~1.8%    | Column not needed for analysis, following stakeholder questions.                                                                              |
| orders       | order\_delivered\_customer\_date | Null values    | 2965     | N         | \~3%      | Imputing this column may cause incorrect results; left as-is due to low magnitude.                                                            |
| products     | product\_category\_name          | Null values    | 610      | N         | 0.018%    | Left as-is due to low magnitude and no reliable way to impute.                                                                                |
| products     | product\_name\_lenght            | Null values    | 610      | N         | 0.018%    | Left as-is.                                                                                                                                   |
| products     | product\_description\_lenght     | Null values    | 610      | N         | 0.018%    | Left as-is.                                                                                                                                   |
| products     | product\_photos\_qty             | Null values    | 610      | N         | 0.018%    | Left as-is.                                                                                                                                   |
| order\_items | price, freight\_value            | Outlier values | 3        | Y         | 0.00002%  | Prices very low (0.85) with high freight values (18–22). Kept them as they don’t meaningfully affect mean and may represent rare valid cases. |


