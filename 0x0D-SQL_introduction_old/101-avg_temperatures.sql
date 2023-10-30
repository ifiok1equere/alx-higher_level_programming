-- Import in hbtn_0c_0 database this table dump: download

-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

SELECT city, AVG(value) as avg_temp FROM hbtn_0c_0.temperatures GROUP BY city ORDER BY AVG(value) DESC;
