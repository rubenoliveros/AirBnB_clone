#!/usr/bin/python3
""" Module for Console """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):

    __dict_class = {"BaseModel": BaseModel, "User": User,
                    "City": City, "State": State, "Place": Place,
                    "Amenity": Amenity, "Review": Review}

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """Creates a new instance of the class
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return
            instance = HBNBCommand.__dict_class[line_tokenized[0]]()
            storage.save()
            print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    print(dictionary[key])
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    del(dictionary[key])
                    storage.save()
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name
        """
        line_tokenized = HBNBCommand.do_manage(line)
        if line_tokenized:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

        dictionary = storage.all()
        list_objects = []
        for key, value in dictionary.items():
            if len(line_tokenized) >= 1:
                token = key
                token = str(token).split(".")
                if token[0] == line_tokenized[0]:
                    list_objects.append(str(dictionary[key]))
            else:
                list_objects.append(str(dictionary[key]))
        print(list_objects)

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        """
        line_tokenized = HBNBCommand.do_manage(line)

        if line:
            if not line_tokenized[0] in HBNBCommand.__dict_class:
                print("** class doesn't exist **")
                return

            if len(line_tokenized) >= 2 and line_tokenized[1]:
                key = line_tokenized[0]+"."+line_tokenized[1]
                dictionary = storage.all()
                try:
                    dictionary[key]
                except BaseException:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return

            if not len(line_tokenized) >= 3:
                print("** attribute name missing **")
                return

            if not len(line_tokenized) >= 4:
                print("** value missing **")
                return
            instance = dictionary[key].__dict__
            instance[line_tokenized[2]] = line_tokenized[3]
            dictionary.get(key).save()
        else:
            print("** class name missing **")

    def do_manage(line):
        """splits the line arguments splits and return an array
        """
        tokens = shlex.split(line)
        return list(tokens)

    def default(self, line):
        """this function print or execute an action if the control is true
        """
        line_token = line.split(".")
        if len(line_token) >= 2 and line_token[0] in HBNBCommand.__dict_class:
            if line_token[1] == "all()":
                HBNBCommand.do_all(self, line_token[0])
            # count the class
            if line_token[1] == "count()":
                HBNBCommand.do_counter(self, line_token[0])
        if line_token[1][0] == "s":
            tmp = line_token[1]
            comand = tmp[0:4]
            star = tmp.index("\"")
            end = tmp.index(")")
            cls_id = tmp[(star + 1):(end - 1)]
            if comand == "show":
                key = line_token[0]+" " + cls_id
                HBNBCommand.do_show(self, key)
        if line_token[1][0] == "d":
            tmp = line_token[1]
            comand = tmp[0:7]
            star = tmp.index("\"")
            end = tmp.index(")")
            cls_id = tmp[(star + 1):(end - 1)]
            if comand == "destroy":
                key = line_token[0]+" " + cls_id
                HBNBCommand.do_destroy(self, key)

        if line_token[1][0] == "u":
            tmp = line_token[1]
            comand = tmp[0:6]
            star = tmp.index("\"")
            end = tmp.index(")")
            input_update = tmp[star:end]
            input_update = input_update.split(",")
            cls_id = input_update[0][1:-1]
            name_atr = input_update[1][1:]
            value_atr = input_update[2][1:]
            key = line_token[0]+" "+cls_id+" "+name_atr+" "+value_atr
            HBNBCommand.do_update(self, key)

    def do_counter(self, line):
        """ Counter of class
        """
        dictionary = storage.all()
        count = 0
        tmp_key = ""
        for key, value in dictionary.items():
            tmp_key = key.split(".")
            if tmp_key[0] == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
