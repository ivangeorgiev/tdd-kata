"""Test bulb module"""

import pytest
from santabulbs.bulb import Bulb


class TestBulbClass:
    def test_can_instantiate_bulb(self):
        bulb = Bulb()
        assert bulb.brightness == 0

    @pytest.mark.parametrize(
        "initial_brightness,expected_brightness", [(0, 0), (1, 1), (-1, 0)]
    )
    def test_can_set_initial_brightness(self, initial_brightness, expected_brightness):
        bulb = Bulb(initial_brightness)
        assert bulb.brightness == expected_brightness
