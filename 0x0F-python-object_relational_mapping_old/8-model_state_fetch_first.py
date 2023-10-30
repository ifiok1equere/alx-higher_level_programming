#!/usr/bin/python3
"""This module lists all State objects from the hbtn_0e_6_usa database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def first_state(user, paswd, db):
    """This function prints the state in the states tabele of the
    hbtn_0e_6_usa database
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states is None:
        print('Nothing')
        return
    print('{}: {}'.format(states.id, states.name))

    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    first_state(user, paswd, db)
