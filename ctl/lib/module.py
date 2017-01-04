import subprocess

from .. import settings


def make_inverse_actions_bidirectional(inverse_actions):
    """Add inverse of all dict tuples to the dict."""
    # tuples = inverse_actions.copy().items()
    tuples = inverse_actions.items()
    # for tup in inverse_actions.copy().items():
    for tup in tuples:
        inverse_actions[tup[1]] = tup[0]
    return inverse_actions


class ModuleMeta(type):

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

    def __init__(self, configurations, used_configuration):
        if used_configuration.name not in configurations:
            raise ValueError(
                "Globally used configuration '{0}' "
                "is not supported by module '{1}'."
                "Configurations defined by module: {2}"
                .format(
                    used_configuration.name,
                    self.name,
                    configurations,
                )
            )
        self.configurations = configurations
        self.used_configuration = used_configuration

    def supports(self, action):
        return hasattr(self, action) and callable(getattr(self, action))

    def inverse_action(self, action):
        if not self.supports(action):
            raise ValueError(
                "Action '{}' is not supported for module '{}'."
                .format(
                    action,
                    self.name
                )
            )
        return self.inverse_actions.get(action)

    def do(self, action):
        if settings._dry_run:
            print(
                "{} {}".format(
                    action,
                    self.name
                ),
                end=" "
            )
        method = getattr(self, action)
        return method(self.configurations[self.used_configuration.name])

    def run_command(self, command):
        if settings._dry_run:
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
