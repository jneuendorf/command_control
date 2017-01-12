import subprocess

from .. import _globals
from .. import settings


def make_inverse_actions_bidirectional(inverse_actions):
    """Add inverse of all dict tuples to the dict."""
    for key, val in inverse_actions.copy().items():
        inverse_actions[val] = key
    return inverse_actions


class ModuleMeta(type):
    """
    This meta class is used for joining all inherited inverse actions
    and making them bidirectional.
    """

    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        inverse_actions = {}
        for base in reversed(bases):
            for key, val in base.inverse_actions.items():
                inverse_actions[key] = val
        inverse_actions = make_inverse_actions_bidirectional(inverse_actions)
        cls.inverse_actions = inverse_actions


class Module(metaclass=ModuleMeta):
    """
    Super class of all modules.
    Each module has a 'name' and
    a directory of related actions ('inverse_actions').
    These two variables are defined in sub classes.
    Typically in the 'interface' classes.
    """

    name = None
    inverse_actions = {}
    available_settings = []
    default_settings = {}

    def __init__(self, configurations):
        if settings.USED_CONFIGURATION not in configurations:
            raise ValueError(
                "Globally used configuration '{0}' "
                "is not supported by module '{1}'."
                "Configurations defined by module: {2}"
                .format(
                    settings.USED_CONFIGURATION,
                    self.name,
                    configurations,
                )
            )
        self.configurations = configurations

    def supports(self, action):
        return hasattr(self, action) and callable(getattr(self, action))

    def inverse_action(self, action):
        """This method is called when unloading a project."""
        if not self.supports(action):
            raise ValueError(
                "Action '{}' is not supported for module '{}'."
                .format(
                    action,
                    self.name
                )
            )
        return self.inverse_actions.get(action, action)

    def get_setting(self, name):
        """
        This method contains the boilerplate code (exception handling).
        The actual setting retrieval is done in self._find_setting().
        """
        if name in self.available_settings and name in self.default_settings:
            try:
                return self._find_setting(name)
            except Exception as e:
                raise "dunno.............."
        else:
            raise ValueError(
                "Cannot get setting with name '{}'. "
                "Check the class variables 'available_settings' and "
                "'default_settings' of module '{}'"
                .format(
                    name,
                    self.name
                )
            )

    def do(self, action):
        if _globals._dry_run:
            self._print_on_do(action)
        method = getattr(self, action)
        return method(self.configurations[settings.USED_CONFIGURATION])

    def run_command(self, command):
        if _globals._dry_run:
            # print what gets executed behind the pseudo command
            print("({})".format(command))
        else:
            try:
                response = subprocess.run(
                    command,
                    shell=True,
                    check=True,
                    stdout=subprocess.PIPE,
                ).stdout
                exit_status = 0
            except subprocess.CalledProcessError as error:
                exit_status = error.returncode
                response = error.output
            # print("# result................................................")
            # prepend comment char to all lines (except 1st one)
            # output = response.decode("utf-8").replace("\n", "\n# ")
            return {
                "successful": exit_status,
                "message": response.decode("utf-8")
            }

    def _print_on_do(self, action):
        print(
            "{} {}".format(
                action,
                self.name
            ),
            end=" "
        )

    def _find_setting(self, name):
        # we know that `self.default_settings` contains `name`
        return (
            _globals._current_project_settings.get(name) or
            settings.__dict__.get(name) or
            self.default_settings[name]
        )
