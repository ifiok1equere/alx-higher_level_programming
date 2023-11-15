-- Top 3 cities temperature query
SELECT city, AVG(value) as avg_temp FROM hbtn_0c_0.temperatures WHERE month >= 7 AND month <= 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
