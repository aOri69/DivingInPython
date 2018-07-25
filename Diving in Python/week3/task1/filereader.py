"""
Ваша задача написать Python-модуль solution.py, внутри которого определен класс FileReader.
Инициализатор этого класса принимает аргумент - путь до файла на диске.
У класса должен быть метод read, возвращающий содержимое файла в виде строки.
Еще один момент - внутри метода read вы должны обрабатывать исключение IOError,
возникающее, когда файла, с которым был инициализирован класс, на самом деле нет на жестком диске.
В случае возникновения такой ошибки метод read должен возвращать пустую строку "".
То есть класс должен работать следующим образом:
    reader = FileReader("example.txt")
    print(reader.read())
"""
import sys
import os.path


class FileReader:
    """Самодельное чтение файла"""

    def __init__(self, filename):
        self._filename = filename
        self.__content = str()

    def read(self):
        """Чтение"""
        try:
            if not os.path.exists(self._filename):
                raise IOError("Файл не существует", self._filename)
            with open(self._filename, encoding='UTF-8') as f:
                self.__content = f.read()
        except IOError as err:
            print(f"Произошло исключение: {err.args[0]}: {err.args[1]}")

        return self.__content


def main():
    """main"""
    reader = FileReader(sys.argv[1])
    print(reader.read())


if __name__ == '__main__':
    main()
