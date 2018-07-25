from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""


class Child(Sender):  # Обязаны переопределить все абстракции
    def send(self):
        print("something")


class PythonWay:
    """Вот так в питоне делать принято"""

    def send(self):
        raise NotImplementedError


print(Child())
