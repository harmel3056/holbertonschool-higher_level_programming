-- Creates a MySQL user if it doesn't yet exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL ROLES ON *.* TO 'user_0d_1'@'localhost';
