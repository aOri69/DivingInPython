import unittest


def fib(n: int) -> int:
    """
    fib
    """
    if not isinstance(n, int) or n < 0:
        raise ArithmeticError
    f = [0, 1] + [0] * (n - 1)
    for i in range(2, n-1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


class TestFib(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def tets_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib(n), fib_n)

    def test_positive(self):
        self.assertEqual(fib(10), 55)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -1)
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -10)


if __name__ == '__main__':
    unittest.main()
