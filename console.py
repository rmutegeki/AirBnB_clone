#!/usr/bin/python3
"""
This is a program that contains the entry point
of the command interpreter.
Functions and Classes:
    class HBNBCommand(cmd.Cmd):
"""


import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of command interpreter"""

    prompt = "(hbnb) "

    classes = {'User': {'email': str, 'password': str, 'first_name': str,
                        'last_name': str},
               'City': {'state_id': str, 'name': str},
               'Amenity': {'name': str},
               'State': {'name': str},
               'Review': {'place_id': str, 'user_id': str, 'text': str},
               'Place': {'city_id': str, 'user_id': str, 'name': str,
                         'description': str, 'number_rooms': int,
                         'number_bathrooms': int, 'max_guest': int,
                         'price_by_night': int, 'latitude': float,
                         'longitude': float, 'amenity_ids': eval},
               'BaseModel': {'id': str, 'created_at': datetime,
                             'updated_at': datetime}}

    def do_EOF(self, line):
        """Exits the program with ^D
        """

        print("")
        return True

    def do_quit(self, line):
        """Exits the program with quit command
        """

        return True

    def emptyline(self):
        """Do nothing with empty line
        """

        pass

    def do_create(self, line):
        """creates new instance of a class
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'Amenity': Amenity, 'Review': Review,
                   'City': City}

        if line == "":
            print("** class name missing **")
        elif line in classes.keys():
            obj = classes[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class name doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] in self.classes.keys():
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                key = '.'.join(args)
                objects = storage.all()
                if key in objects.keys():
                    print(objects[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] in self.classes.keys():
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                key = '.'.join(args)
                objects = storage.all()
                if key in objects.keys():
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """

        args = line.split()

        condition_1 = line == ""
        condition_2 = (len(args) == 1) and (args[0] in self.classes.keys())
        if condition_1 or condition_2:
            objects = storage.all()
            obj_list = []
            for k in objects.keys():
                if len(args) == 1:
                    if args[0] in k:
                        obj_list.append(str(objects[k]))
                else:
                    obj_list.append(str(objects[k]))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = ".".join(args[0:2])
            if key in objects.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    my_obj = objects[key]

                    # Find attribute type
                    cls = args[0]
                    attr = args[2]
                    cast_to_type = self.classes[cls][attr]

                    value = get_value(args[3:])
                    setattr(my_obj, args[2], cast_to_type(value))
                    storage.save()
            else:
                print("** no instance found **")


def get_value(args):
    """ gets attribute's value passed inside double quotes """

    if args:
        if args[0].startswith('"'):
            tmp = ' '.join(args)
            my_l = tmp.split('"')
            for i in my_l:
                if i != "":
                    return i
        else:
            return args[0]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
