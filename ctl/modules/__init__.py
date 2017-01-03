from .abstract_project import abstract_project # NOQA
from .mysql import mysql # NOQA
from .postgres import postgres # NOQA

# make all modules accessible by name
module_dict = {
    "abstract_project": abstract_project,
    "mysql": mysql,
    "postgres": postgres,
}
