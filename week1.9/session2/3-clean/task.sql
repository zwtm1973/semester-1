.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..

-- SELECT * FROM restaurants WHERE UPPER(cuisine) == 'THAI';
UPDATE restaurants SET cuisine = 'Italian' WHERE UPPER(cuisine) == 'ITALIAN'

UPDATE restaurants SET postcode = UPPER(TRIM(postcode));