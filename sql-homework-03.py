
import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

c.execute("SELECT * FROM inventory WHERE make = 'Ford'")

rows = c.fetchall()

for r in rows:
    print(r[0], r[1], r[2])

connection.close()
