import json


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f"{self.name}: waw"


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


class exDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # Вызов по Method Resolution Order
        super().__init__(name, breed=None)
        # super(ExDog, self).__init__(name) тоже самое


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # Явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Woolen dog breed {0}".format(breed)


if __name__ == "__main__":
    dog = Dog("Sharik", "Doberman")
    print(dog.name)
    print(dog.say())
    del dog
    dog = exDog("Belka", "Dvornjaga")
    print(dog.to_json())

    # Любой класс является потомком Object
    print(issubclass(Dog, object))

    # Поиск атрибутов и методов объекта, линеаризация класса
    #       object
    #     /         \
    #   Pet         ExportToJSON
    #    |           /
    #   Dog         /
    #     \        /
    #       ExDog
    print(exDog.__mro__)
    del dog
    dog = WoolenDog("Juchka", "Taksa")
    print(dog.breed)
