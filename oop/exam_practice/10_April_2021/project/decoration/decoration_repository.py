from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if type(decoration) == decoration_type:
                return decoration
        return None
