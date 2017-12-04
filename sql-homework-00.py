
import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

c.execute("CREATE TABLE inventory (make TEXT, model TEXT, quantity INT)")

connection.close()
