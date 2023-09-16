#!/usr/bin/python3
"""This module lists all State objects from the hbtn_0e_6_usa database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def state_search(user, paswd, db, search_state):
    """This function lists all the states in the states tabele of the
    hbtn_0e_6_usa database containing the letter a.
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search_state).first()

    if state is None:
        print('Not Found')
        return
    print('{}'.format(state.id))

    session.close()


if __name__ == "__main__":
    user, paswd, db, search_state = sys.argv[1], sys.argv[2], \
            sys.argv[3], sys.argv[4]
    state_search(user, paswd, db, search_state)
