#!/usr/bin/env python3

from ctl import modules
from ctl.lib import AVAILABLE_CONFIGURATIONS
import sys


used_configuration = AVAILABLE_CONFIGURATIONS.MAC_HOMEBREW


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: ctl.py action(s) module(s)")

    action_args = []
    module_args = []
    for arg in sys.argv[1:]:
        module = None
        # try loading the according module
        # => if it doesn't exist interpret arg as action
        if arg in modules.module_dict:
            module = modules.module_dict[arg](used_configuration)

        if module is None:
            if len(module_args) == 0:
                action_args.append(arg)
            else:
                sys.exit(
                    "An action cannot be declared after the first module.\n" +
                    "Got action '{}' ".format(arg) +
                    "after module " +
                    "'{}'".format(module_args[-1].name) +
                    "."
                )
        else:
            module_args.append(module)

    # ERROR HANDLING

    # only actions given
    if len(module_args) == 0:
        sys.exit("No modules specified. Maybe there is a typo in a module...")

    for module in module_args:
        for action in action_args:
            if not module.supports(action):
                sys.exit(
                    "Module '{0}' does not support action '{1}'."
                    .format(
                        module.name,
                        action
                    )
                )

    # EXECUTING ACTIONS

    # print(action_args)
    # print(module_args)

    for action in action_args:
        for module in module_args:
            module.do(action)
