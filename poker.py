from __future__ import annotations
from typing import List
import random

class Player():
    _name: str
    _money: int
    _cards: List[Card]

    def __init__(self, name: str, money: int) -> None:
        self._set_name(name)
        self._set_init_money(money)
        self._cards = []
    
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
    
    def _action_check(self) -> int:
        return 0
    
    def _action_all_in(self) -> int:
        print("올 인!")
        money = self.money
        self.money = 0 
        return money
    
    def _action_raise(self) -> int:
        money = input("금액을 입력하세요: ")
        self.money -= money
        if self.money <= 0:
            print("소지 금액을 초과하여 올 인합니다.")
            return self.action_all_in(self)
        return money
    
    @property
    def cards(self) -> List[Card]:
        return self._cards
    
    @cards.setter
    def cards(self, cards: List[Card]) -> None:
        self._cards = cards
    
    def receive_card(self, card:Card) -> None:
        self.cards.append(card)
    
    def view_all_cards(self) -> None:
        [print(f"{self.cards.index(x)}번 카드: {x.shape} {x.number}") for x in self.cards]

    @property
    def score(self) -> int:
        return 0
    
    def action(self):
        action_key = input("1: check, 2: raise, 3: all in")
        if not action_key in [1,2,3]:
            action_key = 1
        else:
            action_key -= 1
        actions = [self.action_check(), self.action_raise(), self.action_all_in()]
        return actions[action_key]

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
    
    def hand_out_card(self, cards:List[Card]) -> Card:
        return cards.pop()

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

    
def game(dealer: Dealer, player: Player):
    money = 0

    cards = dealer.set_up_cards()
    
    dealer.shuffle(cards)

    def hand_out_cards():
        player.receive_card(dealer.hand_out_card(cards))
        dealer.receive_card(dealer.hand_out_card(cards))
        player.view_all_cards()

    for _ in range(3):
        hand_out_cards()

    for _ in range(4):
        hand_out_cards()
        betting = player.action()
        betting, sign = dealer.action(betting)
        print(sign)
        money += betting
    
    if player.score >= dealer.score:
        player.money += money
    else:
        dealer.money += money

def main():
    name = input("당신의 이름은?: ")
    player = Player(name)
    dealer = Dealer()

    while dealer.money == 0 or player.money == 0:
        game(dealer, player)


if __name__ == "__main__":
    main()