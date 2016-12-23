#!/usr/bin/env python3

from ctl import modules
import sys


def load_module(module_name):
    if module_name in modules.module_dict:
        return modules.module_dict[module_name]()
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: ctl.py action(s) module(s)")

    action_args = []
    module_args = []
    for arg in sys.argv[1:]:
        module = load_module(arg)
        if module is None:
            if len(module_args) == 0:
                action_args.append(arg)
            else:
                sys.exit(
                    "An action cannot be declared after the first module.\n" +
                    "Got action '{}' ".format(arg) +
                    "after module " +
                    "'{}'".format(module_args[-1].__class__.__name__.lower()) +
                    "."
                )
        else:
            module_args.append(module)

    print(action_args)
    print(module_args)

    # mysql = modules.mysql()
    # mysql = load_module("mysql")
    # print(mysql.configurations)
    # print(mysql.get_tasks())
