import sqlite3

# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     query = "SELECT datetime('now', 'localtime');"
#     time = cursor.execute(query).fetchone()[0]
#     print(time)

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