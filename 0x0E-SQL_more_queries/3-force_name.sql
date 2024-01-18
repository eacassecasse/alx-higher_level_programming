-- Creates a new table ``force_name`` inside a database
-- passed as argument to command line
CREATE TABLE IF NOT EXISTS force_name
(
    id   INT,
    name VARCHAR(256) NOT NULL
);