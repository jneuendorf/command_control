from ... import lib
from .configurations import configurations


class Git(lib.Module):

    name = "git"

    def __init__(self):
        super().__init__(configurations())

    def _exec_action(self, configuration, action):
        return self.run_command(
            "{0} {1}"
            .format(
                configuration["executable"],
                action
            )
        )

    def fetch(self, configuration):
        return self._exec_action(configuration, "fetch")

    def pull(self, configuration):
        return self._exec_action(configuration, "pull")

    def push(self, configuration):
        return self._exec_action(configuration, "push")
