#!/usr/bin/python3
""" Displays all values in states who matched arguments. """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf-8")
    con = db.cursor()
    con.execute(
