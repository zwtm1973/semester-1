.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- A
-- rows 1,3,5

-- B
-- rows 1,3

-- C
-- row 4

-- D
-- row 3,4

SELECT name, price FROM menu_items
ORDER BY price DESC LIMIT 10;