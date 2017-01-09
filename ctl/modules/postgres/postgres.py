from ... import lib
from .configurations import configurations


class Postgres(lib.Module, lib.Restartable):
    """docstring for Postgres"""

    name = "postgres"

    def __init__(self):
        super().__init__(configurations())

    # Usage: pg_ctl start -D $POSTGRES_PATH
    def _exec_action(self, configuration, action):
        return self.run_command(
            "{0} {1} -D {2}"
            .format(
                configuration["executable"],
                action,
                configuration["postgres_path"]
            )
        )

    def start(self, configuration):
        return self._exec_action(configuration, "start")

    def stop(self, configuration):
        return self._exec_action(configuration, "stop")

    def restart(self, configuration):
        return self._exec_action(configuration, "restart")
