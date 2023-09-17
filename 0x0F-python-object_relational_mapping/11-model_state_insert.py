#!/usr/bin/python3
"""This module searches a State object from the hbtn_0e_6_usa database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def add_state(user, paswd, db):
    """This function print the id of a states that is searched for in the
    states tabele of the hbtn_0e_6_usa database.
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    add_state(user, paswd, db)
