-- Creates a table called force_name where the name field cannot be null.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
