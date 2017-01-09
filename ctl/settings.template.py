# The used configuration determines what module configuration will be chosen.
# See the configurations.py file of a module.
USED_CONFIGURATION = "MAC_HOMEBREW"

PROJECT_UNLOAD_DIRECTORY = "~"

# map project name to list of commands to be executed
projects = {
    "my_web_project": [
        "cd ~/Developer/web/project1",
        "start apache mysql",
    ],
    "another_project": {
        "load": [
            "cd ~/Developer/web/project1",
            "start mysql",
            # this action can't be inverted and should not be run on "unload"
            "open atom",
        ],
        "unload": [
            "stop mysql"
        ],
    }
}
