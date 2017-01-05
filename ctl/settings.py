from enum import Enum as __enum__

# 'global' accessible variables that are set in main.py
_is_sourced = None
_dry_run = None


class AVAILABLE_CONFIGURATIONS(__enum__):
#### !!CUSTOMIZATION STARTS HERE!! #### NOQA
    MAC_HOMEBREW = 1


# The used configuration determines what configuration will be chosen.
# See the configurations.py file of a module.
used_configuration = AVAILABLE_CONFIGURATIONS.MAC_HOMEBREW
unload_directory = "~"

# map project name to list of commands to be executed
projects = {
    "amc": [
        "cd ~/Developer/rails/amc",
        "start mysql postgres",
    ],
}
