#!/usr/bin/python3


# console.py

import cmd
import json
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Console for HBNB project"""

    prompt = '(hbnb) '
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Review", "Place"}
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

    def do_create(self, class_name):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        If the class name is missing, print ** class name missing **
        If the class name doesn't exist, print ** class doesn't exist **
        """
        if not class_name:
            print("** class name missing **")
            return

        try:
            class_ = eval(class_name)
            if not issubclass(class_, BaseModel):
                print("** class doesn't exist **")
                return
            new_instance = class_()
            self.file_storage.new(new_instance)
            self.file_storage.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")
            print(e)


    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        args = args.split()
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
            return

        try:
            class_name, id_ = args.split()
            class_ = eval(class_name)
            if not issubclass(class_, BaseModel):
                print("** class doesn't exist **")
                return
            if not id_:
                print("** instance id missing **")
                return
            key = f"{class_.__name__}.{id_}"
            if key not in self.file_storage.__objects:
                print("** no instance found **")
                return
            del self.file_storage.__objects[key]
            self.file_storage.save()
        except Exception as e:
            print("** class doesn't exist **")
            print(e)

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        objects = storage.all()
        list = []
        if not args:
            for name in objects.keys():
                obj = objects[name]
                list.append(str(obj))
            print(list)
            return
        args = args.split(" ")
        if args[0] in self.classes:
            for name in objects:
                if name[0:len(args[0])] == args[0]:
                    obj = objects[name]
                list.append(str(obj))
            print(list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = args.split()
        objects = storage.all()
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(args[0], args[1])
            if k in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                if len(args) < 4:
                    print("** value missing **")
                else:
                    obj = objects[k]
                    setattr(obj, args[2], args[3])
            else:
                print("** no instance found **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()