-- QUERY db

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY max_temp DESC LIMIT 3;
