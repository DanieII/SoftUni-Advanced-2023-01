from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    @property
    def price_per_person(self):
        return self.PRICE_PER_PERSON
