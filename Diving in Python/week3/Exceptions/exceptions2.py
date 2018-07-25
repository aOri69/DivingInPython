# Производительность работы исключений низкая
# Доступ к объекту исключений
try:
    with open("file.txt") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)

# Доступ к объекту исключений через атрибут args
import os.path
filename = "file.txt"
try:
    if not os.path.exists(filename):
        raise ValueError("File not exists", filename)
except ValueError as err:
    print("Incorrect file: ", err.args[0], err.args[1])

# Доступ к стеку вызовов
import traceback
try:
    with open("file.txt") as f:
        content = f.read()
except OSError as err:
    trace_back = traceback.print_exc()
    print(trace_back)

# Делегирование обработки исключений "выше"
try:
    with open("file.txt") as f:
        content = f.read()
except OSError as err:
    print("err")
    # raise

# Если делегирований много, то можно использовать raise from Exception
try:
    raw = 'ass'
    if not raw.isdigit():
        raise ValueError("bad number", raw)
except ValueError as err:
    print("err", err.args[0], err.args[1])
    #raise TypeError("Error") from err

# Инструкция assert чисто такая для программистов
# assert True
# assert 1 == 0


def get_user(id):
    assert isinstance(id, int), "id должен быть числом"
    print("Выполняем поиск")


# Если при запуске добавить флаг -O, то все assert будут пропущены
get_user("foo")
