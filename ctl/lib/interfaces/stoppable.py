class Stoppable():

    def stop(self, configuration):
        raise NotImplementedError(
            "stop() needs to be implemented for module {}"
            .format(self)
        )
