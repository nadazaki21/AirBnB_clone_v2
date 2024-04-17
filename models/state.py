#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    # def cities(self):
    #     """ Return the list of City instances with state_id equals to the current State.id """
    #     return [city for city in City.query().all() if city.state_id == self.id]