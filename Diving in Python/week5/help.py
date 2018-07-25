"""
Это вспомогательный скрипт для тестирования сервера из задания на неделе 6.

Для запуска скрипта на локальном компьютере разместите рядом файл client.py,
где содержится код клиента, который открывается по прохождении задания
недели 5.

Сначала запускаете ваш сервер на адресе 127.0.0.1 и порту 8888, а затем
запускаете этот скрипт.
"""
import sys
import random
from client import Client, ClientError


def run(host, port):
    client_list = [Client(host, port) for _ in range(100)]

    try:
        for client in client_list:
            client.put("Cli", random.randint(1, 50))
        for client in client_list:
            client.get('*')
    except ClientError as err:
        print(f"Ошибка вызова client.put(...) {err.__class__}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    run("127.0.0.1", 8181)
