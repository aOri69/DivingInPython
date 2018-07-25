import json
import unittest
from unittest.mock import patch

from asteroid import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        # Устанавливаем окружение для выполнения тестовых функций
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        with open("apophis_fix.txt") as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(self.asteroid.name, '99942 Apophis (2004 MN4)')

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)
