-- Script that lists all the records in table second_table in the database hbtn_0c_0
-- in MySQL server and adds multiple rows in it.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
