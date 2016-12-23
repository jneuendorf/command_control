from ... import lib
from .configurations import configurations


class MySql(lib.Module, lib.Restartable):
    """docstring for MySql"""

    name = "mysql"

    # must not take any arguments
    def __init__(self):
        super().__init__()
        self.configurations = configurations()

    def get_tasks(self):
        return []

    def start(self):
        print("starting mysql...")
