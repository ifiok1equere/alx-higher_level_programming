-- query a table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC ORDER BY score DESC;
