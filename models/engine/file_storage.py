#!/usr/bin/python3
""" file_storage.py defines FileStorage class"""

import json
import sys
from models.base_model import BaseModel

class FileStorage:
    "serializes instances to a JSON file and deserializes JSON file to instances"
    __file_path = "file.json"
    __objects = {}
    # def __init__(self):
    #     pass


    def all(self):
        "returns the dictionary __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"

        obj_dict = FileStorage.__objects
        dict_of_obj = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_of_obj, f)


    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                # Read the JSON data from the file
                json_data = json.load(file)
                # Check if the data is a dictionary (expected format)
                if isinstance(json_data, dict):
                    self.__objects = {}  # Clear existing objects before reloading
                    for key, value in json_data.items():
                        # Extract class name and ID from the key
                        class_name, obj_id = key.split(".")
                        # Create a new instance of the corresponding class
                        new_obj = getattr(sys.modules[__name__], class_name)()
                        # Set attributes from the deserialized dictionary
                        for field, field_value in value.items():
                            if not field.startswith("__"):  # Skip private attributes
                                setattr(new_obj, field, field_value)
                        # Add the deserialized object to __objects
                        self.__objects[key] = new_obj
        except FileNotFoundError:
            # File not found, but don't raise an exception as per requirement
            return
