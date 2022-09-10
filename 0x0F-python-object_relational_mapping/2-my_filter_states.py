#!/usr/bin/python3
""" Displays all values in states who matched arguments. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    states = con.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    con.close()
    db.close()
