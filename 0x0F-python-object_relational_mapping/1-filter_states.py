#!/usr/bin/python3
"""Module: 1-filter_states"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name REGEXP '^N'
                ORDER BY states.id""")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    conn.close()
