import pytest
from christmas_lights.grid import Grid, Range
from christmas_lights.base import BULB_OFF, BULB_ON

from .asserts import assert_grid_size


class TestGridClass:
    def test_can_create_grid(self):
        grid = Grid(10, 10)
        assert_grid_size(grid, 10, 10)

    @pytest.mark.parametrize("row,column", [(0, 0), (2, 3), (9, 9)])
    def test_bulb_is_off_by_default(self, row, column):
        grid = Grid(10, 10)
        assert grid.get_bulb_state(row, column) == BULB_OFF

    @pytest.mark.parametrize("row,column", [(0, 0), (2, 3), (9, 9)])
    def test_turn_on_sets_bulb_on(self, row, column):
        grid = Grid(10, 10)
        grid.turn_on(row, column)
        assert grid.get_bulb_state(row, column) == BULB_ON

    @pytest.mark.parametrize("row,column", [(0, 0), (2, 3), (9, 9)])
    def test_turn_off_sets_bulb_off(self, row, column):
        grid = Grid(10, 10)
        grid.turn_off(row, column)
        assert grid.get_bulb_state(row, column) == BULB_OFF

    @pytest.mark.parametrize(
        "row,column,turn_on,expect", [(0, 0, True, BULB_OFF), (2, 3, False, BULB_ON)]
    )
    def test_given_bulb_is_on_toggle_turns_bulb_off(self, row, column, turn_on, expect):
        grid = Grid(10, 10)
        if turn_on:
            grid.turn_on(row, column)
        grid.toggle(row, column)
        assert grid.get_bulb_state(row, column) == expect


class TestRangeClass:
    def test_init_sets_r2_equal_to_r1_when_r1_is_not_specified(self):
        range_ = Range(1, 5)
        assert range_.r2 == range_.r1

    def test_init_sets_c2_equal_to_c1_when_c1_is_not_specified(self):
        range_ = Range(1, 5)
        assert range_.c2 == range_.c1

    @pytest.mark.parametrize(
        "r1,c1,r2,c2,expect",
        [
            (0, 0, 0, 0, [(0, 0)]),
            (0, 0, 1, 1, [(0, 0), (0, 1), (1, 0), (1, 1)]),
        ],
    )
    def test_bulb_returns_bulb_indexes(self, r1, c1, r2, c2, expect):
        range_ = Range(r1, c1, r2, c2)
        assert list(range_.bulbs) == expect

    def test_apply_calls_callback_for_each_bulb(self):
        def callback(row_number, column_number):
            called_with.append((row_number, column_number))

        called_with = []
        Range(1, 1, 2, 3).apply(callback)
        assert called_with == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]

    def test_apply_passes_arguments(self):
        def callback(*args, **kwargs):
            called_with.append((args, kwargs))

        called_with = []
        Range(1, 1, 1, 1).apply(callback, "arg", kwarg="value")
        assert called_with == [
            (
                (
                    1,
                    1,
                    "arg",
                ),
                {"kwarg": "value"},
            )
        ]
