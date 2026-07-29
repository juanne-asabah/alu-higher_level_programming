#!/usr/bin/python3
"""
Contains the class definition of a City.
Inherits from Base imported from model_state.
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    City class maps to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the table to map to.
        id (int): Auto-generated unique primary key integer.
        name (str): Maximum 128 characters string, cannot be null.
        state_id (int): Foreign key referencing states.id column.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
