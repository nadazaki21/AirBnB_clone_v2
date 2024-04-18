#!/usr/bin/python3
""" Storage engine 
    Stores in a SQL database using SQL Alchemy 
"""


from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData, select
from dotenv import load_dotenv
from os import getenv
from sqlalchemy.sql import text
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

load_dotenv()


class DBStorage:
    """Storage engine with SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """initiates a session object"""

        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        metadata = MetaData()
        metadata.reflect(bind=self.__engine)

        if getenv("HBNB_ENV") == "test":
            metadata.drop_all()
            self.__session.commit()

    @classmethod
    def all(self, cls=None):
        """query on the current database session (self.__session) all objects depending
        of the class name (argument cls), if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review)"""

        model_classes = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        
        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

        if cls is None:
            result_dict = {}
            for the_class in model_classes.values():
                query_obj = self.__session.query(the_class).all()
                for item in query_obj:
                    result_dict[item.__class__.__name__ + "." + item.id] = item
            #print(result_dict)
            return result_dict
                    
            
        else:
            if cls not in model_classes.keys():
                return None
            else:
                query_obj = self.__session.query(model_classes[cls]).all()

            result_list = []

            for item in query_obj:
                result_list.append(item)

            return result_list

    def new(self, obj):
        """add the object to the current database session"""
        # print(" will add obj")
        self.__session.add(obj)
        # print(" obj added ")

    def save(self):
        """commit all changes of the current database session"""
        # print (" will commit")
        self.__session.commit()
        # print("commited")

    def delete(self, obj=None):
        """delete from the current database session obj (row -record) if not None"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        #all classes that inherit from the class base should be imported
        from models.base_model import Base
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
