from abc import ABC, abstractmethod

from observer_project.notification_decorator import observer_decorator


class AbstractMachine(ABC):

    def __init__(self):
        self.state = None
        self.observers = []

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        pass


class MyMachine(AbstractMachine):
    @observer_decorator
    def start(self):
        self.state = 'Start'

    @observer_decorator
    def stop(self):
        self.state = 'Stop'

    @observer_decorator
    def sleep(self):
        self.state = 'Sleep'

    def add_observer(self, observer):
        self.observers.append(observer)




