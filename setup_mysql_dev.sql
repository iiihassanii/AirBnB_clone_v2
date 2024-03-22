
-- Create or use hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


-- Create or use hbnb_dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';


-- Grant privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';


-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';



FLUSH PRIVILEGES;
