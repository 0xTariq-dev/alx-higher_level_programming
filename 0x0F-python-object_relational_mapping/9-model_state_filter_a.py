#!/usr/bin/python3
"""Script to fetch the states that contains the letter 'a' from states table"""

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
    states = [f"{st.id}: {st.name}" for st
              in session.query(State)
              .filter(State.id, State.name.contains("%a%"))]
    print('\n'.join(states)) if states else print('Nothing')
