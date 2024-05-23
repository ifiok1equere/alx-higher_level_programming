-- querying a db

SELECT title, name
FROM tv_genres
RIGHT JOIN tv_show_genres
ON id = genre_id
RIGHT JOIN tv_shows on show_id = tv_shows.id
ORDER BY title ASC, NAME ASC;
