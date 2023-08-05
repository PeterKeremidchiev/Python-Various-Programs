from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    QUANTITY_REMOVED = {}
    receipt_id = 0
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)
            else:
                continue

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return '\n'.join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name]
            if not meal and client:
                client[0].shopping_cart = []
                client[0].bill = 0.0
                raise Exception(f"{meal_name} is not on the menu!")
            if not meal and not client:
                new_client.shopping_cart = []
                new_client.bill = 0.0
                raise Exception(f"{meal_name} is not on the menu!")
            if quantity > meal[0].quantity:
                if client:
                    client[0].shopping_cart = []
                    client[0].bill = 0.0
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal[0].name}!")
                if not client:
                    new_client.shopping_cart = []
                    new_client.bill = 0.0
                    raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal[0].name}!")

            if client:
                client[0].shopping_cart.append(meal[0])
                client[0].bill += quantity * meal[0].price
                meal[0].quantity -= quantity
                if meal[0].name in self.QUANTITY_REMOVED:
                    self.QUANTITY_REMOVED[meal[0].name] += quantity
                else:
                    self.QUANTITY_REMOVED[meal[0].name] = quantity
            if not client:
                new_client.shopping_cart.append(meal[0])
                new_client.bill += quantity * meal[0].price
                meal[0].quantity -= quantity
                if meal[0].name in self.QUANTITY_REMOVED:
                    self.QUANTITY_REMOVED[meal[0].name] += quantity
                else:
                    self.QUANTITY_REMOVED[meal[0].name] = quantity
        if client:
            return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client[0].shopping_cart])} for {client[0].bill:.2f}lv."
        if not client:
            return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in new_client.shopping_cart])} for {new_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal_in_menu = [m for m in self.menu if m.name == meal.name][0]
            meal_in_menu.quantity += self.QUANTITY_REMOVED[meal_in_menu.name]
            self.QUANTITY_REMOVED[meal_in_menu.name] = 0

        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        total_paid = client.bill
        client.bill = 0
        client.ordered_meals = {}
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print(food_orders_app.cancel_order('0899999999'))
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)
