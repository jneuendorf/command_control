from ... import lib
from .configurations import configurations


class MySql(lib.Module, lib.Restartable):
    """docstring for MySql"""

    name = "mysql"

    def __init__(self):
        super().__init__(configurations())

    # Usage: mysql.server {start|stop|restart|reload|force-reload|status}
    def _exec_action(self, configuration, action):
        return self.run_command(
            "{0} {1}"
            .format(
                configuration["executable"],
                action
            )
        )

    def start(self, configuration):
        return self._exec_action(configuration, "start")

    def stop(self, configuration):
        return self._exec_action(configuration, "stop")

    def restart(self, configuration):
        return self._exec_action(configuration, "restart")
