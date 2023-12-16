#!/usr/bin/python3
'''This module creates a city
and a state in the db hbtn_0e_100_usa
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # command line arguments for db credentials
    user = sys.argv[1]
    pwrd = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    # create a core point for the db
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                user, pwrd, port, db
                ),
            pool_recycle=3600
            )
    # create all the tables defined as Base and State classes
    Base.metadata.create_all(engine)

    # create Session to start talking to the db. This returns an object
    Session = sessionmaker(bind=engine)

    # instantiate a Session object
    session = Session()

    # create state and city in the db
    state_1 = State(name="California")
    city_1 = City(name="San Francisco")
    state_1.cities = [city_1]
    session.add(state_1)

    session.commit()
    session.close()
