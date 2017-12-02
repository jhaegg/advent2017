import sys

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
