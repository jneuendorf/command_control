from ... import lib
from .configurations import configurations


class Rails(lib.Module, lib.Restartable):

    name = "rails"

    def __init__(self):
        super().__init__(configurations())

    def start(self, configuration):
        return self.run_command(
            "{0} server"
            .format(configuration["executable"])
        )

    def stop(self, configuration):
        self.run_command("kill -9 `cat tmp/pids/server.pid`")
        return self.run_command("rm tmp/pids/server.pid")

    # def log(self, configuration):
    #     # TODO: 1. how to stream output (sometimes)?
    #     # TODO: 2. how to provide project (or project kind) related options (e.g. location of 'development.log')
    #     return self.run_command("tail -f log/development.log | grep --line-buffered --ignore-case $pattern --before-context=$before --after-context=$after")
