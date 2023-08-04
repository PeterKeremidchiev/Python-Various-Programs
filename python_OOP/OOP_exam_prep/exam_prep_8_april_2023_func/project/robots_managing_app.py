from project import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services import MainService
from project.services import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"SecondaryService": SecondaryService, "MainService": MainService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")
        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot_obj = [obj for obj in self.robots if obj.name == robot_name][0]
        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        if robot_obj.__class__.__name__ == "MaleRobot" and service_obj.__class__.__name__ == "SecondaryService":
            return "Unsuitable service."
        if robot_obj.__class__.__name__ == "FemaleRobot" and service_obj.__class__.__name__ == "MainService":
            return "Unsuitable service."
        if len(service_obj.robots) >= service_obj.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot_obj)
        service_obj.robots.append(robot_obj)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        robot_obj = [obj for obj in service_obj.robots if obj.name == robot_name]

        if not robot_obj:
            raise Exception("No such robot in this service!")
        service_obj.robots.remove(robot_obj[0])
        self.robots.append(robot_obj[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        for robot in service_obj.robots:
            robot.eating()
        return f"Robots fed: {len(service_obj.robots)}."

    def service_price(self, service_name: str):
        service_obj = [obj for obj in self.services if obj.name == service_name][0]
        price = 0
        for robot in service_obj.robots:
            price += robot.price
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])



# main_app = RobotsManagingApp()
# print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
# print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
# print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
# print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
#
# print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
#
# print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
# print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
#
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
# print(str(main_app))
#
# print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))





