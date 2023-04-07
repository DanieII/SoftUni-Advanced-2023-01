from typing import List

from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(x.expenses + x.room_cost for x in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                result.append(f"{room.family_name} paid {room.expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return "\n".join(result)

    def status(self):
        result = [f"Total population: {sum(x.members_count for x in self.rooms)}"]
        for room in self.rooms:
            result.append(
                f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            if room.children:
                for i, child in enumerate(room.children):
                    result.append(f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$")

            result.append(f"--- Appliances monthly cost: {sum(x.get_monthly_expense() for x in room.appliances):.2f}$")

        return "\n".join(result)
