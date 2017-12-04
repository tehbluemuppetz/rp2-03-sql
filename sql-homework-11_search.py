
import sqlite3

with sqlite3.connect("newnum.db") as connection:

    c = connection.cursor()

    while(1):

        choice = raw_input("Enter DB action (valid choices are AVG, MAX, MIN and SUM or EXIT to end program): ")
        valid = ["AVG", "MAX", "MIN", "SUM", "EXIT"]

        if any(x in choice for x in valid):
            if choice == "AVG":
                c.execute("SELECT avg(value) FROM integers")
                print c.fetchall()

            elif choice == "MAX":
                c.execute("SELECT max(value) FROM integers")
                print c.fetchall()

            elif choice == "MIN":
                c.execute("SELECT min(value) FROM integers")
                print c.fetchall()

            elif choice == "SUM":
                c.execute("SELECT sum(value) FROM integers")
                print c.fetchall()

            elif choice == "EXIT":
                break


        else:
            print "Invalid choice (valid choices are AVG, MAX, MIN and SUM). "
