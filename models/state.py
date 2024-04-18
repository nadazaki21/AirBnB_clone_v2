#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from dotenv import load_dotenv
from os import getenv

load_dotenv()


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class"""
        __tablename__ = "states"
        @property
        def cities(self):
            """ getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id => It will be the FileStorage
            relationship between State and City """
            from models.city import City
            return [city for city in City.query().all() if city.state_id == self.id]

        name = Column(String(128), nullable=False)
        
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
else:
    class State(BaseModel):
        """ State class """
        name = ""
        