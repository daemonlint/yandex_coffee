import sqlite3

connection = sqlite3.connect("coffee.sqlite")
cursor = connection.cursor()

response = cursor.execute("SELECT * FROM coffee").fetchall()

print(response)