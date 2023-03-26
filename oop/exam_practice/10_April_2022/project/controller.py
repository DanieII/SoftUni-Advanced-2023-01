from collections import deque

from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def __get_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    @staticmethod
    def check_if_player_can_duel(player):
        if player.stamina == 0:
            return f"Player {player.name} does not have enough stamina."

    @staticmethod
    def play_duel(players):
        attacks = 0
        winner = None

        while attacks < 2:
            attacker = players.popleft()
            attack = attacker.stamina / 2

            if players[0].stamina - attack <= 0:
                players[0].stamina = 0
                winner = attacker
                break

            attacks += 1
            players[0].stamina -= attack
            players.append(attacker)
            winner = attacker if attacker.stamina > players[0].stamina else players[0]

        return winner.name

    def add_player(self, *args):
        added = []
        for player in args:
            if self.__get_object_from_attribute("name", player.name, self.players):
                continue

            self.players.append(player)
            added.append(player.name)

        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        [self.supplies.append(x) for x in args]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type in ["Food", "Drink"]:

            player: Player = self.__get_object_from_attribute("name", player_name, self.players)

            if player:
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."

                # supplies = list(filter(lambda x: x.supply_type == sustenance_types, reversed(self.supplies)))
                for index in range(len(self.supplies) - 1, -1, -1):
                    if self.supplies[index].supply_type == sustenance_type:
                        supply: Supply = self.supplies.pop(index)
                        break
                else:
                    if sustenance_type == "Food":
                        raise Exception("There are no food supplies left!")
                    elif sustenance_type == "Drink":
                        raise Exception("There are no drink supplies left!")

                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy

                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__get_object_from_attribute("name", first_player_name, self.players)
        player2 = self.__get_object_from_attribute("name", second_player_name, self.players)

        output = []
        # A smarter solution but the walrus operator isn't supported on the python version in judge
        # if result := self.check_if_player_can_duel(player1):
        #     output.append(result)
        # if result := self.check_if_player_can_duel(player2):
        #     output.append(result)
        result1 = self.check_if_player_can_duel(player1)
        if result1:
            output.append(result1)
        result2 = self.check_if_player_can_duel(player2)
        if result2:
            output.append(result2)
        if output:
            return "\n".join(output)

        players = deque(player for player in sorted([player1, player2], key=lambda x: x.stamina))
        winner = self.play_duel(players)

        return f"Winner: {winner}"

    def next_day(self):
        for player in self.players:
            decrease = player.age * 2
            if player.stamina - decrease < 0:
                player.stamina = 0
            else:
                player.stamina -= decrease
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        [result.append(str(x)) for x in self.players]
        [result.append(x.details()) for x in self.supplies]

        return "\n".join(result)
