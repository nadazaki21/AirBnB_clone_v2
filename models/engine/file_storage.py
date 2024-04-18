#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        required_objs = {}
        if cls:
            
            if cls not in classes.values():
                print("** class doesn't exist **")
                return
            #print( "case 2 satisfied")
            for key, value in FileStorage.all(self).items():
                # print("here" +  key.split(".")[0])
                # print("here" + str(cls.__name__))
                if key.split(".")[0] == cls.__name__:
                    #print("here" +  key.split(".")[0])
                    #print("here" + cls)
                    required_objs[key] = value
            return required_objs
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    # object created appended to __objects
                    # print (classes[val['__class__']])
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

        # print("priting what's isnnide objetcts" + str(self.all()))

    def delete(self, obj=None):
        """delete obj from __objects if its inside - if
        obj is equal to None, the method should not do anything"""
        if obj == None:
            return
        for key, value in self.all().items():
            if key.split(".")[1] == obj.id:
                del self.all()[key]
                break
