from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number][0]

        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number][0]

        guests = room.guests
        result = room.free_room()

        if result:
            return result

        self.guests -= guests

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}",
                  f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"]
        return "\n".join(result)
