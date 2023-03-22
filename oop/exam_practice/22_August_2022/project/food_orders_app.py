from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def check_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def find_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    @property
    def available_meals(self):
        return Starter, MainDish, Dessert

    def register_client(self, client_phone_number: str):
        if self.find_object_from_attribute("phone_number", client_phone_number, self.clients_list):
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *args):
        for meal in args:
            for v in self.available_meals:
                if isinstance(meal, v):
                    self.menu.append(meal)
                    break

    def show_menu(self):
        self.check_menu()

        menu = []
        for meal in self.menu:
            menu.append(meal.details())

        return "\n".join(menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = self.find_object_from_attribute("phone_number", client_phone_number, self.clients_list)

        self.check_menu()

        if not client:
            self.register_client(client_phone_number)
            client = self.find_object_from_attribute("phone_number", client_phone_number, self.clients_list)

        ordered_meals = {}
        bill = 0
        for name, quantity in meal_names_and_quantities.items():
            meal = self.find_object_from_attribute("name", name, self.menu)

            if not meal:
                raise Exception(f"{name} is not on the menu!")

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

            ordered_meals[meal] = quantity
            bill += quantity * meal.price

        for ordered, ordered_quantity in ordered_meals.items():
            self.menu[self.menu.index(ordered)].quantity -= ordered_quantity

            if not self.find_object_from_attribute("name", ordered.name, client.shopping_cart):
                client.shopping_cart.append(ordered)

            for index in range(len(client.meals_with_quantities)):
                order = client.meals_with_quantities[index][0]
                if order == ordered:
                    client.meals_with_quantities[index][1] += ordered_quantity
                    break
            else:
                client.meals_with_quantities.append([ordered, ordered_quantity])

        client.bill += bill

        meal_names = ", ".join([x.name for x in client.shopping_cart])
        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_object_from_attribute("phone_number", client_phone_number, self.clients_list)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for info in client.meals_with_quantities:
            meal, quantity = info
            self.menu[self.menu.index(meal)].quantity += quantity

        client.shopping_cart.clear()
        client.meals_with_quantities.clear()
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.find_object_from_attribute("phone_number", client_phone_number, self.clients_list)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        receipt = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."
        self.receipt_id += 1

        client.shopping_cart.clear()
        client.bill = 0

        return receipt

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
