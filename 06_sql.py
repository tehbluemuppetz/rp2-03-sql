# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # using for loop to iterate through DB, printing results line by line
    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print(row)

        
