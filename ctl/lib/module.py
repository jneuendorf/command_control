class Module():
    """docstring for Module"""

    # def __init__(self):
    #     self.name = self.__class__.name

    def get_tasks(self):
        raise NotImplementedError("...")

    def supports(self, action):
        return hasattr(self, action) and callable(getattr(self, action))

    def do(self, action):
        return getattr(self, action)()
