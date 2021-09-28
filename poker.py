from __future__ import annotations
from typing import List
import random

class Player():
    _name: str
    _money: int

    def __init__(self, name: str, money: int) -> None:
        self._set_name(name)
        self._set_init_money(money)
    
    def _set_name(self, name) -> None:
        self._name = name
    
    def _set_init_money(self) -> None:
        self.money = 100000
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, money) -> None:
        self._money = money
    
    def action_call(self, money) -> int:
        if self.money <= money:
            return self.action_all_in(self)
        else:
            self.money -= money
        return money
    
    def action_check(self) -> int:
        return 0
    
    def action_all_in(self) -> int:
        money = self.money
        self.money = 0 
        return money
    
    def action_raise(self, money) -> int:
        self.money -= money
        if self.money <= 0:
            return self.action_all_in(self)
        return money

class Dealer(Player):

    def _set_name(self) -> None:
        self._name = "jack"
    
    def _set_init_money(self) -> None:
        self.money = 1000000

    def shuffle(card_deck: List[Card]) -> None:
        random.shuffle(card_deck)
    
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
    
    dealer.shuffle(cards)

if __name__ == "__main__":
    main()