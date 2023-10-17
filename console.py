#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    def do_quit(self, arg):
        """ Exit method for quit typing """
        sys.exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        sys.exit()

    def emptyline(self):
        """ Method to pass when an empty line is entered """
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if not arg:
            print('** class name missing **')
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new = self.classes[arg]()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """ Method to print an instance """
        if not arg:
            print('** class name missing **')
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        obj_dict = storage.all()
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """ Method to delete an instance with class and id """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        obj_dict = storage.all()
        if key in obj_dict:
            obj_dict.pop(key)
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """ Method to print all instances """
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in obj_dict.items() if arg in key])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg_list = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        obj_dict = storage.all()
        if key not in obj_dict:
            print('** no instance found **')
            return
        if len(arg_list) < 3:
            print('** attribute name missing **')
            return
        if len(arg_list) < 4:
            print('** value missing **')
            return
        setattr(obj_dict[key], arg_list[2], arg_list[3][1:-1])
        obj_dict[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()