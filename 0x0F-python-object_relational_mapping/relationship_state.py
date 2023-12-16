#!/usr/bin/python3
'''This module  contains the class definition
of a State and an instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''This is a class definition of a State table in
    the hbtn_0e_6_usa database
    '''

    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref="state", cascade="all, delete-orphan"
            )
