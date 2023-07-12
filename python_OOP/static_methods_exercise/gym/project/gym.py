from typing import List

from project import Customer
from project import Equipment
from project import ExercisePlan
from project import Subscription
from project import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subs = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [s for s in self.customers if s.id == subscription_id][0]
        trainer = [s for s in self.trainers if s.id == subscription_id][0]
        equipment = [s for s in self.equipment if s.id == subscription_id][0]
        plan = [s for s in self.plans if s.id == subscription_id][0]

        result = f"{subs}\n" + f"{customer}\n" + f"{trainer}\n" + f"{equipment}\n" + f"{plan}\n"
        return result
