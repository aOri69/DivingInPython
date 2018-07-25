import socket


def main():
    # Таймаут только на установку соединения
    with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
        # set socket read
        sock.settimeout(2)
        try:
            sock.sendall("ping".encode("utf8"))
        except socket.timeout:
            print("timeout sending")
        except socket.error as exc:
            print("error sending", exc)


if __name__ == '__main__':
    main()
