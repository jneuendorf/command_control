from .abstract_project import abstract_project # NOQA
from .atom import atom # NOQA
from .git import git # NOQA
from .homebrew import homebrew # NOQA
from .mysql import mysql # NOQA
from .postgres import postgres # NOQA
from .rails import rails # NOQA

# make all modules accessible by name
# key should match module_class.name (this is what the user has to type)
module_dict = {
    "abstract_project": abstract_project,
    "atom": atom,
    "git": git,
    "homebrew": homebrew,
    "mysql": mysql,
    "postgres": postgres,
    "rails": rails,
}
