class Bulb:
    _brightness: int

    def __init__(self, brightness: int = 0):
        self.brightness = brightness

    @property
    def brightness(self) -> int:
        return self._brightness

    @brightness.setter
    def brightness(self, value: int):
        self._brightness = 0 if value < 0 else value
