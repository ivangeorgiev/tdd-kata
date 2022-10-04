from santabulbs.bulb import Bulb
from santabulbs.grid import BulbGrid, GridRange
from santabulbs.controller import ImprovedBulbController, SimpleBulbController


class SumAggregate:
    value: int

    def __init__(self):
        self.value = 0

    def visitor(self, bulb: Bulb):
        self.value += bulb.brightness


def apply_instructions(grid, controller):
    grid.visit(GridRange(887, 9, 959, 629), controller.turn_on)
    grid.visit(GridRange(887, 9, 959, 629), controller.turn_on)
    grid.visit(GridRange(887, 9, 959, 629), controller.turn_on)
    grid.visit(GridRange(887, 9, 959, 629), controller.turn_on)
    grid.visit(GridRange(454, 398, 844, 448), controller.turn_on)
    grid.visit(GridRange(539, 243, 559, 965), controller.turn_off)
    grid.visit(GridRange(370, 819, 676, 868), controller.turn_off)
    grid.visit(GridRange(145, 40, 370, 997), controller.turn_off)
    grid.visit(GridRange(301, 3, 808, 453), controller.turn_off)
    grid.visit(GridRange(351, 678, 951, 908), controller.turn_on)
    grid.visit(GridRange(720, 196, 897, 994), controller.toggle)
    grid.visit(GridRange(831, 394, 904, 860), controller.toggle)


controller = SimpleBulbController()
grid = BulbGrid(1000, 1000)
apply_instructions(grid, controller)
sum_aggregate = SumAggregate()
grid.visit(GridRange(0, 0, 999, 999), sum_aggregate.visitor)
print(sum_aggregate.value)

controller = ImprovedBulbController()
grid = BulbGrid(1000, 1000)
apply_instructions(grid, controller)
sum_aggregate = SumAggregate()
grid.visit(GridRange(0, 0, 999, 999), sum_aggregate.visitor)
print(sum_aggregate.value)
