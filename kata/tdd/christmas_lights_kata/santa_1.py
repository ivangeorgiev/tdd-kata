from christmas_lights.base import BULB_ON
from christmas_lights.grid import BulbOperatorV2, Grid, Range


class CountAggregate:
    count: int = 0

    def __call__(self, row_number, column_number, getter):
        if getter(row_number, column_number) == BULB_ON:
            self.count += 1


class SumAggregate:
    value: int = 0

    def __call__(self, row_number, column_number, getter):
        self.value += getter(row_number, column_number)


def apply_instructions(grid):
    Range(887, 9, 959, 629).apply(grid.turn_on)
    Range(454, 398, 844, 448).apply(grid.turn_on)
    Range(539, 243, 59, 965).apply(grid.turn_off)
    Range(370, 819, 676, 868).apply(grid.turn_off)
    Range(145, 40, 370, 997).apply(grid.turn_off)
    Range(301, 3, 808, 453).apply(grid.turn_off)
    Range(351, 678, 951, 908).apply(grid.turn_on)
    Range(720, 196, 897, 994).apply(grid.toggle)
    Range(831, 394, 904, 860).apply(grid.toggle)


grid1 = Grid(1000, 1000)
apply_instructions(grid1)
sum_aggregate = SumAggregate()
Range(0, 0, 999, 999).apply(sum_aggregate, grid1.get_bulb_state)
print("Result from classic instructions: ", sum_aggregate.value)

grid2 = Grid(1000, 1000, BulbOperatorV2())
apply_instructions(grid2)
sum_aggregate = SumAggregate()
Range(0, 0, 999, 999).apply(sum_aggregate, grid2.get_bulb_state)
print("Result from modern instructions: ", sum_aggregate.value)
