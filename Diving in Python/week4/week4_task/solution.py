"""
В этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.
Класс инициализируется полным путем.
obj = File('/tmp/file.txt')
Класс должен поддерживать метод write.
obj.write('line\n')
Объекты типа File должны поддерживать сложение.
first = File('/tmp/first')
second = File('/tmp/second')

new_obj = first + second
В этом случае создается новый файл и файловый объект,
в котором содержимое второго файла добавляется к содержимому первого файла.
Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir.
Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.
for line in File('/tmp/file.txt'):
  ...
И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.
obj = File('/tmp/file.txt')

print(obj)
'/tmp/file.txt'
"""
from tempfile import gettempdir
import os
import uuid


class File:
    def __init__(self, full_path: str):
        # Для итератора
        self.content_list = []
        self.current = 0
        self.end = 0
        # Для открытия
        self.full_path = full_path
        if not os.path.exists(self.full_path):
            open(self.full_path, 'w').close()

    def write(self, content):
        with open(self.full_path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.full_path, 'r') as f:
            return f.read()

    def __str__(self):
        return self.full_path

    def __iter__(self):  # Должен возвращать итератор в себя
        # if not self.file.readable():
        #     self.__exit__()
        with open(self.full_path, 'r') as f:
            self.content_list = f.readlines()
        self.current = 0
        self.end = len(self.content_list)
        return self

    def __next__(self):  # Определяет какие элементы возвращаются во время итераций
        if self.current >= self.end:
            raise StopIteration
        result = self.content_list[self.current]
        self.current += 1
        return result
    # Другой варик
    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     with open(self.path, 'r') as f:
    #         f.seek(self.current_position)

    #         line = f.readline()
    #         if not line:
    #             self.current_position = 0
    #             raise StopIteration('EOF')

    #         self.current_position = f.tell()
    #         return line

    def __add__(self, obj):
        path = os.path.join(os.getcwd(), "week4\\week4_task\\temp", "add.txt")
        result = self.read() + obj.read()
        with open(path, 'w') as add:
            add.write(result)
            return add
    # Другой варик
        # new_path = os.path.join(os.path.dirname(
        #     self.full_path), str(uuid.uuid4().hex))
        # new_file = type(self)(new_path)
        # new_file.write(self.read() + obj.read())
        # return new_file


def main():
    first_path = os.path.join(
        os.getcwd(), "week4\\week4_task\\temp", "first.txt")
    second_path = os.path.join(
        os.getcwd(), "week4\\week4_task\\temp", "second.txt")
    string_to_write = '\nline '.join(map(str, range(1, 101)))
    first = File(first_path)
    first.write(string_to_write)
    second = File(second_path)
    string_to_write = '\nline '.join(map(str, range(1, 50)))
    second.write(string_to_write)
    for line in File(first_path):
        print(line)
    third = first + second
    print(type(third), third)


if __name__ == '__main__':
    main()
