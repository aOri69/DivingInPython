class Human:
    """Данный класс ничего не делает"""
    pass


class Robot:
    """Данный класс ничего не делает"""


class Planet:
    def __init__(self, name):
        """Конструктор....self всегда"""
        self.name = name

    def __str__(self):
        """Переопределение метода __str__
           определяем как будет печататься объект"""
        return self.name

    def __repr__(self):
        """Метод меняет внутреннее представление экземпляра"""
        return f"Planet-{self.name}"


if __name__ == "__main__":
    print(Robot)
    print(dir(Robot))

    # Создание экземпляра
    planet = Planet("Name")
    print(planet)

    # Можно собрать экземпляры в список, или в словарь!(Они хэшируются)
    planet_names = [
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uran", "Neptun"
    ]
    solar_system_list = []
    solar_system_dict = {}
    for name in planet_names:
        planet = Planet(name)
        solar_system_list.append(planet)  # Список
        solar_system_dict[planet] = True  # Или даже словарь

    print(solar_system_dict)
    print(solar_system_list)
