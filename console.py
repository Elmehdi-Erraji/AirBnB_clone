#!/usr/bin/python3
"""
The console
"""
import cmd
from models import storage
from models.base_model import BaseModel
import re


class HBNBCommand(cmd.Cmd):
    """The Console Class"""
    prompt = '(hbnb)'

    def do_create(self, args):
        """Creates a new instance of BaseModel\n"""
        if not args:
            print("** class name missing **")
            return

        classes = {"BaseModel": BaseModel}
        class_name = args.split()[0]
        if class_name not in classes:
            print("** class doesn't exist ** (ex: $ create MyModel)")
            return

        instance = classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Show command to print the str representation of an instance\n"""

        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in ["BaseModel"]:
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
        elif arg[0] not in ["BaseModel"]:
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
            if len(arg) == 0:
                my_list.append(key.__str__())
            elif len(arg) > 0:
                if arg[0] == key.__class__.__name__:
                    my_list.append(key.__str__())
                else:
                    print("** class doesn't exist **")
                    return
        print(my_list)

     
    def do_update(self, args):
        """Updates an instance based on the class\
        name and id by adding or updating attribute.
        """
        if args == "" or args is None:
            print("** class name missing **")
            return

        rex = '^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, args)
        if not match:
            print("** class name missing **")
        elif match.group(1) not in storage.classes():
            print("** class doesn't exist **")
        elif match.group(2) is None:
            print("** instance id missing **")
        elif match.group(3) is None:
            print("** attribute name missing **")
        elif match.group(4) is None:
            print("** value missing **")
        else:
            value = match.group(4).replace('"', '')
            key = "{}.{}".format(match.group(1), match.group(2))
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[match.group(1)]
                if match.group(3) in attributes:
                    value = attributes[match.group(3)](value)
                setattr(storage.all()[key], match.group(3), value)
                storage.all()[key].save()

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