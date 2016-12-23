from .startable import Startable
from .stoppable import Stoppable


class Restartable(Startable, Stoppable):

    def restart(self, configuration):
        raise NotImplementedError(
            "restart() needs to be implemented for module {}"
            .format(self)
        )
