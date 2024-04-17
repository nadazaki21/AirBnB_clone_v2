#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import Column,  String, DateTime, Integer


load_dotenv()



Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60) ,unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime() ,default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime(), nullable=False, default= datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        if kwargs:
            if kwargs.get("id", None) is None:
                #print("case1")
                self.id = str(uuid.uuid4())  
            else:
                self.id = kwargs["id"]
            
            for key, value in kwargs.items():
                #print("inside for loop")
                if key != '__class__' and key != "created_at" and key != "updated_at" and key != "id":
                    # print("first condition satisfied")
                    if key in dir(self.__class__):
                        # print("second condition satisfied")
                        # print(key)
                        setattr(self, key, value)
            #print(self)
        else:
            self.id = str(uuid.uuid4())


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        for key in dictionary.keys():
            if key == "_sa_instance_state":
                del dictionary[key]
                break
        return dictionary

    def delete(self):
        from models import storage
        del storage