# Тоже самое только с контекстными менеджерами
import socket


def main():
    with socket.create_connection(("127.0.0.1", 10001)) as sock:
        sock.sendall("ping".encode("utf8"))


if __name__ == '__main__':
    main()
