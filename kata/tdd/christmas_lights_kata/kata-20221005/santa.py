from santalights.grid import BulbGrid, GridRange
from santalights.bulb import BulbController, SimpleBulbController


def get_visitor(operation: str, grid: BulbGrid, controller: BulbController):
    def visitor(row_number, column_number):
        bulb = grid.bulbs[row_number][column_number]
        operation_method(bulb)

    operation_method = getattr(controller, operation)
    return visitor


def sum_brightness(grid: BulbGrid):
    class IntValue:
        value: int = 0

    def sum_visitor(bulb, result):
        result.value += bulb.brightness

    result = IntValue()
    grid.visit(GridRange(0, 0, 999, 999), sum_visitor, result)
    return result.value


def apply_santa_instructions(grid: BulbGrid, controller: SimpleBulbController):
    grid.visit(GridRange(887, 9, 959, 629), controller.turn_on)
    grid.visit(GridRange(454, 398, 844, 448), controller.turn_on)
    grid.visit(GridRange(539, 243, 559, 965), controller.turn_off)
    grid.visit(GridRange(370, 819, 676, 868), controller.turn_off)
    grid.visit(GridRange(145, 40, 370, 997), controller.turn_off)
    grid.visit(GridRange(301, 3, 808, 453), controller.turn_off)
    grid.visit(GridRange(351, 678, 951, 908), controller.turn_on)
    grid.visit(GridRange(720, 196, 897, 994), controller.toggle)
    grid.visit(GridRange(831, 394, 904, 860), controller.toggle)


grid = BulbGrid(1000, 1000)
controller = SimpleBulbController()
apply_santa_instructions(grid, controller)
print(sum_brightness(grid))

grid = BulbGrid(1000, 1000)
controller = SimpleBulbController()
controller.max_brightness = 100000
controller.toggle_expression = lambda bulb: bulb.brightness + 2
apply_santa_instructions(grid, controller)
print(sum_brightness(grid))
