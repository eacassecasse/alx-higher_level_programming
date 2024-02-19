#!/usr/bin/python3
"""
A definition of State class and an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mdata = MetaData()
Base = declarative_base(metadata=mdata)


class State(Base):
    """
    Definition of the State Class

    Args:
    id(int): The identifier of the state
    name(str): The name of the state
    cities(list): Cities of the State
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
