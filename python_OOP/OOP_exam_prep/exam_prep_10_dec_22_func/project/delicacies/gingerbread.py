from project import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."

# gb = Gingerbread("test", 5.5)
# print(gb.portion)

