#!/usr/bin/python3
"""Script to fetch the first state from states table."""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    mk_session = sessionmaker(bind=engine)
    session = mk_session()
    match = session.query(State).filter(State.name == (argv[4],))
    try:
        print(match[0].id)
    except IndexError:
        print('Not found')
