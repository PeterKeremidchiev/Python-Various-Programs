from project import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float, weight: int = 9):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 3

# mr = MaleRobot("asd", "asd", 10.2, 2)
# mr.eating()
# print(mr.weight)
# print(mr.name)