#!/usr/bin/python3
'''
This module lists Cities by states
'''
# -*- coding: utf-8
if __name__ == "__main__":
    import MySQLdb
    import sys

    # "SELECT * FROM states WHERE name = 'Arizona'; TRUNCATE TABLE states ;
    # SELECT * FROM states WHERE name = '' ORDER BY id ASC"

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_username,
            passwd=mysql_password, db=database_name, charset="utf8"
            )

    cur = conn.cursor()

    # query = "SELECT * FROM states WHERE name = '{:s}'
    # ORDER BY id ASC".format(sys.argv[4])
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id ORDER BY \
            cities.id ASC"

    # Here is where the SQL query is done;
    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
