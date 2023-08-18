-- Import in hbtn_0c_0 database this table dump: download (same as TemperatureE #0)

-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT state, MAX(value) as max_temp FROM hbtn_0c_0.temperatures GROUP BY state ORDER BY state;
