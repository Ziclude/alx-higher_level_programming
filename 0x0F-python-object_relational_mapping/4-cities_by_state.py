#!/usr/bin/python3
""" Displays all values in states who matched arguments. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT c.id, c.name, s.name FROM cities as c INNER JOIN states as s ON c.state_id = s.id ORDER BY c.id")
    [print(city) for city in c.fetchall()]
