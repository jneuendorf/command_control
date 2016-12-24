from .mysql import mysql # NOQA
from .postgres import postgres # NOQA

# make all modules accessible by name
module_dict = {
    "mysql": mysql,
    "postgres": postgres,
}
