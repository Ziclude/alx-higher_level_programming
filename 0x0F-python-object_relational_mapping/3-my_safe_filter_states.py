#!/usr/bin/python3
""" Displays all values in states who matched arguments. """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf-8")
    con = db.cursor()
    con.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    row = cursor.fetchall()
    for rw in row:
        print(rw)
    con.close()
    db.close()
