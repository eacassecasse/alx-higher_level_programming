#!/usr/bin/python3
""" Lists all the cities with their corresponding States
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for _state in session.query(State).order_by(State.id):
        for _city in _state.cities:
            print(_city.id, _city.name, sep=": ", end="")
            print(" -> " + _state.name)
