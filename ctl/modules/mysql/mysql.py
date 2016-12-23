from ... import lib
from .configurations import configurations


class MySql(lib.Module, lib.Restartable):
    """docstring for MySql"""

    name = "mysql"

    def __init__(self, used_configuration):
        super().__init__(configurations(), used_configuration)

    def exec_action(self, configuration, action):
        return self.run_command(
            "{0} {1}"
            .format(
                configuration["executable"],
                action
            )
        )

    def start(self, configuration):
        return self.exec_action(configuration, "start")

    def stop(self, configuration):
        return self.exec_action(configuration, "stop")

    def restart(self, configuration):
        return self.exec_action(configuration, "restart")
