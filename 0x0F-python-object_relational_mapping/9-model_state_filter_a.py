#!/usr/bin/python3
"""This module lists all State objects
that contain the letter a from the
database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # query the db and print out information needed from the object returned
    result = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id)

    # result object is a list of objects that are classes representing each row
    # in the table
    for obj in result:
        print("{}: {}".format(obj.id, obj.name))

    session.close()
