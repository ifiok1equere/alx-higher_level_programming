#!/usr/bin/python3
'''
This module Filter states stsrting with N from the hbtn_0e_0_usa database
'''
# -*- coding: utf-8

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host="localhost", port=3306, user="ifiok",
            passwd="1Fiok@equere", db="hbtn_0e_0_usa", charset="utf8"
            )

    cur = conn.cursor()

    # Here is where the SQL query is done;
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
