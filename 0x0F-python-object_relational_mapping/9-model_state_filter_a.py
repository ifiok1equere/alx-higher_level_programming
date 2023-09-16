#!/usr/bin/python3
"""This module lists all State objects from the hbtn_0e_6_usa database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def a_in_state(user, paswd, db):
    """This function lists all the states in the states tabele of the
    hbtn_0e_6_usa database containing the letter a.
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
            State.name.ilike('%a%')
            ).order_by(State.id)
#   states = session.query(State).order_by(State.id).first()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    a_in_state(user, paswd, db)
