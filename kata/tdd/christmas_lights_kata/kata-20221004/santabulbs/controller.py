from abc import ABC, abstractmethod
from .bulb import Bulb


class BulbController(ABC):
    @abstractmethod
    def turn_on(self, bulb: Bulb):
        ...

    @abstractmethod
    def turn_off(self, bulb: Bulb):
        ...

    @abstractmethod
    def toggle(self, bulb: Bulb):
        ...


class SimpleBulbController(BulbController):
    def turn_on(self, bulb: Bulb):
        bulb.brightness = 1

    def turn_off(self, bulb: Bulb):
        bulb.brightness = 0

    def toggle(self, bulb: Bulb):
        bulb.brightness = 0 if bulb.brightness > 0 else 1


class ImprovedBulbController(BulbController):
    def turn_on(self, bulb: Bulb):
        bulb.brightness += 1

    def turn_off(self, bulb: Bulb):
        if bulb.brightness > 0:
            bulb.brightness -= 1
        else:
            bulb.brightness = 0

    def toggle(self, bulb: Bulb):
        bulb.brightness += 2
