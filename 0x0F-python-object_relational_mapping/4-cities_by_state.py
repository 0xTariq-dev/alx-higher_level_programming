#!/usr/bin/python3
"""Module: 4-cities_by_state"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                LEFT JOIN states
                ON states.id = cities.state_id""")
    cities = cur.fetchall()
    print(*cities, sep='\n') if cities else 'Nothing'
    cur.close()
    conn.close()
