# The used configuration determines what module configuration will be chosen.
# See each module's configurations.py.
USED_CONFIGURATION = "MAC_HOMEBREW"

PROJECT_UNLOAD_DIRECTORY = "~"

projects = {
    "my_web_project": [
        "cd ~/Developer/web/project1",
        "start apache mysql",
    ],
    "another_project": {
        "load": [
            "cd ~/Developer/web/project1",
            "start mysql rails",
            # this action can't be inverted and should not be run on "unload"
            "open atom",
        ],
        "unload": [
            "stop mysql rails"
        ],
        # additional settings for this project only
        # (these override the global settings below)
        "RAILS_DEV_LOG": "log/dev.log"
    }
}

# provide setting for all rails modules
RAILS_DEV_LOG = "log/development.log"
