-- Creates a table called id_not_null where the id field has a default value of 1.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
