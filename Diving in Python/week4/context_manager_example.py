import time
# https://docs.python.org/3/reference/datamodel.html


class timer():
    """
    Контекстный менеджер, который считает сколько времени проведено внутри него
    """

    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(f'Elapsed time: {self.current_time()}')


if __name__ == '__main__':

    with timer() as t:
        time.sleep(1)
        print(f'First elapsed time {t.current_time()}')
        time.sleep(1)
