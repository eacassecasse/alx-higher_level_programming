-- Creates a new table ``unique_id`` inside a database
-- passed as argument to command line, where the id is
-- unique and not null having 1 as default value
CREATE TABLE IF NOT EXISTS unique_id
(
    id   INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
