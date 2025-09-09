SELECT schemaname, tablename
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;

-- We have customers, products, and sellers information. This potenstially can help me
-- check where customers belong, what they buy, and how they feel. What are the the available
-- products and who sell them.

select *
from customers;

select distinct count(customer_id)
from customers;

-- there are 99, 441 unique customers.

select *
from geolocation;

-- geolocation table provides addtional long-lat to the location,
-- But it dont have unique id, then how it will be connect to custoemrs?

select *
from order_items;

-- It gaves us order details price, fright, data, also with unique keys to product id and seller id.

select distinct count(order_id)
from order_items;


-- 112,650 unique orders.

select * 
from products;


select *
from orders;

select *
from sellers;


-- So we have where seller belong, whats they order status how payments made. What has been bought and how user reviewd them.



/*
 * SUMMARY:
 * The Olist dataset provides a relational view of an e-commerce marketplace, connecting customers,
 * sellers, and products through orders. It contains customer demographics, geolocation details,
 * order transactions, product information, seller data, and reviews—enabling analysis of customer behavior, 
 * product demand, seller performance, and overall marketplace dynamics.
 * */

