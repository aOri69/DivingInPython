# Сопрограммы (корутины)


def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield  # Функция замораживает свое состояние
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("grep closed")
    except RuntimeError as exc:
        print("why U stop me?", exc.args)


def main():
    g = grep("python")
    next(g)  # g.send(None)
    # Код корутины запустится только после некст, чтобы заморозить свое состояние на yield
    g.send("golang is better?")
    g.send("python is simple!")
    g.throw(RuntimeError, "something gone wrong")
    g.close()  # Если надо самим останоить корутину


if __name__ == '__main__':
    main()
