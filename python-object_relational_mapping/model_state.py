#!/usr/bin/python3
"""
Establishes a class definition for State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    'State' class which contains id and name
    """
    __tablename__ = 'states'
    # nullable=False not necessary for PRIMARY KEYS
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
