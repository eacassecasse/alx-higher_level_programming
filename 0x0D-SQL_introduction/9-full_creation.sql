# Creates a new table ``second_table`` inside a database
# passed as argument to command line and insert data
CREATE TABLE IF NOT EXISTS second_table
(
    id    INT,
    name  VARCHAR(256),
    score INT
);

INSERT INTO second_table
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
