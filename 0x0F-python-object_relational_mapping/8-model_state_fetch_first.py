#!/usr/bin/python3
"""Script to fetch the first state from states table."""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    mk_session = sessionmaker(bind=engine)
    session = mk_session()
    first = session.query(State).first()
    print(first.id, first.name, sep=': ') if first else 'Nothing'
