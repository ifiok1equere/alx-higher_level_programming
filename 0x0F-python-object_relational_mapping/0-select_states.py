#!/usr/bin/python3
'''This module fetches all the states from the hbtn_0e_0_usa database'''

# -*- coding: utf-8
if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_username,
            passwd=mysql_password, db=database_name, charset="utf8"
            )

    cur = conn.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
