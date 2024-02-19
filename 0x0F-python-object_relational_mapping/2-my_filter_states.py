#!/usr/bin/python3
"""  Displays the state that matches the one passed as argument
from a database """

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
