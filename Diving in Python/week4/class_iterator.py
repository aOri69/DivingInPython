class SquareIterator:
    """Вариант обычного итератора"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):  # Должен возвращать итератор в себя
        return self

    def __next__(self):  # Определяет какие элементы возвращаются во время итераций
        if self.current >= self.end:
            raise StopIteration
        result = self.current**2
        self.current += 1
        return result


class IndexIterable:
    """Вариант итератора-контейнера"""

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


if __name__ == '__main__':
    for num in SquareIterator(1, 4):
        print(num)
    for letter in IndexIterable('abcdefg'):
        print(letter)
