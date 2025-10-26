#!/usr/bin/python3
"""
Establishes a class definition for City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """
    'City' class which contains id and name
    """
    __tablename__ = 'cities'
    # nullable=False not necessary for PRIMARY KEYS
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
