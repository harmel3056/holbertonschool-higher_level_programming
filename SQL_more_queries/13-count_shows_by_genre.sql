-- Utilises an inner join to select attributes from a database, and then counts them
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;