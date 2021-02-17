#!/usr/bin/python3
"""
a command interpreter for the AirBnB clone
"""

import cmd
from datetime import datetime
from shlex import split  
import models



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    classes = ["Basemodel"]

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_quit(self, arg):
        return True

    def do_create(self, arg):
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
