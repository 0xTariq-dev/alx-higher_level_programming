#!/usr/bin/python3
"""Model City: Defines Class City and Base."""
import sys
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """
    class: City
    Attributes:
        __tablename__ (string): The table name to be mapped to the class.
        id (int): The id column of the table.
        name (string): The name column value.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
