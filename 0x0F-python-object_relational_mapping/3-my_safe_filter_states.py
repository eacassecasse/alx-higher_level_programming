#!/usr/bin/python3
"""  A SQL injection safe query to display the state
that matches the one passed as argument from a database """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
