#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    state = sys.argv[4]
    query = "SELECT cities.name FROM cities INNER JOIN states \
            ON cities.state_id = states.id WHERE states.name = '{}' \
            ORDER BY cities.id ASC".format(state)
    cur.execute(query)
    query_rows = cur.fetchall()
    result = ""
    for row in query_rows:
        result += ' '.join(map(str, row)) + ', '
    result = result[:-2]
    print(result)
    '''
    for row in query_rows:
        print(row)
    '''
    cur.close()
    conn.close()
