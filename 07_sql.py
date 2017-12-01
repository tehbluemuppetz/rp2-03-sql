# SELECT statement where unicode indicators are removed from output

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname FROM employees")

    # fetchall() retreives all records from the query
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
