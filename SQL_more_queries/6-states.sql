-- Creates a database and a table with a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY DEFAULT 1,
	name VARCHAR(256) NOT NULL
	);
