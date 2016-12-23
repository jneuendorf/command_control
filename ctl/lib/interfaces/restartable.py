from .startable import Startable
from .stoppable import Stoppable


class Restartable(Startable, Stoppable):

    def restart(self):
        raise NotImplementedError("...")
