from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            r_num = [r_n for r_n in self.rooms if r_n.number == room_number][0]
            if r_num.capacity >= people and not r_num.is_taken:
                self.guests += people
                r_num.guests += people
                r_num.is_taken = True
        except IndexError:
            pass

    def free_room(self, room_number):
        try:
            r_num = [r_n for r_n in self.rooms if r_n.number == room_number][0]
            if r_num.is_taken:
                r_num.is_taken = False
                self.guests -= r_num.guests
                r_num.guests = 0
        except IndexError:
            pass

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken = [t for t in self.rooms if t.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(x.number) for x in taken])}"
