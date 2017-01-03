import subprocess

from .. import settings


class Module():
    """docstring for Module"""

    name = None

    def __init__(self, configurations, used_configuration):
        if used_configuration.name in configurations:
            self.configurations = configurations
            self.used_configuration = used_configuration
        else:
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

    def supports(self, action):
        return hasattr(self, action) and callable(getattr(self, action))

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
