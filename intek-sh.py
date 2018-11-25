#!/usr/bin/env python3
import os
import subprocess


def cd():
    if len(command) == 1:
        try:
            os.chdir(os.environ["HOME"])
        except KeyError:
            print("intek-sh: cd: HOME not set")
    else:
        try:
            os.chdir(os.path.abspath(command[1]))
        except FileNotFoundError:
            print("intek-sh: cd: " + command[1] + ": \
                  No such file or directory")


def printenv():
    if len(command) == 1:
        for key in os.environ.keys():
            print(key + "=" + os.environ[key])
    else:
        if command[1] in os.environ.keys():
            print(os.environ[command[1]])
        else:
            return


def export():
    if len(command) == 1:
        return
    else:
        variables = command[1:]
        for variable in variables:
            if "=" not in variable:
                os.environ[variable] = ""
            else:
                variable = variable.split("=")
                os.environ[variable[0]] = variable[1]


def unset():
    if len(command) == 1:
        return
    else:
        variables = command[1:]
        for variable in variables:
            if variable in os.environ.keys():
                del os.environ[variable]
            else:
                return


def my_exit():
    if len(command) == 1:
        print("exit")
    elif command[1] in "1234567890":
        print("exit")
    else:
        print("exit\nintek-sh: exit:")


def run_file():
    if "./" in command[0]:
        try:
            subprocess.run(command[0])
        except PermissionError:
            print("intek-sh: " + command[0] + ": Permission denied")
        except FileNotFoundError:
            print("intek-sh: " + command[0] + ": No such file or directory")
    else:
        flag = False
        try:
            PATH = os.environ["PATH"].split(":")
        except KeyError:
            print("intek-sh: " + command[0] + ": command not found")
            return
        for item in PATH:
            if os.path.exists(item + "/" + command[0]):
                subprocess.run([item + "/" + command[0]] + command[1:])
                flag = True
                break
        if flag is not True:
            print("intek-sh: " + command[0] + ": command not found")


if __name__ == '__main__':
    global command
    command = None
    try:
        while command != "exit":
            command = input("intek-sh$ ").split(" ")
            #  to remove '', '', '', ''... in command
            lst = []
            for item in command:
                if item != "":
                    lst.append(item)
            command = lst
            if len(command) == 0:
                pass
            elif command[0] == "cd":
                cd()
            elif command[0] == "printenv":
                printenv()
            elif command[0] == "export":
                export()
            elif command[0] == "unset":
                unset()
            elif command[0] == "exit":
                my_exit()
                exit()
            else:
                run_file()
    except EOFError:
        pass
