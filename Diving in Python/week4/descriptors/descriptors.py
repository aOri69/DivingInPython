class Descriptor:
    """Класс дескриптор переопреляет поведение, при доступе к атрибутам"""

    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Value:
    """Здесь при записи значения в атрибут, оно будет умножаться на 10 дескриптором"""

    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value*10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class:
    attr = Descriptor()
    attr_1 = Value()


def main():
    instance = Class()
    print(instance.attr)
    instance.attr = 10
    del instance.attr

    instance.attr_1 = 10
    print(instance.attr_1)


if __name__ == '__main__':
    main()
