#!/usr/bin/python3
"""This module lists all State objects from the hbtn_0e_6_usa database
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    import sys

    user, paswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
            conn_str.format(user, paswd, db, pool_pre_ping=True)
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(str(instance.id) + ': ' + instance.name)
