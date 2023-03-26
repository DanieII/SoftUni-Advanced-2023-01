from project.supply.supply import Supply


class Drink(Supply):

    def __init__(self, name):
        super().__init__(name, 15)

    @property
    def supply_type(self):
        return self.__class__.__name__
