"""Test cases for controller module"""
import pytest
from santabulbs.controller import BulbController, SimpleBulbController
from santabulbs.bulb import Bulb


class TestSimpleBulbControllerClass:
    def test_can_create_instance(self):
        controller = SimpleBulbController()
        assert isinstance(controller, BulbController)

    @pytest.mark.parametrize("initial_brightness,final_brightness", [(0, 1), (1, 1)])
    def test_can_turn_bulb_on(self, initial_brightness, final_brightness):
        bulb = Bulb(initial_brightness)
        controller = SimpleBulbController()
        controller.turn_on(bulb)
        assert bulb.brightness == final_brightness

    @pytest.mark.parametrize("initial_brightness,final_brightness", [(0, 0), (1, 0)])
    def test_can_turn_bulb_off(self, initial_brightness, final_brightness):
        bulb = Bulb(initial_brightness)
        controller = SimpleBulbController()
        controller.turn_off(bulb)
        assert bulb.brightness == final_brightness

    @pytest.mark.parametrize("initial_brightness,final_brightness", [(0, 1), (1, 0)])
    def test_can_toggle_bulb(self, initial_brightness, final_brightness):
        bulb = Bulb(initial_brightness)
        controller = SimpleBulbController()
        controller.toggle(bulb)
        assert bulb.brightness == final_brightness
