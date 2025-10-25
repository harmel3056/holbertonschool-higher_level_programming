#!/root/venvs/sql_env/bin/python3
"""
Extracts values matching a name argument passed
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
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
        """
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
