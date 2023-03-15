import pytest
from santalights.bulb import Bulb, SimpleBulbController


class TestBulbClass:
    def test_can_create_bulb_instance(self):
        bulb = Bulb()
        assert bulb.brightness == 0

    def test_can_set_brightness(self):
        bulb = Bulb()
        bulb.brightness = 11
        assert bulb.brightness == 11

    def test_setting_brightness_below_zero_resets_to_zero(self):
        bulb = Bulb()
        bulb.brightness = -5
        assert bulb.brightness == 0


class TestSimpleBulbControllerClass:
    def test_can_create_simplebulbcontroller(self):
        controller = SimpleBulbController()
        assert isinstance(controller, SimpleBulbController)

    @pytest.mark.parametrize(
        "target_brightness,expected_brightness", [(0, 0), (1, 1), (2, 1), (-1, 0)]
    )
    def test_adjust_brightness_retruns_value_within_range(
        self, target_brightness, expected_brightness
    ):
        controller = SimpleBulbController()
        assert controller.adjust_brightness(target_brightness) == expected_brightness

    @pytest.mark.parametrize("initial_brightness,expected_brightness", [(0, 1), (1, 1)])
    def test_can_turn_on(self, initial_brightness, expected_brightness):
        controller = SimpleBulbController()
        bulb = Bulb()
        bulb.brightness = initial_brightness
        controller.turn_on(bulb)
        assert bulb.brightness == expected_brightness

    @pytest.mark.parametrize("initial_brightness,expected_brightness", [(0, 0), (1, 0)])
    def test_can_turn_off(self, initial_brightness, expected_brightness):
        controller = SimpleBulbController()
        bulb = Bulb()
        bulb.brightness = initial_brightness
        controller.turn_off(bulb)
        assert bulb.brightness == expected_brightness

    @pytest.mark.parametrize("initial_brightness,expected_brightness", [(0, 1), (1, 0)])
    def test_toggle(self, initial_brightness, expected_brightness):
        controller = SimpleBulbController()
        bulb = Bulb()
        bulb.brightness = initial_brightness
        controller.toggle(bulb)
        assert bulb.brightness == expected_brightness
