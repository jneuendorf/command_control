from .module import Module # NOQA

# hide interfaces folder from package structure
from .interfaces import Loadable # NOQA
from .interfaces import Restartable # NOQA


# USED PACKAGES
from .. import _globals
from .. import modules
from .. import settings


# HELPER FUNCTIONS IN CTL.PY
def parse_args(args):
    action_args = []
    module_args = []
    for i, arg in enumerate(args):
        module = None
        # try loading the according module
        if hasattr(modules, arg):
            module = getattr(modules, arg)()
        # try (un)loading the according project
        if arg in settings.projects:
            # arg is also the name of module
            if module is not None:
                raise ValueError(
                    "Argument with name '{}' is the name of a module "
                    "as well as of a project. "
                    "Make sure there is no name ambiguity."
                )
            module = modules.abstract_project(arg)
        # special case: cd /path/to/go/to
        # this is often the case when loading a project
        if arg.lower() == "cd":
            if i != 0 or len(args) != 2:
                raise ValueError(
                    "Action 'cd' must be the very first argument "
                    "and must be following by exactly one location."
                )
            return ("cd", args[i + 1])

        # arg is neither a module nor a project
        # => interpret arg as action
        if module is None:
            if len(module_args) == 0:
                action_args.append(arg)
            else:
                raise ValueError(
                    "An action cannot be declared after the first module.\n" +
                    "Got action '{}' ".format(arg) +
                    "after module " +
                    "'{}'".format(module_args[-1].name) +
                    "."
                )
        else:
            module_args.append(module)

    # only actions given
    if len(module_args) == 0:
        raise ValueError(
            "No modules specified. "
            "Maybe there is a typo in a module..."
        )

    for module in module_args:
        for action in action_args:
            if not module.supports(action):
                raise ValueError(
                    "Module '{0}' does not support action '{1}'."
                    .format(
                        module.name,
                        action
                    )
                )
    return (action_args, module_args)
