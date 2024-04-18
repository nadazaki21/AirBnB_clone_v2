#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, getenv ,load_dotenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State

load_dotenv()

if getenv("HBNB_TYPE_STORAGE")=="db":
    class City(BaseModel, Base):
        """The city class, contains state ID and name"""

        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        # places = relationship(
        #     "Place",
        #     backref="city",
        #     cascade="delete",
        #     passive_deletes=True
        # )

        places = relationship(
            "Place", back_populates="cities", cascade="all, delete-orphan"
        )
        state = relationship("State", back_populates="cities")
else:
    class City(BaseModel):
        name = ""
        state_id = ""