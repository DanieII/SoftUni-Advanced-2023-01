from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        result = [f"{self.name} Secondary Service:"]
        if not self.robots:
            result.append("Robots: none")
        else:
            robots = []
            for robot in self.robots:
                robots.append(robot.name)

            result.append(f"Robots: {' '.join(robots)}")

        return "\n".join(result)
