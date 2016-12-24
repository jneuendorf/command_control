from ... import lib
from .configurations import configurations


class Postgres(lib.Module, lib.Restartable):
    """docstring for Postgres"""

    name = "postgres"

    def __init__(self, used_configuration):
        super().__init__(configurations(), used_configuration)

    # Usage: pg_ctl start -D $POSTGRES_PATH
    def exec_action(self, configuration, action):
        return self.run_command(
            "{0} {1} -D {2}"
            .format(
                configuration["executable"],
                action,
                configuration["postgres_path"]
            )
        )

    def start(self, configuration):
        return self.exec_action(configuration, "start")

    def stop(self, configuration):
        return self.exec_action(configuration, "stop")

    def restart(self, configuration):
        return self.exec_action(configuration, "restart")
