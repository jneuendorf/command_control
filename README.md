# command_control
Tool with simple command line usage for running similar task e.g. starting MySQL, stopping postgres etc.
There are actions (e.g. start, stop) and modules (e.g. mysql, postgres).
Also there are global configurations which can influence the implementation of a module's action
(e.g. the apache installed with homebrew might be started differently than the one bundled in XAMPP).

## Usage samples

```bash
ctl start mysql
ctl stop mysql
ctl restart mysql
ctl load project
ctl unload project
ctl cd predefined_location
```
