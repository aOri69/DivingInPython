# Если задачи cpu-bound задачи разбивать на потоки,
# то её итоговое время увеличится из-за GIL

from threading import Thread
import time


def count(n):
    while n > 0:
        n -= 1


def main():
    # Series run
    t0 = time.time()
    count(100_000_000)
    count(100_000_000)
    print(time.time()-t0)

    # Parallel run
    t0 = time.time()
    th1 = Thread(target=count, args=(100_000_000,))
    th2 = Thread(target=count, args=(100_000_000,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(time.time()-t0)

# Результаты без потоков
# 508.69724011421204
# Результаты с потоками
# 511.90980052948


if __name__ == '__main__':
    main()
