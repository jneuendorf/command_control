class Startable():

    def start(self, configuration):
        raise NotImplementedError(
            "start() needs to be implemented for module {}"
            .format(self)
        )
