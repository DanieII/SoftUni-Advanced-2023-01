from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    @property
    def price_per_person(self):
        return self.PRICE_PER_PERSON
