from inher import Pet, ExportJSON
# Разрешение конфликта имен


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return f"{self.name}: waw"

    def get_breed(self):
        return self.__breed


class ExDog(Dog, ExportJSON):
    def get_breed(self):
        # Вот тут внимательнее
        return f"Breed: {self.name} - {self._Dog__breed}"
        # Так конечно лучше не делать


if __name__ == '__main__':
    dog = ExDog("Foks", "Mops")
    print(dog.__dict__)
    print(dog.get_breed())
