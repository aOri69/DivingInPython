from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def do_something(self):
        print('Hi!')


class B(A):
    def do_something(self):
        super().do_something()
        print('Hello!')


if __name__ == '__main__':
    b = B()
    b.do_something()
