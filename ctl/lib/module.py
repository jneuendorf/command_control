import subprocess


class Module():
    """docstring for Module"""

    def __init__(self, configurations, used_configuration):
        if used_configuration.name in configurations:
            self.configurations = configurations
            self.used_configuration = used_configuration.name
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

    def get_tasks(self):
        raise NotImplementedError("...")

    def supports(self, action):
        return hasattr(self, action) and callable(getattr(self, action))

    def do(self, action):
        method = getattr(self, action)
        return method(self.configurations[self.used_configuration])

    def run_command(self, command):
        print(command)
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
        print(response.decode("utf-8"))
        return {
            "successful": exit_status,
            "message": response.decode("utf-8")
        }
