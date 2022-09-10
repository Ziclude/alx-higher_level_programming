#!/usr/bin/python3
"""Displays all cities of given state."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sysargv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM cities as c INNER JOIN states as s ON c.state_id = s.id ORDER BY c.id")
    print(", ".joint([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
