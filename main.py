import sqlite3

connection = sqlite3.connect("coffee.sqlite")
cursor = connection.cursor()

result = cursor.execute("SELECT * FROM coffee").fetchall()

print(result)