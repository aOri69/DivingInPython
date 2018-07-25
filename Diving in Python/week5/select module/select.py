import socket
import select


def main():
    sock = socket.socket()
    sock.bind(("", 10001))
    sock.listen()

    # Как обработать запросы для кон1 и кон2
    # Одновременно без потоков?
    conn1, addr = sock.accept()
    conn2, addr = sock.accept()

    conn1.setblocking(0)
    conn2.setblocking(0)

    sel = select.select()


if __name__ == '__main__':
    main()
