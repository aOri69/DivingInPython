import unittest


class TestPython(unittest.TestCase):
    def test_float_to_int_correction(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_key(self):
        self.assertIsNone({}.get('key'))

    def tets_true(self):
        self.assertTrue(bool(1))


class TestDivision(unittest.TestCase):
    def test_div(self):
        self.assertIs(10/5, 2)
# Запускаем так: python -m unittest test.py
