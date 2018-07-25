# Создание потока

from threading import Thread


def f(name):
    print('Hello', name)


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Hello', self.name)


if __name__ == '__main__':
    # Аналогичный способ 1
    th = Thread(target=f, args=('Bob',))
    th.start()
    th.join()
    # Аналогичный способ 2 при помощи наследования
    th = PrintThread('Mike')
    th.start()
    th.join()
