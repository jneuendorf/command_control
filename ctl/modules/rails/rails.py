from ... import lib
from ... import settings
from .configurations import configurations


class Rails(lib.Module, lib.Restartable):

    name = "rails"
    available_settings = [
        "RAILS_DEV_LOG"
    ]
    default_settings = {
        "RAILS_DEV_LOG": "log/development.log"
    }

    def __init__(self):
        super().__init__(configurations())

    def start(self, configuration):
        print(
            "starting rails....RAILS_DEV_LOG = {}"
            .format(self.get_setting("RAILS_DEV_LOG"))
        )
        return self.run_command(
            "{0} server"
            .format(configuration["executable"])
        )

    def stop(self, configuration):
        self.run_command("kill -9 `cat tmp/pids/server.pid`")
        return self.run_command("rm tmp/pids/server.pid")

    # def log(self, configuration):
    #     # TODO: how to stream output (sometimes)?
    #     return self.run_command("tail -f log/development.log | grep --line-buffered --ignore-case $pattern --before-context=$before --after-context=$after")
