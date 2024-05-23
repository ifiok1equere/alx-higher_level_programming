-- querying a db

SELECT name
FROM tv_genres
RIGHT JOIN tv_show_genres
ON id = genre_id
WHERE show_id = 8;
