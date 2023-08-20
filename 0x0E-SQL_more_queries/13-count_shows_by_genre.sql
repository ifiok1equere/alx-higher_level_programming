-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT
    name as genre,
    COUNT(genre_id) as number_of_shows
FROM tv_genres
RIGHT JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY COUNT(genre_id) DESC;
