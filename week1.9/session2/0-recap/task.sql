.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

SELECT name FROM driver;

SELECT name FROM menu_items WHERE price > 10;

SELECT postcode FROM restaurants WHERE postcode LIKE 'LS2%';

-- SELECT name FROM restaurants ORDER BY name LIMIT 3 WHERE cuisine = 'Thai';
SELECT name FROM restaurants WHERE cuisine == 'Thai' ORDER BY name LIMIT 3;
-- only 1 = sign and wrong order

-- final Q: 3