
import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

try:

    c.execute("UPDATE inventory SET quantity = 77 WHERE model = 'T'")
    c.execute("UPDATE inventory SET quantity = 55 WHERE model = 'Freed'")

    connection.commit()

except sqlite3.OperationalError:
    print("Error when executing SQL update statement")

c.execute("SELECT * FROM inventory")

rows = c.fetchall()

for r in rows:
    print(r[0], r[1], r[2])

connection.close()
