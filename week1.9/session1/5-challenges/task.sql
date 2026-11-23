.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

.schema drivers
-- driver_id, name, vehicle, phone

-- BRONZE
SELECT name, price FROM menu_items WHERE restaurant_id = 3;
-- Red curry with prawns  │   9.5 
-- Massaman beef curry    │   7.5
-- Basil chicken          │   8.5
-- Tom yum soup           │   7.5
-- Vegetable spring rolls │   5.5
-- Pad see ew             │ 11.95
-- Pad Thai with chicken  │  9.95
-- Papaya salad           │ 10.95
-- Green curry with tofu  │ 11.95

SELECT name FROM restaurants WHERE cuisine = 'Indian';
-- Spice Route, Tandoori Nights, Dosa Corner, Curry Leaf

SELECT COUNT(*) FROM customers;
-- 180


-- SILVER

SELECT name, price FROM menu_items WHERE is_vegetarian = true AND price <= 8 ORDER BY price ASC;
-- Cheapest is Egg fried rice at £3.5

SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 ORDER BY hygiene_rating ASC;
-- Worst is Brooklyn Burger Co at 2/5 rating

SELECT name FROM restaurants WHERE postcode LIKE 'LS6%' ORDER BY hygiene_rating DESC;
-- If this student lives at the other side of the postcode's area to the restaurant, it could still take a while for delivery.

SELECT email FROM customers WHERE email LIKE '%leeds.ac.uk' ORDER BY joined_date DESC;
-- They should not send it as a lot of people with this address can and would be from other areas commuting to leeds.

SELECT * FROM orders WHERE status = 'cancelled' ORDER BY order_time DESC LIMIT 10;
-- No comment

SELECT name FROM menu_items WHERE is_vegetarian = true AND restaurant_id = 4;
SELECT name FROM menu_items WHERE restaurant_id = 4 ORDER BY price DESC LIMIT 1;
-- Most expensive dish is the pepperoni pizza


-- GOLD

SELECT * FROM orders WHERE order_time LIKE '%-10-%' AND status = 'placed';
-- All columns are included so the team has all the information about these orders as possible.

SELECT name, price FROM menu_items WHERE is_vegetarian = 1 ORDER BY price ASC LIMIT 5;
-- The error with this one was that ascending/descending was not chosen. 'ASC' was added. Also, the phrase order was mixed up. Ordering comes after 'WHERE'.
SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5;
-- This is the second one, which is incorrect. There is no ordering by price here. To get the correct answer, add 'ORDER BY price ASC' before 'LIMIT'

SELECT name, price FROM menu_items ORDER BY price ASC LIMIT 11;
-- Alot of the cheapest foods are the same price, so all should be given. In this case, 11 entries have the same price.