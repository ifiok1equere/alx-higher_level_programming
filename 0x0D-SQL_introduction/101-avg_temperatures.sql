-- Temperature #0
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
