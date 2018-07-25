"""
Иерархия исключений
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
    +-- Exception
    +-- StopIteration
    +-- AssertionError
    +-- AttributeError
    +-- LookupError
        +-- IndexError
        +-- KeyError
    +-- OSError
    +-- SystemError
    +-- TypeError
    +-- ValueError
    Обработка исключений
    try:
        1/0
    except: Ловит все исключения
        print("err")
"""


def _main():
    # Обработка нескольких исключений
    total = 0
    while True:
        try:
            raw = input("Enter the number: ")
            number = int(raw)
            total = total / number
            break
        except (ValueError, ZeroDivisionError):
            print("Incorrect input")
        except KeyboardInterrupt:
            print("exiting...")
            break

    # Несколько исключений с помощью наследования
    # +--LookupError
    #     +--IndexError
    #     +--KeyError
    # При помощи родительского класса можно ловить все искл. наследников
    print(issubclass(KeyError, LookupError))
    print(issubclass(IndexError, LookupError))
    database = {
        "red": ["fox", "flower"],
        "green": ["peace", "M", "python"]
    }
    try:
        color = input("Enter color: ")
        number = input("Enter the number of the order: ")

        label = database[color][int(number)]
        print("U've choose: ", label)
    # except (IndexError,KeyError):
    except LookupError:
        print("There's no such object")

    # Блок FINALLY
    f = open("file.txt")
    try:
        for line in f:
            print(line.strip("\n"))
            1/0
    except OSError:
        print("err")
    # Все равно выполнится и закроет файл(но лучше конечно файловый дескриптор)
    finally:
        f.close()


if __name__ == "__main__":
    _main()
