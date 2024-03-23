#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
