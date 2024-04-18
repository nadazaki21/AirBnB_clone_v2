#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
from os import getenv

load_dotenv()

if getenv("HBNB_TYPE_STORAGE") == "db":

    class User(BaseModel, Base):
        """This class defines a user by various attributes"""

        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)

        places = relationship(
            "Place", back_populates="user", cascade="all, delete-orphan"
        )
        reviews = relationship(
            "Review", back_populates="user", cascade="all, delete-orphan"
        )

else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
