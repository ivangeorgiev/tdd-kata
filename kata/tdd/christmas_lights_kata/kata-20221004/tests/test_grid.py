"""Test cases for grid module"""
import pytest
from santabulbs.bulb import Bulb
from santabulbs.controller import BulbController, SimpleBulbController
from santabulbs.grid import BulbGrid, GridRange


class TestGridRangeClass:
    def test_can_instantiate(self):
        range_ = GridRange(1, 2, 3, 4)
        assert (range_.r1, range_.c1, range_.r2, range_.c2,) == (
            1,
            2,
            3,
            4,
        )

    @pytest.mark.parametrize(
        "rangeargs, expected",
        [((1, 2, 2, 4), [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)])],
    )
    def test_items(self, rangeargs, expected):
        range_ = GridRange(*rangeargs)
        assert list(range_.items()) == expected


class TestBulbGridClass:
    def test_can_instantiate(self):
        grid = BulbGrid(5, 10)
        assert grid.width == 5
        assert grid.height == 10
        assert isinstance(grid.controller, BulbController)
        assert isinstance(grid.controller, SimpleBulbController)
        assert len(grid.bulbs) == 10
        for row_number in range(10):
            row = grid.bulbs[row_number]
            assert len(row) == 5
            for column_number in range(5):
                bulb = row[column_number]
                assert isinstance(bulb, Bulb)
                assert bulb.brightness == 0

    def test_visit(self):
        def visitor(bulb: Bulb, *args, **kwargs):
            visited.append((bulb, args, kwargs))

        grid = BulbGrid(10, 5)
        visited = []
        args = tuple("arg")
        kwargs = {"kwarg": "value"}
        grid.visit(GridRange(1, 1, 1, 2), visitor, *args, **kwargs)
        assert visited == [
            (grid.bulbs[1][1], args, kwargs),
            (grid.bulbs[1][2], args, kwargs),
        ]
