-- query new db

SELECT title, genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_shows.id IS NULL OR tv_show_genres.show_id IS NULL
ORDER BY title ASC, genre_id ASC;
