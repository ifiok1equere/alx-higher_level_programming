#!/usr/bin/python3
'''This module  contains the class definition
of a City and an instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    '''This is a class definition of a City table in
    the hbtn_0e_6_usa database
    '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
