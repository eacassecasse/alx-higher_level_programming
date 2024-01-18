-- Creates a new database ``hbtn_0d_usa`` with a table ``cities``
-- inside, where the id field is a primary key, auto generated and
-- not null, the state_id field in a reference for the id of the state
-- in the states table and the name field is not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
