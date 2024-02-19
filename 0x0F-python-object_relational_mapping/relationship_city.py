#!/usr/bin/python3
"""
A definition of City class
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Defines the model for a city

    Args:
        id(int): The identifier of the city
        name(str): The name of the city
        state_id(int): The state where the city belongs
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
