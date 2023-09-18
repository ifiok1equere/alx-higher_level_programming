#!/usr/bin/python3
"""Defines class of a City and a Base Instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """This class represents the cities table in the hbtn_0e_6_usa database
    """

    __tablename__ = 'cities'

    id = Column(Integer(), unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref='cities')
