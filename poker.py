from __future__ import annotations

import random


class Dealer():

    def shuffle() -> Card:
        shapes = ["spade", "heart", "diamond", "clover"]
        card_shape = shapes[random.randint(3)]
        card_number = random.randrange(1,13)
        return Card(card_shape, card_number)

class Card():
    _shape: str
    _number: int

    def __init__(self, shape, number) -> None:
        self._shape = shape
        self._number = number
    
    @property
    def shape(self) -> str:
        return self._shape

    @property
    def number(self) -> int:
        return self._number
