from abc import ABC, abstractmethod
import time


class Work(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Eat(ABC):

    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Work, Eat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):

    def work(self):
        print("I'm a robot. I'm working....")


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Work), "`worker` must be of type {}".format(Work)

        self.worker = worker

    def manage(self):
        self.worker.work()


class LunchManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eat), "`worker` must be of type {}".format(Eat)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
lunch_manager = LunchManager()

work_manager.set_worker(Robot())
work_manager.manage()

lunch_manager.set_worker(SuperWorker())
lunch_manager.lunch_break()

work_manager.set_worker(SuperWorker())
work_manager.manage()
