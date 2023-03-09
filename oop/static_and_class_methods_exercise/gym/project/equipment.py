from project.id_mixin import IDMixin


class Equipment(IDMixin):
    id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
