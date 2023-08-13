#!/usr/bin/python3
"""
The console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """The Console Class"""
    prompt = '(hbnb)'
    classes = {"BaseModel": BaseModel, "User": User}

    def do_create(self, args):
        """Creates a new instance of BaseModel\n"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = HBNBCommand.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Show command to print the str representation of an instance\n"""

        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, args):
        """Destroy command that delete an instance\n"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(arg[0], arg[1])]

    def do_all(self, args):
        """All command prints a str representation of all instances"""
        my_list = []
        arg = args.split()
        for key in storage.all().values():
            if not arg or arg[0] == key.__class__.__name__:
                my_list.append(key.__str__())
        if my_list:
            print("\n".join(my_list))
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update command updates an instance"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in storage.all().keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg) == 4:
            obj = storage.all()["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
            obj.updated_at = datetime.now()


        elif type(eval(arg[2])) == dict:
            obj = storage.all()["{}.{}".format(arg[0], arg[1])]
            for k, v in eval(arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
                obj.updated_at = datetime.now()
        storage.save()  


    def do_quit(self, args):
        """Quit command to exit the console\n"""
        return (True)

    def do_EOF(self):
        """exit the console"""
        print()
        return (True)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()