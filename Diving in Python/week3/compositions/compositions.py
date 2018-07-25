import json
"""Тот случай, когда композиция классов лучше наследования
удобно для расширения"""

# Основной класс композиция


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class ExportJSON(PetExport):  # Расширяем класс композицию
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed,
        })


class ExportXML(PetExport):  # Расширяем класс композицию
    def export(self, dog):
        return """<?xml version="1.0"> encoding="utf-8"?>
<dog>
    <name>{0}</name>
    <breed>{1}</breed>
</dog>
""".format(dog.name, dog.breed)


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed=None)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError

    def export(self):
        return self._exporter.export(self)


if __name__ == '__main__':
    dog = ExDog("Sharik", "Mops", exporter=ExportXML())
    print(dog.export())
    del dog
    dog = ExDog("Tuzik", "Doberman")
    print(dog.export())
