class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        properties = ["Player", "Sprint", "Dribble", "Passing", "Shooting"]
        result = []
        for index in range(len(properties)):
            result.append(f"{properties[index]}: {list(self.__dict__.values())[index]}")
        return "\n".join(result)
