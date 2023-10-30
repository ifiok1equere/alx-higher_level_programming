-- Import in hbtn_0c_0 database this table dump: download (same as TemperatureE #0)

-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(value) as avg_temp FROM hbtn_0c_0.temperatures WHERE month >= 7 AND month <= 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
