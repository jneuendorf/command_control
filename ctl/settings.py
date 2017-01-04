from enum import Enum as __enum__

# 'global' accessible variables that are set in main.py
_is_sourced = None
_dry_run = None


class AVAILABLE_CONFIGURATIONS(__enum__):
    MAC_HOMEBREW = 1


used_configuration = AVAILABLE_CONFIGURATIONS.MAC_HOMEBREW

# map project name to list of commands to be executed
projects = {
    "amc": [
        "cd ~/Developer/rails/amc",
        "start mysql postgres",
    ],
}
