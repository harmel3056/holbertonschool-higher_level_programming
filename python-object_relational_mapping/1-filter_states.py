#!/usr/bin/python3
"""
Filters database results for names starting with N
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

cursor = db.cursor()

cursor.execute(
    "SELECT * FROM states "
    # LEFT targets leftmost chars of desired qty
    "WHERE LEFT(name, 1) = %s "
    "ORDER BY id ASC"
    )
cursor.execute(query, ('N',))

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
