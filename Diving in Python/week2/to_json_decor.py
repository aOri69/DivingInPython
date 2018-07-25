# декоратор to_json, который можно применить к различным функциям,
# чтобы преобразовывать их возвращаемое значение в JSON-формат.
# Не забудьте про сохранение корректного имени декорируемой функции.
# @to_json
# def get_data():
#   return {
#     'data': 42
#   }
# get_data()  # вернёт '{"data": 42}'
import functools
import json


def to_json(func):
    @functools.wraps(func)
    def decorated(*args, **kwagrs):
        result = func(*args, **kwagrs)
        return result

    return decorated


@to_json
def get_data(param):
    return {'data': param}


if __name__ == '__main__':
    print(get_data({'key': 'value'}))
    print(get_data([1, 2, 3]))
    print(get_data({'key': 'value', 'nested': {'list': [1, 2, 3, 4]}}))
