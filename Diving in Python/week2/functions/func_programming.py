# Функции в качестве аргумента
def caller(func, params):
    return func(*params)


def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))


caller(printer, ['King', 'Damned'])


# Функции в качестве возвращаемого параметра


def get_multiplier():
    def inner_func(a, b):
        return a * b

    return inner_func


multiplier = get_multiplier()
print(multiplier.__name__)  # Имя самой внутренней функции
print(multiplier(3, 4))


# Функции в качестве возвращаемого параметра с аргументами


def get_multiplier_by(number):
    def inner_func(a):
        return a * number

    return inner_func


mult_by_3 = get_multiplier_by(3)
print(mult_by_3(6))


# Применение функции к набору аргументов........map,filter,lambda
# """Применение MAP"""


def sqarify(a):
    return a ** 2


# Коротко
print(list(map(sqarify, range(10))))
# Тоже самое
squared_list = []
for number in range(10):
    squared_list.append(sqarify(number))


# """ Применение FILTER """


def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-5, 5))))

# Анонимные функции LAMBDA
print(list(map(lambda x: x ** 2, range(10))))


# Например функция переводит список чисел в список строк


def int_to_str_list(num_list):
    return list(map(str, num_list))


print(int_to_str_list(range(10)))

# Полезный модуль functools и ф-я reduce
from functools import reduce


def mult(a, b):
    return a * b


# Последовательно передает на вход mult сначала 1,2(1*2), к получ. рез-ту 3(2*3), и т.д.
print(reduce(mult, [1, 2, 3, 4, 5]))
# Тоже самое)
print(reduce(lambda x, y: x * y, range(1, 6)))

# Подмена параметров - ф-ция partial

from functools import partial


def greeter(name, greeting):
    return '{}, {}!'.format(greeting, name)


# Подмена параметра greeting в функции greeter
hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')
print(hier('brother'))
print(helloer('Sir'))

# Списочные выражения!!!!!!!!!!!!!!!
# По-старому
square_list = []
for number in range(10):
    square_list.append(number ** 2)
print(square_list)
# По-новому
square_list = [number ** 2 for number in range(10)]
print(square_list)
# Точно так же и с условиями
even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)

# АНАЛОГИЧНО СО СЛОВАРЯМИ
square_map = {number: number ** 2 for number in range(10)}
print(square_map)

# НУ И АНАЛОГИЧНО С МНОЖЕСТВАМИ
reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

# Функция ZIP склеивает списки(первый элемент первого и второго списков попадают в один кортеж)
num_l = list(range(7))
sqa_l = [x ** 2 for x in num_l]
print(list(zip(num_l, sqa_l)))
