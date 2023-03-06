from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = [x for x in self.workers if x.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed = sum(x.salary for x in self.workers)
        if needed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed = sum(x.money_for_care for x in self.animals)
        if needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        animals = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            type_of_animal = animal.__class__.__name__
            animals[type_of_animal].append(animal)

        for k, v in animals.items():
            result.append(f"----- {len(v)} {k + 's'}:")
            result.extend(str(x) for x in v)

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        workers = {"Keeper": [], "Caretaker": [], "Vet": []}
        for worker in self.workers:
            type_of_worker = worker.__class__.__name__
            workers[type_of_worker].append(worker)

        for k, v in workers.items():
            result.append(f"----- {len(v)} {k + 's'}:")
            result.extend(str(x) for x in v)

        return "\n".join(result)
