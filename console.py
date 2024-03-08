#!/usr/bin/python3


# console.py

import cmd
import json
import sys
from models import storage

class HBNBCommand(cmd.Cmd):
    """Console for HBNB project"""

    prompt = '(hbnb) '
    file_path = "file.json"
    file_storage = storage

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Display help about commands"""
        super().do_help(arg)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def preloop(self):
        """Deserialize the JSON file to __objects before starting the command loop"""
        self.file_storage.reload()

    def postloop(self):
        """Serialize the __objects dictionary to the JSON file before exiting the command loop"""
        self.file_storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()