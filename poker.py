from __future__ import annotations
from typing import List
import random


class Dealer():

    def shuffle(card_deck) -> List[Card]:
        random.shuffle(card_deck)
        return card_deck
    
    def set_up_cards(self) -> List[Card]:
        card_types = ["spade", "heart", "diamond", "clover"]
        cards = [Card(t, i) for t in card_types for i in range(1, 14)]    
        return cards

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

def main():
    dealer = Dealer()
    cards = dealer.set_up_cards()
    print(len(cards))

if __name__ == "__main__":
    main()