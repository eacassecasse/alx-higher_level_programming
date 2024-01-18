-- Creates a new table ``id_not_null`` inside a database
-- passed as argument to command line, where the id is
-- not null having 1 as default value
CREATE TABLE IF NOT EXISTS id_not_null
(
    id   INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);

