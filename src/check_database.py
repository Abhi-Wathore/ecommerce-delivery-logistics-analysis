import sqlite3

database_path = "data/ecommerce_analysis.db"

connection = sqlite3.connect(database_path)

print("Database connected successfully!")

query = "SELECT name FROM sqlite_master WHERE type = 'table'"
tables = connection.execute(query).fetchall()

print("Tables found in database:")
for table in tables:
    print(table[0])

connection.close()