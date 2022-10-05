from santalights.grid import BulbGrid, GridRange


class TestGridRangeClass:
    def test_can_create_gridrange_instance(self):
        range = GridRange(1, 2, 3, 4)
        assert (range.r1, range.c1, range.r2, range.c2) == (1, 2, 3, 4)

    def test_can_visit_each_bulb(self):
        def visitor(r, c, *args, **kwargs):
            visited.append((r, c, args, kwargs))

        range_ = GridRange(1, 2, 2, 3)
        args = ()
        kwargs = {}
        visited = []
        range_.visit(visitor, *args, **kwargs)
        assert visited == [
            (1, 2, args, kwargs),
            (1, 3, args, kwargs),
            (2, 2, args, kwargs),
            (2, 3, args, kwargs),
        ]


class TestBulbGridClass:
    def test_can_create_bulbgrid_instance(self):
        grid = BulbGrid(3, 5)
        assert len(grid.bulbs) == 5
        assert len(grid.bulbs[0]) == 3

    def test_visit_visits_all_bulbs(self):
        def visitor(bulb, *args, **kwargs):
            visited.append((bulb, args, kwargs))

        visited = []
        grid = BulbGrid(10, 10)
        args = ()
        kwargs = {}
        grid.visit(GridRange(1, 2, 1, 3), visitor)
        expected = [(grid.bulbs[1][2], args, kwargs), (grid.bulbs[1][3], args, kwargs)]
        assert visited == expected
