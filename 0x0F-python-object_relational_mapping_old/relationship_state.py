#!/usr/bin/python3
"""Define class of a State and a Base Instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This class represents the state table in the hbtn_0e_6_usa database
    """

    __tablename__ = 'states'

    id = Column(Integer(), unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')
