
import sqlite3
import random

numbers = {}

with sqlite3.connect("newnum.db") as connection:

    c = connection.cursor()

    c.execute("DROP TABLE IF exists integers")
    c.execute("CREATE TABLE IF not exists integers(ind INT, value INT)")

    for i in range(0,100):
        j = random.randint(0,100)
        numbers[i] = j

    for entry in numbers:
        c.execute("INSERT INTO integers VALUES(?, ?)", (entry, numbers[entry]))
        connection.commit()
        # print entry, numbers[entry]
