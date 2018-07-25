# Тоже самое только с контекстными менеджерами
import socket


def main():
    with socket.socket() as sock:
        sock.bind(("", 10001))
        sock.listen()

        while True:
            conn, addr = sock.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode("utf8"))


if __name__ == '__main__':
    main()
