-- Top 3 cities temperature query
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE MONTH(month) IN (7, 8) GROUP BY cit
y ORDER BY avg_temp DESC LIMIT 3;
