#!/usr/bin/python3
""" Lists all states from the database."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], pwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM states")
    [print(state) for state in con.fetchall()]
