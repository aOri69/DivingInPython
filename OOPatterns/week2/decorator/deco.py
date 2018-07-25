from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print('eating grass')

    def move(self):
        print('walking')

    def make_noise(self):
        print('WOOO!')


class AbstractDecorator(Creature):

    def __init__(self, base: Creature):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):

    def move(self):
        print('swimming')

    def make_noise(self):
        print('...')


class Predator(AbstractDecorator):

    def feed(self):
        print('animals')


class Fast(AbstractDecorator):
    def move(self):
        self.base.move()
        print('Fast')


if __name__ == '__main__':
    animal = Animal()
    animal.move()
    animal.feed()
    animal.make_noise()
    swimming = Swimming(animal)
    swimming.move()
    swimming.feed()
    swimming.make_noise()
    predator = Predator(swimming)
    predator.move()
    predator.feed()
    predator.make_noise()
    fast = Fast(predator)
    fast.move()
    fast.feed()
    fast.make_noise()

    faster = Fast(fast)
    faster.move()
    faster.feed()
    faster.make_noise()

    # Detach decorator
    faster.base.base = faster.base.base.base
    faster.move()
    faster.feed()
    faster.make_noise()
