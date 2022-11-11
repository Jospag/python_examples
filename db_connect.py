import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    time = cursor.execute(query).fetchone()[0]
    print(time)

# Actual connection to the db
connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
    );"""
)
cursor.execute(
    """INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42
    );"""
)
connection.commit()
connection.close()

cursor.execute("DROP TABLE People;")

connection.commit()
connection.close()

# With with key word

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
    );"""
)
cursor.execute(
    """INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42
    );""")

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
cursor.executescript(
    """DROP TABLE IF EXISTS People;
    CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
    );""")

people_values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28)
)

cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
