from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


# shutdown() in exit
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [pool.submit(f, i) for i in range(1000)]
        for future in as_completed(results):
            print(future.result())
