import os

from ... import lib
from ... import settings
from .configurations import configurations


class AbstractProject(lib.Module, lib.Loadable):
    """docstring for AbstractProject"""

    name = "abstract_project"

    def __init__(self, name, commands, used_configuration):
        super().__init__(configurations(), used_configuration)
        self.name = name
        self.commands = commands

    # # @Override
    # def do(self, action):
    #     if settings._dry_run:
    #         print("go to project location", end=" ")
    #     method = getattr(self, action)
    #     return method(self.configurations[self.used_configuration.name])

    def load(self, configuration):
        """
        When loading a project multiple `cd` actions are possible.
        The intermediate directories that may be visited are not
        visible to the user.
        Therefore, only the last `cd` will be printed so the calling script
        can change the directory using `source cd`.
        """
        last_cd_command_idx = None
        parsed_commands = []
        for i, command in enumerate(self.commands):
            parsed_command = lib.parse_args(
                command.split(),
                self.used_configuration,
                settings.projects
            )
            parsed_commands.append(parsed_command)
            actions, modules = parsed_command
            if "cd" in actions:
                last_cd_command_idx = i

        for i, parsed_command in enumerate(parsed_commands):
            actions, modules = parsed_command
            if i != last_cd_command_idx:
                # execute actions normally
                if actions != "cd":
                    for action in actions:
                        for module in modules:
                            module.do(action)
                # special action: cd -> modules == path
                else:
                    self.cd(configuration, modules)
            # last of the "cd" actions -> print for wrapper bash script's eval
            else:
                if not settings._is_sourced:
                    print(
                        "\n# WARNING:\n"
                        "#  Tried changing the directory "
                        "while loading a project.\n"
                        "#  This script should be called like "
                        "`source ctl.sh load {}`.\n".format(self.name)
                    )
                self.cd(configuration, modules)

    # same as load but without special last `cd` command
    # commands are executed in reversed order
    def unload(self, configuration):
        parsed_commands = []
        for command in reversed(self.commands):
            parsed_commands.append(lib.parse_args(
                command.split(),
                self.used_configuration,
                settings.projects
            ))

        for parsed_command in parsed_commands:
            actions, modules = parsed_command
            # execute actions normally
            if actions != "cd":
                for action in actions:
                    for module in modules:
                        module.do(
                            module.inverse_action(action)
                            if module.inverse_action(action)
                            else action
                        )
            # special action: cd -> modules == path
            else:
                self.cd(configuration, modules)

        self.cd(configuration, "~")

    def cd(self, configuration, path):
        if settings._dry_run:
            print("(cd {})".format(path))
        elif settings._is_sourced:
            print("cd {}".format(path))
        path = os.path.expanduser(path)
        os.chdir(path)
