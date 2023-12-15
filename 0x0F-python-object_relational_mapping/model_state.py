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
    '''This is a class definition of a State table in
    the hbtn_0e_6_usa database
    '''
    __tablename__ = 'states'
    id = Column(
            Integer, unique=True, primary_key=True,
            autoincrement=True, nullable=False
            )
    name = Column(
            String(128, charset='latin1', collation='latin1_general_ci'),
            nullable=False
            )


engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            user, pwrd, port, db
            ),
        pool_recycle=3600, pool_pre_ping=True
        )
