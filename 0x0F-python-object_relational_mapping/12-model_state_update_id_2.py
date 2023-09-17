#!/usr/bin/python3
"""This module updates a State object from the hbtn_0e_6_usa database
with a particular id.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def update_state(user, paswd, db):
    """This function chnages/updates a state that with
    a particular id in the tabele of the hbtn_0e_6_usa database.
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'

    session.commit()
    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    update_state(user, paswd, db)
