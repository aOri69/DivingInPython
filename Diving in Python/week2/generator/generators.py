# Простейший генератор
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


# По генератору можно итерироваться
# Оператор yield придержит значение, и потом к нему вернется
# в функции возвращаемое значение None
for num in even_range(0, 10):
    print(num)

# Вот как это работает
# В конце иксепшн StopIteration
ranger = even_range(0, 4)
print(next(ranger))
print(next(ranger))
# print(next(ranger))

# Числа фибоначчи


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print([num for num in fibonacci(10)])

# Аккумулирование значений


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
# Если значение не передано, то выходим из аккумулятора
        if not value:
            break
        total += value
    # return accumulator

gen = accumulator()
print(next(gen))
print('Accumulated: {}'.format(gen.send(2)))
