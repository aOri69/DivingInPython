class Human:
    def __init__(self, name, age=0):
        """Атрибуты приватные"""
        self._name = str(name).lower().capitalize()
        self._age = age

    def _say(self, text):
        """Приватный метод"""
        print(text)

    def say_name(self):
        self._say(f"Hello, my name is {self._name}")

    def say_age(self):
        self._say(f"I\'m {self._age} years old")


class Planet:
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human: Human):
        # print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


def extract_desctiption(user_string):
    return "Открытие чемпионата мира по футболу"


def extract_date(user_string):
    return "14.06.2018" #date(2018, 6, 14)


class Event:
    def __init__(self, descr, ev_date):
        self.decription = descr
        self.date = ev_date

    def __str__(self):
        return f"Event \"{self.decription}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        """Это метод класса, не привязан к экземпляру"""
        desription = extract_desctiption(user_input)
        date = extract_date(user_input)
        return cls(desription, date)


if __name__ == "__main__":
    mars = Planet("Mars")
    bob = Human("Bob", 28)
    bob.say_age()
    bob.say_name()
    mars.add_human(bob)

    event = Event.from_string("Добавить в мой календарь открытие чемпионата мира на 14 июня 2018 года")

    # Пример метода класса у словарей
    print(dict.fromkeys("123456789"))
