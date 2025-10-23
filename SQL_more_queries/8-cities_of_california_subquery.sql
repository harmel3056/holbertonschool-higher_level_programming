-- Lists cities in a database
SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;
