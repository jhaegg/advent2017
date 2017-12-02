from unittest import TestCase
from day_02 import day_02, parse_2d
from textwrap import dedent

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class TestDay02(TestCase):
    def test_day_02(self):
        example = ((5, 1, 9, 5),
                   (7, 5, 3),
                   (2, 4, 6, 8))

        self.assertEqual(18, day_02(example))

    def test_the_boring_parts(self):
        example = dedent("""\
                            5\t1 9 5\t
                            7 5 3
                            2 4 6 8""")

        expected = ((5, 1, 9, 5),
                    (7, 5, 3),
                    (2, 4, 6, 8))

        try:
            f = StringIO(example)
        except TypeError:
            f = StringIO(unicode(example))

        result = parse_2d(f)

        for expected_line in expected:
            self.assertEqual(expected_line, tuple(next(result)))

        with self.assertRaises(StopIteration):
            next(result)
