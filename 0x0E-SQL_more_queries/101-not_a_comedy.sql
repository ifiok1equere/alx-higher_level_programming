-- querying a database

SELECT DISTINCT title
FROM tv_shows RIGHT JOIN tv_show_genres
on tv_shows.id = tv_show_genres.show_id RIGHT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE name != "Comedy";
