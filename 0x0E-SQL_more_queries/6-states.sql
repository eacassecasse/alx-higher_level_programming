-- Creates a new database ``hbtn_0d_usa`` with a table ``states``
-- inside, where the id field is a primary key, auto generated and
-- not null and the name field is not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
    id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
