import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
query = "SELECT datetime('now', 'localtime');"
time = cursor.execute(query).fetchone()[0]
print(time)

# with sqlite3.connect("test_database.db") as connection:
#     ... cursor = connection.cursor()
# ... query = "SELECT datetime('now', 'localtime');"
# ... time = cursor.execute(query).fetchone()[0]