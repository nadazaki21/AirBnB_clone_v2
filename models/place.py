#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    user = relationship("User", back_populates="places")

    cities = relationship("City", back_populates="places")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def reviews_by_id(self):
            """getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id => It will be the FileStorage
            relationship between Place and Review"""

            return [
                review for review in Review.query().all() if review.place_id == self.id
            ]
