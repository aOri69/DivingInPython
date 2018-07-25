# Синхронизация потоков, условные переменные
import threading


class Queue(object):
    def __init__(self, size=5):
        self._size = size
        self._queue = []
        self._mutex = threading.RLock()  # Объект блокировок
        # Создаем усл. пер. и передаем туда объект блокировок
        # так как empty и full взаимозависимые, им надо один объект блокировки
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()  # Ждем
            self._queue.append(val)
            self._empty.notify()  # Говорим, что освободились

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()  # Ждем
            ret = self._queue.pop(0)
            self._full.notify()  # Говорим, что освободились
            return ret
