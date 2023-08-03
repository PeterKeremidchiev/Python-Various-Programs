from project import OpenBooth
from project import PrivateBooth
from project import Gingerbread
from project import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        existing_delicacy = [d for d in self.delicacies if d.name == name]
        if existing_delicacy:
            raise Exception(f"{name} already exists!")
        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {new_delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        existing_booth = [b for b in self.booths if b.booth_number == booth_number]
        if existing_booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_boot = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_boot)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        search_booth = [b for b in self.booths if not b.is_reserved if b.capacity >= number_of_people]
        if not search_booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        search_booth[0].reserve(number_of_people)
        search_booth[0].is_reserved = True
        return f"Booth {search_booth[0].booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        search_booth = [b for b in self.booths if b.booth_number == booth_number]
        search_delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not search_booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not search_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        search_booth[0].delicacy_orders.append(search_delicacy[0])
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        search_booth = [b for b in self.booths if b.booth_number == booth_number][0]
        calc_bill = search_booth.price_for_reservation + sum(d.price for d in search_booth.delicacy_orders)
        search_booth.delicacy_orders = []
        search_booth.is_reserved = False
        search_booth.price_for_reservation = 0
        self.income += calc_bill
        return f"Booth {booth_number}:\n" + \
               f"Bill: {calc_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())


