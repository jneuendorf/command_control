from .module import Module # NOQA
# from .actions import actions # NOQA
from .task import Task # NOQA

# hide interfaces folder from package structure
from .interfaces import Restartable # NOQA


from enum import Enum


class AVAILABLE_CONFIGURATIONS(Enum):
    MAC_HOMEBREW = 1
