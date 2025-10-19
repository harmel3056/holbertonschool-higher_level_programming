-- Creates a table that specifies a unique ID
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
