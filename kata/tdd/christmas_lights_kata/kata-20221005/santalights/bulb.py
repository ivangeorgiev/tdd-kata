from abc import ABC, abstractmethod


class Bulb:
    _brightness: int = 0

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value if value > 0 else 0


class BulbController(ABC):
    @abstractmethod
    def turn_on(self, bulb: Bulb):
        ...

    @abstractmethod
    def turn_off(self, bulb: Bulb):
        ...


class SimpleBulbController(BulbController):
    min_brightness = 0
    max_brightness = 1
    turn_on_expression = lambda self, bulb: bulb.brightness + 1
    turn_off_expression = lambda self, bulb: bulb.brightness - 1
    toggle_expression = lambda self, bulb: 0 if bulb.brightness > 0 else 1

    def turn_on(self, bulb: Bulb):
        brightness = self.turn_on_expression(bulb)
        bulb.brightness = self.adjust_brightness(brightness)

    def turn_off(self, bulb: Bulb):
        brightness = self.turn_off_expression(bulb)
        bulb.brightness = self.adjust_brightness(brightness)

    def toggle(self, bulb: Bulb):
        brightness = self.toggle_expression(bulb)
        bulb.brightness = self.adjust_brightness(brightness)

    def adjust_brightness(self, brightness):
        if brightness < self.min_brightness:
            return self.min_brightness
        if brightness > self.max_brightness:
            return self.max_brightness
        return brightness
