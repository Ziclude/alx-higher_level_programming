#!/usr/bin/python3
""" Lists all states starting with N in the database. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], pwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in con.fetchall() if state[1][0] == "N"]
