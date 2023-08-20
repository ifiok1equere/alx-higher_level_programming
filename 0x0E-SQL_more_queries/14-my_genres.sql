-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT
    name
FROM
    (SELECT genre_id FROM tv_show_genres WHERE tv_show_genres.show_id = 8) AS gen_id
INNER JOIN
    tv_genres ON gen_id.genre_id = tv_genres.id
ORDER BY name ASC;
