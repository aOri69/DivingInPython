import contextlib


class open_file:  # Название класса с маленькой буквы, потому что это контекстный менеджер
    """Контекстный менеджер with as"""

    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):  # Возвращаем в переменную после AS
        return self.f

    def __exit__(self, *args):  # Обязательные действия по окончании контекстного менеджера
        self.f.close()


class supress_exception:
    """Класс подавляющий исключения"""

    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print('Nothing happend')
            return True  # Обязательно нужно вернуть True


if __name__ == '__main__':
    with open_file("week4/test.log", 'w') as f:
        f.write('Oh////')

    with supress_exception(ZeroDivisionError):
        really_big_number = 1 / 0
    with contextlib.suppress(ValueError):
        raise ValueError
