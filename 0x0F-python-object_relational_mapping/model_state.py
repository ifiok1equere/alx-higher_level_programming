#!/usr/bin/python3
'''This module  contains the class definition
of a State and an instance Base = declarative_base()
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = "root"
pwrd = "October1990#124#"
db = "hbtn_0e_6_usa"
port = 3306

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


# create a core point for the db
engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            user, pwrd, port, db
            ),
        pool_recycle=3600
        )

# create all the tables defined as Base and State classes
Base.metadata.create_all(engine)
