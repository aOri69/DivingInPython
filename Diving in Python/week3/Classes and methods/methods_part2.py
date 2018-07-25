# Статический метод класса @staticmethod
class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        """Статический метод не принимает на вход cls """
        return 0 < age < 150


# Вычисляемые свойства класса property
class Robot:
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power

# Аналогично можно использовать просто декоратор property для полезных вычислений


class Robo2:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        # Здесь могут быть любые полезные вычисления
        return self._power


if __name__ == "__main__":
    wall_e = Robot(100)
    wall_e.power = -20
    print(wall_e.power)
    del wall_e.power
    eva = Robo2(150)
    print(eva.power)
