"""
Смотри description.md
"""
import csv
import sys
import os.path


class BaseCar:

    def __init__(self, car_type: str, brand: str, carrying, photo_file_name):
        self._car_type = car_type.lower()
        self._brand = brand
        self._carrying = float(carrying)
        self._photo_file_name = photo_file_name

    def __str__(self):
        return f'{self._car_type} - {self._brand} - {self._carrying}'

    def get_photo_file_ext(self):
        """Получение расширения файла картинки"""
        ext = os.path.splitext(self._photo_file_name)
        return ext[1]


class Car(BaseCar):
    def __init__(self, car_type, brand, carrying, photo_file_name, passenger_seats_count):
        super().__init__(car_type, brand, carrying, photo_file_name)
        self._passenger_seats_count = int(passenger_seats_count)

    def __str__(self):
        return super().__str__() + f' пассажирских мест - {self._passenger_seats_count}'


class Truck(BaseCar):
    def __init__(self, car_type, brand, carrying, photo_file_name, body_whl: str):
        super().__init__(car_type, brand, carrying, photo_file_name)
        self._lenght = 0.0
        self._width = 0.0
        self._height = 0.0
        splited = body_whl.split("x")
        if len(splited) == 3:
            # if splited[2].isdigit() else 0.0)
            self._lenght = float(splited[0])
            # if splited[2].isdigit() else 0.0)
            self._width = float(splited[1])
            # if splited[2].isdigit() else 0.0)
            self._height = float(splited[2])

    def __str__(self):
        return super().__str__() + f' Объем кузова - {self.get_body_volume()}'

    def get_body_volume(self):
        """Получение объема грузовика"""
        return self._lenght * self._width * self._height


class SpecMachine(BaseCar):
    def __init__(self, car_type, brand, carrying, photo_file_name, extra):
        super().__init__(car_type, brand, carrying, photo_file_name)
        self._extra = extra

    def __str__(self):
        return super().__str__() + f' Доп.сведения - {self._extra}'


def object_create(data: list):
    obj = None
    try:
        if data[0] == 'car':
            obj = Car(data[0], data[1], data[5], data[3], data[2])
        elif data[0] == 'truck':
            obj = Truck(data[0], data[1], data[5], data[3], data[4])
        elif data[0] == 'spec_machine':
            obj = SpecMachine(data[0], data[1], data[5], data[3], data[6])
    except ValueError:
        raise

    return obj


def get_car_list(csv_filename: str):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        while True:
            try:
                row = next(reader)
                if row == [] or len(row) != 7:
                    continue
                print(row)
                obj = object_create(row)
                car_list.append(obj)
            except StopIteration:
                break
            except ValueError:
                continue
    return car_list


def main():
    car_list = get_car_list(sys.argv[1])
    for car in car_list:
        print(car)
    # car = Car("car", "Chevrolet", 1.5, "2.jpg", 4)
    # truck = Truck("truck", "Man", 2.5, "1.jpg", "1x2.5x6")
    # print(truck.get_photo_file_ext())
    # print(f"{type(BaseCar.car_types)} - {BaseCar.car_types}")
    # print(car.__dict__)
    # print(truck.__dict__)


if __name__ == '__main__':
    main()
