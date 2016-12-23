# command_control
Tool with simple command line usage for running similar task e.g. starting MySQL, stopping postgres etc.
There are actions (e.g. start, stop) and targets (e.g. mysql, postgres).
A task is an action combined with a target.
A module bundles multiple tasks (for 1 target).

## Usage samples

```bash
ctl start mysql
ctl stop mysql
ctl restart mysql
ctl load project
ctl unload project
ctl cd predefined_location
```
