#!/usr/bin/python3
"""
Utilises INNER JOIN and WHERE validation to extract
city names corresponding to an entered state, details
of which are spread across three tables in the db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
