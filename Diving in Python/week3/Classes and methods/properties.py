class C:
    """GET-SET-DELETE"""

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot:
    """READ-ONLY"""

    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


class D:
    """GET-SET-DELETE"""

    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


def main():
    c = C()
    c.x = 'value'
    print(c.x)
    d = D()
    d._x = 'value'  # Вот эта штука не через сеттер работает, но так лучше не делать
    print(d.x)
    parrot = Parrot()
    print(parrot.voltage)  # вызовет геттер
    parrot._voltage = 12  # Изменить можно, но он как бы приватный
    parrot.voltage = 12  # А вот так рид онли


if __name__ == '__main__':
    main()
