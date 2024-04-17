#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float

class Amenity(BaseModel):
    """ class that represents Amenities in the system """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
