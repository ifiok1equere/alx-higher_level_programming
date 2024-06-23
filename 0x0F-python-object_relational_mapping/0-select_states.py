#!/usr/bin/python3
"""Connecting to the hbtn_0e_0_usa db using the MySQLdb module"""

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=usr,
            passwd=pwd, db=db_name, charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
