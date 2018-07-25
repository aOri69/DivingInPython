import random
from string import ascii_letters


class Singleton:
    instance = None

    def __new__(cls):  # Вызывается в момент создания экземпляра до __init__
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):  # Меняет поведение при печати экземпляра
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):  # Переопределение хэширования(например, когда получаем ключи в словаре)
        return hash(self.email)

    def __eq__(self, obj):  # Переопределение ==
        return self.email == obj.email


class Researcher:
    def __getattr__(self, name):  # Определяет поведение, когда атрибут не найден
        return 'Nothing found'

    def __getattribute__(self, name):  # Вызывается всегда, когда обращаемся к атрибутам
        print(f'Looking for a {name}')  # Логируем доступ к атрибуту
        return object.__getattribute__(self, name)

    # Управляет поведенеием при попытке записать значение в атрибут
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __delattr__(self, name):  # Управляет поведением, когда удаляем атрибут
        object.__delattr__(self, name)


class Logger:
    """Класс логирования, впоследствии может использоваться в качестве декоратора"""

    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):  # Переопределяет поведение, когда класс вызывается
        with open(self.filename, 'w') as f:
            f.write('Oh....writing!')
        return func


logger = Logger('log.txt')  # Экземпляр будет вызван в качестве декоратора


@logger
def useless():  # Класс будет вызван
    pass


class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):  # Перегрузка сложения
        noise = random.uniform(-1, 1)
        return self.value + noise + obj.value


class MyContainer(object):
    def __init__(self):
        self.storage = {}

    # Метод присущ контейнерам и вызывается при выполнении инструкций вида obj[key] = value.
    def __setitem__(self, key, value):
        self.storage[key] = value

    # Метод присущ контейнерам и вызывается при выполнении инструкций вида obj[key] = value.
    def __getitem__(self, key):
        return self.storage[key]


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()

    print(a is b)

    # Два юзера с одинаковыми емайлами
    jane = User('Jane Doe', 'jdoe@example.com')
    joe = User('Joe Doe', 'jdoe@example.com')
    print(jane)
    print(joe)
    print(jane == joe)
    print(hash(jane), hash(joe))
    user_email_map = {user: user.name for user in [jane, joe]}
    print(user_email_map)

    obj = Researcher()

    print(obj.dkfjaklf)
    print(obj.asdfkasdjflkasfasdlkfj)
    # Операция сложения перегуржена
    a = NoisyInt(10)
    b = NoisyInt(20)
    print(a+b)
    print(a+b)
    print(a+b)
