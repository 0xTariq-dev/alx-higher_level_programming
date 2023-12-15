#!/usr/bin/python3
"""Module: 0-select_states"""

import MySQLdb
from sys import argv

conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name REGEXP '^N';")
states = [row for row in cur.fetchall()]
print(*states, sep='\n')
