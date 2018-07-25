# Пример декоратора, который записывает в лог результат декорируемой функции
import functools


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result

    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print(summator.__name__)
summator([1, 2, 3, 4, 5, 6, 7, 8, 9])


# А теперь декоратор, который может писать в конкретный файл...
def logger_new_file(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result

        return wrapped

    return decorator


@logger_new_file('new_log.txt')
def summator2(num_list):
    return sum(num_list)


print(summator2.__name__)
# summator2 = logger_new_file('new_log.txt')(summator2) На самом деле происходит вот это
summator2([1, 2, 3, 4])


# Вот что будет, если применить сразу несколько декораторов
def first_deco(func):
    def wrapped():
        print('Firs decorator is called...')
        return func()

    return wrapped


def second_deco(func):
    def wrapped():
        print('Second decorator is called...')
        return func()

    return wrapped


@first_deco
@second_deco
def decorator():
    print('Function called')


decorator()


# decorated = first_deco(second_deco(decorator)) # А на самом деле вызов такой...

# И еще один пример
def bold_decor(func):
    def wrapped():
        return '<b>' + func() + '</b>'

    return wrapped


def italic_decor(func):
    def wrapped():
        return '<i>' + func() + '</i>'

    return wrapped


@bold_decor
@italic_decor
def hello():
    return 'Hello World!'


# hello = bold_decor(italic_decor(hello())) На самом деле так
print(hello())
