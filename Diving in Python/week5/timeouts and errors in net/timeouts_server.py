import socket


def main():
    with socket.socket() as sock:
        sock.bind(("", 10001))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            # timeout := None|0|gt 0 - 0 Это неблокирующий режим
            conn.timeout('5')  # Странно но сюда ничего не записывается
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                    except sock.timeout:
                        print("closed connection by timout")
                        break

                    if not data:
                        break
                    print(data.decode("utf8"))


if __name__ == '__main__':
    main()
