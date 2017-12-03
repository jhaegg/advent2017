from unittest import TestCase
from day_01 import day_01

class TestDay01(TestCase):
    def test_sum_consecutive(self):
        self.assertEqual(3, day_01("1122", -1))

    def test_sum_multiple(self):
        # Replacement for example 2, this one does not assume wraparound
        self.assertEqual(2, day_01("1112", -1))

    def test_none(self):
        self.assertEqual(0, day_01("1234", -1))

    def test_wraparound(self):
        self.assertEqual(9, day_01("91212129", -1))
        self.assertEqual(4, day_01("1111", -1))

    def test_part2(self):
        self.assertEqual(6, day_01("1212", 2))
        self.assertEqual(0, day_01("1221", 2))
        self.assertEqual(4, day_01("123425", 3))
        self.assertEqual(12, day_01("123123", 3))
        self.assertEqual(4, day_01("12131415", 4))
