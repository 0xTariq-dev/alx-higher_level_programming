-- Script that lists all the records with a name in the table
-- second_table of the database hbtn_0c_0 in your MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
