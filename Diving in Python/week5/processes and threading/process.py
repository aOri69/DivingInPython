# Создание процесса на Python3
# Тоже самое и с файловыми дескрипторами
import time
import os
from multiprocessing import Process


def f(name):
    print('Hello', name)


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Hello', self.name)


# foo = 'bar'
# pid = os.fork()

# if pid == 0:
#     # Код будет выполнен дочерним процессом
#     print("child: {}".format(os.getpgid()))
#     foo = 'baZ'
#     print("child: {}".format(foo))
#     time.sleep(5)
# else:
#     # Родительский процесс, у него ПИД будет
#     print("parent: {}".format(os.getpgid()))
#     print("parent: {}".format(foo))
#     os.wait()
if __name__ == '__main__':
    # Способ 1
    p = Process(target=f, args=('Bob',))
    p.start()
    p.join()
    # Способ 2, унаследовавшись от класса Process
    p = PrintProcess('Mike')
    p.start()
    p.join()
