# Вызываем корутины из корутин)


def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_py_coroutine():
    g = grep("python")
    yield from g


def main():
    g = grep_py_coroutine()
    g.send(None)
    g.send("python wow!")


if __name__ == '__main__':
    main()
