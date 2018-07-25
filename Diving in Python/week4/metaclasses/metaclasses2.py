"""Вариант логирования всех подклассов с помощью метакласса"""


class Meta(type):
    """Логируем все созданные подклассы"""
    def __init__(cls, name, bases, attrs):
        print('Initialising - {}'.format(name))
        # Записываем в собственный атрибут, все созданные подклассы
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls
        super().__init__(name, bases, attrs)


class Base(metaclass=Meta):
    """Когда создаем класс с наследуемым метаклассом, будет создаваться атрибут registry"""
    pass


class A(Base):
    pass


class B(Base):
    pass


def main():
    print(Base.registry)
    print(Base.__subclasses__())


if __name__ == '__main__':
    main()
