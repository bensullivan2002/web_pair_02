DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    availability VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (name, availability) VALUES ('Ben house', 'free');
INSERT INTO spaces (name, availability) VALUES ('Emily house', 'free');
INSERT INTO spaces (name, availability) VALUES ('Harry house', 'occupied');
INSERT INTO spaces (name, availability) VALUES ('Josh house', 'free');
INSERT INTO spaces (name, availability) VALUES ('James house', 'occupied');
