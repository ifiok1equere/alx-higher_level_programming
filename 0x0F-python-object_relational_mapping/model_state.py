#!/usr/bin/python3

# import sys
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

'''
user = sys.argv[1]
pwrd = sys.argv[2]
db = sys.argv[3]
port = 3306
'''

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


'''
engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            user, pwrd, port, db
            ),
        pool_pre_ping=True
        )

Base.metadata.create_all(engine)
'''
