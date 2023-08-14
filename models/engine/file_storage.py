#!/usr/bin/python3
"""
file_storage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "Place": Place,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Review": Review
                  }

    def all(self):
        """returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """serializes __objects to JSON file"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        """Dokeserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    class_name = value['__class__']
                    obj = self.class_dict[class_name](**value)
                    self.__class__.__objects[key] = obj
        except FileNotFoundError:
            pass
