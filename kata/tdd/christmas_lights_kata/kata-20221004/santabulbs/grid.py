from typing import List
from .bulb import Bulb
from .controller import BulbController, SimpleBulbController


class GridRange:
    r1: int
    c1: int
    r2: int
    c2: int

    def __init__(self, r1: int, c1: int, r2: int, c2: int):
        self.r1, self.c1 = (r1, c1)
        self.r2, self.c2 = (r2, c2)

    def items(self):
        for row_number in range(self.r1, self.r2 + 1):
            for column_number in range(self.c1, self.c2 + 1):
                yield (row_number, column_number)


class BulbGrid:
    width: int
    height: int
    controller: BulbController
    bulbs: List[List[Bulb]]

    def __init__(self, width: int, height: int, controller: BulbController = ...):
        self.width = width
        self.height = height
        self.controller = SimpleBulbController() if controller is ... else controller
        self.bulbs = [None] * height
        for row_number in range(height):
            row = [None] * width
            self.bulbs[row_number] = row
            for column_number in range(width):
                row[column_number] = Bulb()

    def visit(self, range: GridRange, apply, *args, **kwargs):
        for row_number, column_number in range.items():
            bulb = self.bulbs[row_number][column_number]
            apply(bulb, *args, **kwargs)
