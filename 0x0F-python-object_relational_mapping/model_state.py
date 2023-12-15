#!/usr/bin/python3
'''This module  contains the class definition
of a State and an instance Base = declarative_base()
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''This is a class
    definition of a State
    object mapped to the states table
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(
            String(128, charset='latin1', collation='latin1_general_ci'),
            nullable=False
            )
