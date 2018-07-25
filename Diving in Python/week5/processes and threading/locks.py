# Синхронизация потоков, блокировки
import threading


class Point(object):
    def __init__(self):
        self._mutex = threading.RLock()
        self._x = 0
        self._y = 0

    def get(self):
        with self._mutex:  # Вот тут похоже блокируем классом RLock
            return(self._x, self._y)

    def set(self, x, y):
        with self._mutex:  # И вот тут блокируем
            self._x = x
            self._y = y


# Другой пример на блокировки

a = threading.RLock()
b = threading.RLock()


def foo():
    try:  # Без контекстного менеджера надо быть осторожным
        a.acquire()
        b.acquire()
    finally:
        a.release()  # Вот тут будет дэдлок, не в той последовательности освобождаем
        b.release()
