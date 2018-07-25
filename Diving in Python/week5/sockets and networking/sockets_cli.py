# Создание сокета, клиент
import socket


def main():
    # Длинная запись
    sock = socket.socket()
    sock.connect(("127.0.0.1", 10001))
    sock.sendall("ping".encode("utf8"))
    sock.close()
    # Короткая запись
    sock = socket.create_connection(("127.0.0.1", 10001))
    sock.sendall("ping".encode("utf8"))
    sock.close()


if __name__ == '__main__':
    main()
