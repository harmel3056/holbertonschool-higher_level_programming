-- Utilises multiple inner joins to select aliased, grouped attributes from a database, and then counts them
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;