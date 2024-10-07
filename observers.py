from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def update(state):
        pass


class StartupObserver(Observer):
    @staticmethod
    def update(state):
        if state == 'Start':
            print('Startup Observer is updating ...')


class StopObserver(Observer):
    @staticmethod
    def update(state):
        if state == 'Stop':
            print('Stop Observer is updating ...')


class SleepObserver(Observer):
    @staticmethod
    def update(state):
        if state == 'Sleep':
            print('Sleep Observer is updating ...')
