from datetime import datetime

# Функции без параметров/с параметрами


def get_seconds():
    """Current seconds return"""
    return datetime.now().second


def splt_tags(tag_string):
    """Splitting string by commas"""
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    return tag_list

# Аннотация типов


def add(x: int, y: int)->int:
    return x + y


print(add(2, 3))
print(add('Test ', 'me'))

# Передача по ссылке...всегда


def extender(source_list: list, extend_list: list)->list:
    """List extender by other list"""
    return source_list.extend(extend_list)

# Аргументы по умолчанию


def greeting(name='it\'s me'):
    print('Hello, {}'.format(name))


greeting('Alex!')
greeting()

# Осторожно с изменяемыми значениями по умолчанию


def append_one(iterable=[]):
    iterable.append(1)
    return iterable


print(append_one())
print(append_one())  # тут уже выведет 2 единицы
print(append_one())  # а тут три
print(append_one.__defaults__)  # это дефолтные значения, там TUPLE


def func(iterable=None):  # Правильно делать так, передаем дефолтный параметр как None
    if iterable is None:
        iterable = []


def func2(iterable=None):  # или так...
    iterable = iterable or []

# Множественное количество аргументов.............


def printer(*args):
    print(type(args))
    for arg in args:
        print(arg)


printer(1, 2, 3, 4, 5)  # Просто передача кучи параметров

name_list = ['Alex', 'Ella', 'Helen', 'Oksana']
printer(*name_list)  # В таком случае список развернется

# Точно так же работает и со словарями
# Для передачи именованых параметров... **kwargs


def named_printer(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print('{} - {}'.format(key, value))


named_printer(a=10, b=20)  # Просто передача..

payload = {
    'user_id': 601,
    'feedback': {
        'subject': 'Subject for this user\'s payload',
        'message': 'Oh! This is message!'
    }
}
named_printer(**payload)  # Как бы 2 аргумента user_id, feedback
