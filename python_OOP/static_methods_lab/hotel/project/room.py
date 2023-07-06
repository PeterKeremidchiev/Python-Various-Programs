class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.capacity <= people or self.is_taken:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f"Room number {self.number} is not taken"

