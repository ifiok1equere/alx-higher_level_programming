#!/usr/bin/python3
"""This module lists all City objects from the hbtn_0e_14_usa database
"""
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def list_states(user, paswd, db):
    """This function prints all the cities from the database
    hbtn_0e_14_usa in order of their city id's
    """

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
    
    session.close()


if __name__ == "__main__":
    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(user, paswd, db)
