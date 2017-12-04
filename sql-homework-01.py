
import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

try:
    c.execute("INSERT INTO inventory VALUES('Ford', 'T', 30)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Fiesta', 20)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Taurus', 70)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Freed', 50)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Fit', 20)")

    connection.commit()

except sqlite3.OperationalError:
    print("DB insert operation error")

connection.close()
