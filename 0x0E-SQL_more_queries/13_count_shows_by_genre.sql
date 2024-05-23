-- querying the db

SELECT name AS genre, count(name) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres ON genre_id = id
GROUP BY name 
ORDER BY number_of_shows DESC;
