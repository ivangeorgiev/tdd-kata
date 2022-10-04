from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List
from .base import BULB_ON, BULB_OFF


class Range:
    r1: int
    c1: int
    r2: int
    c2: int

    def __init__(self, r1: int, c1: int, r2: int = ..., c2: int = ...):
        self.r1, self.c1 = (r1, c1)
        self.r2, self.c2 = (r1 if r2 is ... else r2, c1 if c2 is ... else c2)

    @property
    def bulbs(self):
        for row_number in range(self.r1, self.r2 + 1):
            for column_number in range(self.c1, self.c2 + 1):
                yield (row_number, column_number)

    def apply(
        self,
        callback: Callable[[int, int], None],
        *args: List[Any],
        **kwargs: Dict[Any, Any]
    ):
        for row_number, column_number in self.bulbs:
            callback(row_number, column_number, *args, **kwargs)


class BulbOperator(ABC):
    @abstractmethod
    def turn_on(self, current_state):
        ...


class BulbOperatorV1(BulbOperator):
    def turn_on(self, bulb_state):
        return BULB_ON

    def turn_off(self, bulb_state):
        return BULB_OFF

    def toggle(self, bulb_state):
        return BULB_OFF if bulb_state == BULB_ON else BULB_ON


class BulbOperatorV2(BulbOperator):
    def turn_on(self, bulb_state):
        return bulb_state + 1

    def turn_off(self, bulb_state):
        return bulb_state - 1 if bulb_state > BULB_OFF else BULB_OFF

    def toggle(self, bulb_state):
        return bulb_state + 2


class Grid:
    height: int
    width: int
    operator: BulbOperator

    def __init__(self, width: int, height: int, operator: BulbOperator = ...):
        self.width = width
        self.height = height
        self.operator = BulbOperatorV1() if operator is ... else operator
        self._bulb_states = [None] * height
        for row_number in range(height):
            self._bulb_states[row_number] = [BULB_OFF] * width

    def get_bulb_state(self, row: int, col: int):
        return self._bulb_states[row][col]

    def turn_on(self, row: int, col: int):
        current_state = self.get_bulb_state(row, col)
        self._bulb_states[row][col] = self.operator.turn_on(current_state)

    def turn_off(self, row: int, col: int):
        current_state = self.get_bulb_state(row, col)
        self._bulb_states[row][col] = self.operator.turn_off(current_state)

    def toggle(self, row: int, col: int):
        current_state = self._bulb_states[row][col]
        self._bulb_states[row][col] = self.operator.toggle(current_state)
