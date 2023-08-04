from project import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float, weight: int = 7):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 1

# fr = FemaleRobot("asd", "female", 5.5, 5)
# fr.eating()
# print(fr.weight)