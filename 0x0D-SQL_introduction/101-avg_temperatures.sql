-- import sql file into db and query

SELECT city, avg(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
