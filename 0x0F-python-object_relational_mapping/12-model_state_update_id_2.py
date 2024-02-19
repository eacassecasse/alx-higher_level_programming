#!/usr/bin/python3
""" Updates the name of the State with ```id=2``` to ```New Mexico```
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    _instance = session.query(State).filter_by(id=2).first()
    _instance.name = 'New Mexico'
    session.commit()
