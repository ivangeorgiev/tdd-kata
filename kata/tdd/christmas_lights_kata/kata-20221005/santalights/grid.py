from typing import List
from .bulb import Bulb


class GridRange:
    r1: int
    c1: int
    r2: int
    c2: int

    def __init__(self, r1, c1, r2, c2):
        self.r1, self.c1 = r1, c1
        self.r2, self.c2 = r2, c2

    def visit(self, visitor, *args, **kwargs):
        for row_number in range(self.r1, self.r2 + 1):
            for column_number in range(self.c1, self.c2 + 1):
                visitor(row_number, column_number, *args, **kwargs)


class BulbGrid:
    bulbs: List[List[Bulb]]

    def __init__(self, width, height):
        self.bulbs = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(Bulb())
            self.bulbs.append(row)

    def visit(self, range_: GridRange, visitor, *args, **kwargs):
        def internal_visitor(row_number, column_number, *args, **kwargs):
            bulb = self.bulbs[row_number][column_number]
            visitor(bulb, *args, **kwargs)

        range_.visit(internal_visitor, *args, **kwargs)
