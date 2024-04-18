#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Amenity(BaseModel, Base):
    """class that represents Amenities in the system"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
