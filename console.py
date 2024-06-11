#!/usr/bin/python3
"""
Command interpreter for managing AirBnB objects.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        super().do_help(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
