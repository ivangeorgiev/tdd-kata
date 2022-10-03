import pytest
from christmas_lights.grid import Grid


def assert_grid_size(grid: Grid, width: int, height: int):
    __tracebackhide__ = True
    errors = []
    if grid.width != width:
        errors.append(f"grid width {grid.width} != {width}")
    if grid.height != height:
        errors.append(f"grid heigh {grid.height} != {height}")
    if errors:
        pytest.fail("Comparing Grid size:\n" + "\n".join(f"   {err}" for err in errors))
