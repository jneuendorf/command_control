# command_control

Tool with simple command line usage for running similar tasks e.g. starting MySQL, stopping postgres etc.
There are actions (e.g. start, stop) and modules (e.g. mysql, postgres).
Also there are global configurations which can influence the implementation of a module's action
(e.g. the apache installed with homebrew might be started differently than the one bundled in XAMPP).


## Prerequisites

- python3.6+
- `ctl.sh` made executable (e.g. with `chmod +x ctl.sh`)
  - optionally, it can of course be renamed to just `ctl`


## Configuration

All configurations for your local machine are set in `ctl/settings.py`.
In the settings file the globally used configuration must be set.
Additionally projects can be defined.

The following variables must be defined:

- `USED_CONFIGURATION (str)`
- `PROJECT_UNLOAD_DIRECTORY (str)`
- `projects (dict of list of str, dict of dict of list of str)`

An example can be seen in `ctl/settings.template.py`:

```python
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
            "start mysql",
            # this action can't be inverted and should not be run on "unload"
            # thus it does not appear in "unload"
            "open atom",
        ],
        "unload": [
            "stop mysql"
        ],
    }
}

```

#### Modules

A module implements actions for usually one binary.
One example would be mysql that can be started, stopped and restarted.
Each module has a set of configurations.
The used configuration is determined by the `USED_CONFIGURATION` variable (from the settings).


#### Projects

Projects are groups of multiple commands that would otherwise be multiple calls of `ctl.sh`.
That makes it very convenient to load your working environment.

Projects have 2 actions: `load` and `unload`.
For example, it would be as easy as

`ctl.sh load my_rails_project`

to get a rails app started (maybe including `postgres` and `mongodb`) and change to the according directory.

When done working `unload` will stop everything needed for the project and take you to the `PROJECT_UNLOAD_DIRECTORY` directory (defined in the settings).


## Usage samples

```bash
ctl.sh start mysql
ctl.sh stop mysql
ctl.sh restart mysql
# start 2 modules
ctl.sh start mysql postgres
# load project (multiple actions)
ctl.sh load project
ctl.sh unload project
```
