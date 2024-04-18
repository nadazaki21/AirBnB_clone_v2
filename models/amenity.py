#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, getenv#, load_dotenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# load_dotenv()

if getenv("HBNB_TYPE_STORAGE")=="db":

    class Amenity(BaseModel, Base):
        """class that represents Amenities in the system"""

        
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity",viewonly=False
        )

else:
    class Amenity(BaseModel):
        """class that represents Amenities in the system"""
        name=""
