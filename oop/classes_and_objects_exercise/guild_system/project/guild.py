from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        try:
            member = [x for x in self.players if x.name == player_name][0]
            member.guild = "Unaffiliated"
            self.players.remove(member)
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        [result.append(x.player_info()) for x in self.players]

        return "\n".join(result)
