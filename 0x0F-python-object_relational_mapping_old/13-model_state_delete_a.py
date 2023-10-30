#!/usr/bin/python3
"""This module deletes some State objects from the hbtn_0e_6_usa database
with accoding to set condition.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def delete_state(user, paswd, db):
    """This function deletes State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
            State.name.ilike('%a%')
            ).order_by(State.id)
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_state(user, paswd, db)
