from ... import lib
from .configurations import configurations


class Atom(lib.Module):

    name = "atom"

    def __init__(self):
        super().__init__(configurations())

    def open(self, configuration):
        return self.run_command(
            "{0} ."
            .format(
                configuration["executable"],
            )
        )
