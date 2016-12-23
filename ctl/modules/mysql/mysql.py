from ... import lib
from .configurations import configurations


class MySql(lib.Module, lib.Restartable):
    """docstring for MySql"""

    # must not take any arguments
    def __init__(self):
        super().__init__()
        self.configurations = configurations()

    def get_tasks(self):
        return []

    def supports(self, action):
        return action in [
            "start",
            "stop",
            "restart",
            # "status",
        ]
