from enum import Enum as __enum__

# 'global' accessible variables that are set in main.py
_is_sourced = None
_dry_run = None


class AVAILABLE_CONFIGURATIONS(__enum__):
    MAC_HOMEBREW = 1


used_configuration = AVAILABLE_CONFIGURATIONS.MAC_HOMEBREW

projects = {
    # "amc": {
    #     "location": "~/Developer/rails/amc",
    #     "commands": [
    #         "start mysql postgres",
    #         # multiple items possible to avoid potential
    #         # incompatible actions and modules:
    #         # e.g.  action1 module1 + action2 module2
    #         #       ~> if module2 does not support action1
    #         #           this cannot be written as
    #         #           'action1 action2 module1 module2'
    #         # "init something_else",
    #     ]
    # },
    "amc": [
        "cd ~/Developer/rails/amc",
        "start mysql postgres",
    ],
}
