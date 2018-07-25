# скрипт, который принимает в качестве аргументов ключи и значения и
# выводит информацию из хранилища (в нашем случае — из файла).
# Запись значения по ключу
# > storage.py --key key_name --val value
# Получение значения по ключу
# > storage.py --key key_name
# Ответом в данном случае будет вывод с помощью print соответствующего значения
# > value
# или
# > value_1, value_2
# если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления.
# Обратите внимание на пробел после запятой.
# Если значений по ключу не было найдено, выводите пустую строку или None.
# Для работы с аргументами командной строки используйте модуль argparse.
# Вашей задачей будет считать аргументы, переданные вашей программе,
# и записать соответствующую пару ключ-значение в файл хранилища или вывести значения,
# если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json.
# Проверьте добавление нескольких ключей и разных значений.
# Файл следует создавать с помощью модуля tempfile.
# import os
# import tempfile
# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# with open(storage_path, 'w') as f:
#   ...

import os
import tempfile

import json
import argparse  # Для работы с аргументами командной строки


def parser_create():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--key')
    parser.add_argument('--value', nargs='?')
    # for param, nargs in param_map.items():
    #     parser.add_argument(param, nargs=nargs)
    return parser


def read_storage(path):
    try:
        data = dict(json.load(open(path)))
    except:
        data = {}
    return data


def write_storage(key, value, path, j_data):
    not_to_write = False
    if key in j_data:
        print('Добавляем по ключу {} значение {}'.format(key, value))
        if value not in j_data[key]:
            j_data[key].append(value)
        else:
            print('Такое значение {} уже есть для ключа {}'.format(value, key))
            not_to_write = True
    else:
        print('Добавляем пару ключ: {} значение: {}'.format(key, value))
        j_data[key] = []
        j_data[key].append(value)
    if not not_to_write:
        with open(path, 'w') as f:
            json.dump(j_data, f, indent=2, ensure_ascii=False)
            print('Хранилище обновлено')


if __name__ == '__main__':
    # Путь к файлу
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.json')
    # Создаем парсер для двух параметров и получаем агрументы
    parser = parser_create()
    args = parser.parse_args()
    # Читаем данные из файла
    json_data = read_storage(storage_path)
    # Основное условие
    if args.key and args.value:
        write_storage(args.key, args.value, storage_path, json_data)
    elif args.key and not args.value:
        if args.key in json_data:
            print('Извлечено из хранилище значение для ключа {} ---> {}'.format(args.key, json_data.get(args.key)))
        else:
            print('Ключа {} нет в хранилище'.format(args.key))
    else:
        print('Enter at least --key argument')
        exit()
    # storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    # with open(storage_path, 'w') as f:
    #     f.write('Any')
