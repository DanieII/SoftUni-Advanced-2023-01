from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES:
            raise Exception("Invalid service type!")

        service = self.SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [x for x in self.robots if x.name == robot_name][0]
        service = [x for x in self.services if x.name == service_name][0]

        robot_type = robot.__class__.__name__
        service_type = service.__class__.__name__

        if robot_type == "FemaleRobot":
            if service_type == "MainService":
                return "Unsuitable service."

        elif robot_type == "MaleRobot":
            if service_type == "SecondaryService":
                return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        try:
            robot = [x for x in service.robots if x.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]

        total_price = sum(x.price for x in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []

        for service in self.services:
            result.append(service.details())

        return "\n".join(result)
