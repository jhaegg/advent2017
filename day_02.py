import sys
import re

from itertools import permutations

try:
    from functools import reduce
except ImportError:
    pass


def day_02(spreadsheet):
    return sum(a - b for a, b in
               (reduce(lambda (a, b), e: (max(e, a), min(e, b)),
                       row,
                       (-sys.maxint, sys.maxint))
               for row in spreadsheet))


def day_02_part2(spreadsheet):
    return sum(next(a / b for a, b in permutations(row, 2) if a % b == 0 ) for row in spreadsheet)


def parse_2d(f):
    for line in f:
        yield (int(e) for e in filter(lambda e: e != '', re.split("\s+", line)))


if __name__ == '__main__':
    if sys.argv[1] == "1":
        print(day_02(parse_2d(sys.stdin)))
    else:
        print(day_02_part2(parse_2d(sys.stdin)))
