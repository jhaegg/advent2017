from unittest import TestCase
from day_02 import day_02
from textwrap import dedent

class TestDay02(TestCase):
    def test_day_02(self):
        example = ((5, 1, 9, 5),
                   (7, 5, 3),
                   (2, 4, 6, 8))

        self.assertEqual(18, day_02(example))
