
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
);

INSERT INTO inventory (NAME, quantity, price)
VALUES ('Sunflower oil', 3, 1.29);

SELECT * FROM inventory;
