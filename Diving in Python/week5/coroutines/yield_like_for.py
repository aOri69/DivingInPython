def chain(x_iter, y_iter):
    yield from x_iter
    yield from y_iter


def the_same_chain(x_iter, y_iter):
    for x in x_iter:
        yield x
    for y in y_iter:
        yield y


def main():
    a = [1, 2, 3]
    b = (4, 5)
    for x in chain(a, b):
        print(x)


if __name__ == '__main__':
    main()
