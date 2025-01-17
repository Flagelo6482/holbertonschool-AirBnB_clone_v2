#!/usr/bin/python3


"""This module defines a class User"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import Place
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os


class User(BaseModel, Base):
    """defines the attributes to be stored in the DB"""
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', backref='user', cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        """defines the attributes to be stored in the JSON"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
