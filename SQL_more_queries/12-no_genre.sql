-- Utilises a left join to select attributes ONLY in table A
SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC