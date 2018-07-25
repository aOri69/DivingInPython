"""Дескриптор, который пишет в файл все присваеваемые значения"""


class ImportantValue:
    def __init__(self, amount):
        self._amount = amount

    def __get__(self, obj, obj_type):
        return self._amount

    def __set__(self, obj, value):
        with open('./week4/descriptors/descriptor_log.txt', 'w') as f:
            f.write(str(value))
        self._amount = value


class Account:
    amount = ImportantValue(100)  # Амоунт является дата дескриптором


# На самом деле если вызывать метод от объекта и от класса, то вернутся разные объекты
# class Class:
#     def method(self):
#         pass
# obj = Class()
# print(obj.method) # Вернется bound method
# print(Class.method) # Вернется function как просто функция

class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name

    @property  # Вроде функция, а вроде атрибут...короче тоже через дескрипторы
    def full_name(self):
        return f'{self.first} {self.last}'


class Property:
    """# Тот же самый декоратор, написанный с помощью класса дескриптора"""

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        return self.getter(obj)


class Class:
    @property  # Обычный проперти
    def original(self):
        return 'original'

    @Property  # Самописный проперти
    def custom_sugar(self):
        return 'custom_sugar'

    def custom_pure(self):
        return 'custom_pure'

# Точно так же реализованы статические методы и классметоды


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):  # Потому что нужно передать еще и класс
            return self.func(obj_type, *args, **kwargs)


# Конструкция __SLOTS__ позволят жестко ограничить количество атрибутов в классе
class Class2:
    __slots__ = ["anakin"]

    def __init__(self):
        self.anakin = 'the chosen one'


def main():
    bob_acc = Account()
    bob_acc.amount = 150

    amy = User('Amy', 'Jones')
    print(amy.full_name)
    print(User.full_name)

    obj = Class()
    print(obj.original)  # Будет вызван стандартный дескриптор
    print(obj.custom_sugar)  # Будет вызван дескриптор наш
    print(obj.custom_pure)

    obj = Class2()
    obj.luke = 'the chosen too'  # __slots__ ограничивает создание атрибутов


if __name__ == '__main__':
    main()
