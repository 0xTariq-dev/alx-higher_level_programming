#!/usr/bin/python3
"""Script to prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    mk_session = sessionmaker(bind=engine)
    session = mk_session()
    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)
    session.add(california, san_francisco)
    session.commit()
