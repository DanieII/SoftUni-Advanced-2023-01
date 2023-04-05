from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    Food = {
        "Bread": Bread,
        "Cake": Cake,
    }
    Drinks = {
        "Tea": Tea,
        "Water": Water,
    }
    Tables = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def find_item_in_menu_by_name(name, collection):
        for food in collection:
            if food.name == name:
                return food
        return None

    def add_food(self, food_type: str, name: str, price: float):
        existing_foods = [x for x in self.food_menu if x.name == name]
        if existing_foods:
            raise Exception(f"{existing_foods[0].__class__.__name__} {name} is already in the menu!")

        food = self.Food[food_type](name, price)
        self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        existing_drinks = [x for x in self.drinks_menu if x.name == name]
        if existing_drinks:
            raise Exception(f"{existing_drinks[0].__class__.__name__} {name} is already in the menu!")

        drink = self.Drinks[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)

        return f"Added {name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [x.table_number for x in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.Tables[table_type](table_number, capacity)
        self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            table = [x for x in self.tables_repository if not x.is_reserved and x.capacity >= number_of_people][0]
        except IndexError:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        try:
            table = [x for x in self.tables_repository if x.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        found = []
        not_found = []

        for food_name in args:
            result = self.find_item_in_menu_by_name(food_name, self.food_menu)
            if result:
                found.append(result)
                table.order_food(result)
            else:
                not_found.append(food_name)

        output = [f"Table {table_number} ordered:"]

        for food in found:
            output.append(food.__repr__())

        output.append(f"{self.name} does not have in the menu:")

        for food in not_found:
            output.append(food)

        return "\n".join(output)

    def order_drink(self, table_number: int, *args):
        try:
            table = [x for x in self.tables_repository if x.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        found = []
        not_found = []

        for drink_name in args:
            result = self.find_item_in_menu_by_name(drink_name, self.drinks_menu)
            if result:
                found.append(result)
                table.order_drink(result)
            else:
                not_found.append(drink_name)

        output = [f"Table {table_number} ordered:"]

        for drink in found:
            output.append(drink.__repr__())

        output.append(f"{self.name} does not have in the menu:")

        for drink in not_found:
            output.append(drink)

        return "\n".join(output)

    def leave_table(self, table_number: int):
        table = [x for x in self.tables_repository if x.table_number == table_number][0]
        bill = table.get_bill()
        table.clear()

        self.total_income += bill

        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        free_tables = []
        for table in self.tables_repository:
            info = table.free_table_info()
            if info:
                free_tables.append(info)

        return "\n".join(free_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
