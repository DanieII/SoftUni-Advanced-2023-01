from booths.open_booth import OpenBooth
from booths.private_booth import PrivateBooth
from delicacies.gingerbread import Gingerbread
from delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        all_names = [x.name for x in self.delicacies]
        if name in all_names:
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            delicacy = Stolen(name, price)
        else:
            Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        all_booths = [x.booth_number for x in self.booths]
        if booth_number in all_booths:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
        else:
            Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            needed_booth = [x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people][0]
        except IndexError:
            Exception(f"No available booth for {number_of_people} people!")

        needed_booth.reserve(number_of_people)
        return f"Booth {needed_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = [x for x in self.booths if x.booth_number == booth_number][0]
        except IndexError:
            return f"Could not find booth {booth_number}!"

        try:
            delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        except IndexError:
            return f"No {delicacy_name} in the pastry shop!"

        booth.deliacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        delicacies = sum(x.price for x in booth.deliacy_orders)

        bill = delicacies + booth.price_for_reservation
        self.income += bill

        booth.deliacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
