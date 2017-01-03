# command_control

Tool with simple command line usage for running similar tasks e.g. starting MySQL, stopping postgres etc.
There are actions (e.g. start, stop) and modules (e.g. mysql, postgres).
Also there are global configurations which can influence the implementation of a module's action
(e.g. the apache installed with homebrew might be started differently than the one bundled in XAMPP).


## Prerequisites

- python3.6+
- `ctl.sh` made executable (e.g. with `chmod +x ctl.sh`)


## Configuration

All configurations for your local machine are set in `ctl/settings.py`.
In the settings file the globally used configuration must be set.
The default is `ctl.lib.AVAILABLE_CONFIGURATIONS.MAC_HOMEBREW`.
Additionally projects can be defined.

#### Projects

Projects combine a location with actions and modules.
When loading a project a associated modules are started and you will be taken to the project's location.
Thus, projects are shortcuts for otherwise multiple calls of `ctl.sh` and make it very convenient to load your working environment.

Projects have 3 actions: `load`, `unload` and `cd`.
For example, it would be as easy as

`ctl.sh load my_rails_project`

to get a rails app started (maybe including `postgres` and `mongodb`) and change to the according directory.

When done working `unload` will stop everything needed for the project and take you to your home directory.


## Usage samples

```bash
ctl.sh start mysql
ctl.sh stop mysql
ctl.sh restart mysql
# start 2 modules
ctl.sh start mysql postgres
ctl.sh load project
ctl.sh unload project
ctl.sh cd predefined_location
```

### Note

The `cd` action is special and only takes parameter (the path to go to).
Thus, no other modules can define that action.
Also that implies that there must be exactly 2 parameters for the entire call (1 action + 1 parameter).
