
from project.services import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if not self.robots:
            result += "Robots: none"
        else:
            result += f"Robots: {' '.join([r.name for r in self.robots])}"
        return result

# ms = MainService("test")
# fr = FemaleRobot("mima", "female", 5.5, 5)
# fr_2 = FemaleRobot("mima", "female", 5.5, 5)
# print(ms.capacity)
# ms.robots.append(fr)
# ms.robots.append(fr_2)
# print(ms.details())
