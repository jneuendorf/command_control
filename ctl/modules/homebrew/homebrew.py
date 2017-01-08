from ... import lib
from .configurations import configurations


class Homebrew(lib.Module):

    name = "homebrew"

    def __init__(self):
        super().__init__(configurations())

    def update_only(self, configuration):
        return self.run_command(
            "{0} update"
            .format(
                configuration["executable"],
            )
        )

    def upgrade_only(self, configuration):
        return self.run_command(
            "{0} upgrade"
            .format(
                configuration["executable"],
            )
        )

    def cleanup_only(self, configuration):
        return self.run_command(
            "{0} cleanup"
            .format(
                configuration["executable"],
            )
        )

    def update(self, configuration):
        self.update_only(configuration)
        self.upgrade_only(configuration)
        self.cleanup_only(configuration)
