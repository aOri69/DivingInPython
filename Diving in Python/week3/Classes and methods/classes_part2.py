class Planet:
    """Этот класс описывает планеты"""
    count = 0  # Атрибут класса

    def __new__(cls, *args, **kwargs):
        """Непосредственно конструктор экземпляра класса"""
        print('__new__ is called')
        obj = super().__new__(cls)
        return obj

    def __init__(self, name, population=None):
        print('__init__ is called')
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __del__(self):
        """Лучше его не переопределять
        Лучше явно определить действия в явных методах
        для очистки того, что нужно"""
        print("Goodbye!")


if __name__ == '__main__':
    earth = Planet("Earth")
    mars = Planet("Mars")

    print(earth.__dict__)  # Словарь атрибутов, сюда питон смотрит в первую очередь
    earth.mass = 5.97e24
    print(earth.__dict__)  # Здесь появится новый атрибут
    print(Planet.__dict__)  # Объект mappingproxy, здесь будет и атрибут класса count
    print(Planet.__doc__)

    print(earth.__class__)  # Получаем класс, которому принадлежит экземпляр

    print(Planet.count)
    print(mars.count)  # Есди атрибут не будет найден у экземпляра, он будет искаться в классе
    del earth
    del mars
