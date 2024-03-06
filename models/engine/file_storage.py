#!/usr/bin/python3
class FileStorage:
    "serializes instances to a JSON file and deserializes JSON file to instances"
    __file_path = "file.json"
    __objects = {}
    def __init__(self):
        pass


    def all(self):
        "returns the dictionary __objects"
        return FileStorage.__objects

    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        "serializes __objects to the JSON file (path: __file_path)"
        pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        pass

