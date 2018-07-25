from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, title, text):
        pass


class ObservableEngine:
    def __init__(self) -> None:
        self.__subscribers = set()

    def subscribe(self, subscriber: AbstractObserver):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class ShortPrinter(AbstractObserver):

    def __init__(self) -> None:
        self.achivements = set()

    def update(self, title, text):
        self.achivements.add(title)


class FullPrinter(AbstractObserver):

    def __init__(self) -> None:
        self.achivements = list()

    def update(self, title, text):
        if title not in self.achivements:
            self.achivements.append((title, text))
