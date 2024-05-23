-- querying a db

SELECT DISTINCT new_table.name 
FROM (
	SELECT *
	FROM tv_show_genres AS sg 
	LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
) AS new_table 
LEFT JOIN tv_shows AS newest 
ON new_table.show_id = newest.id 
WHERE new_table.id NOT IN (6, 1, 2, 7, 8) 
ORDER BY new_table.name ASC LIMIT 3;
