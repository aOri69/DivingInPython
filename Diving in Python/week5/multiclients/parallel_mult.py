"""Здесь выполним в отдельных процессах а не потоках"""
import os
import socket
import threading
from multiprocessing import Process


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


def worker(sock):
    """Каждый рабочий будет в отдельном процессе получая входящее соединение
    и создаем поток"""
    while True:
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


def main():
    # Создаем сокет
    with socket.socket() as sock:
        sock.bind(("", 10001))
        sock.listen()
        # Количество процессов
        workers_count = 3
        # В каждый процесс запихиваем
        workers_list = [Process(target=worker, args=(sock,))
                        for _ in range(workers_count)]

        for w in workers_list:
            w.start()
        for w in workers_list:
            w.join()


if __name__ == '__main__':
    main()


# def main():
#     with socket.socket() as sock:
#         sock.bind(("", 10001))
#         sock.listen()
#         # Creating new processes
#         while True:
#             # accept распределится "равномерно" между процессами
#             conn, addr = sock.accept()
#             # поток для обработки соединения
#             with conn:
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     print(data.decode("utf8"))


# if __name__ == '__main__':
#     main()
