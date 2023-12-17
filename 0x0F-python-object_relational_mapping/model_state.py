#!/usr/bin/python3
"""Model State: Defines Class State and Base."""
import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)

class State(Base):
	"""
    class: State
    Attributes:
        __tablename__ (string): The table name to be mapped to the class.
        id (int): The id column of the table.
        name (string): The name column value.
    """
	__tablename__ = 'states'
	id = Column(Integer, unique=True, nullable=False, primary_key=True)
	name = Column(String(128), nullable=False)