class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.meals_with_quantities = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value.startswith("0") and len(value) == 10 and all(x.isdigit() for x in value)):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
