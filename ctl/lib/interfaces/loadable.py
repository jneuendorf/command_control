class Loadable():

    def load(self, configuration):
        raise NotImplementedError(
            "load() needs to be implemented for module {}"
            .format(self)
        )

    def unload(self, configuration):
        raise NotImplementedError(
            "unload() needs to be implemented for module {}"
            .format(self)
        )
