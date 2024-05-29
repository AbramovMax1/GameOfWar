from DeckOfCards.DeckOfCards import DeckOfCards
from Card.Card import Card


class Player:
    def __init__(self, name: str, count_of_cards: int):
        self.name = name
        self.list_cards_of_player = []
        self.count_of_cards = count_of_cards
        if self.count_of_cards > 26 or self.count_of_cards < 10:
            self.count_of_cards = 26

    def __str__(self):
        return f"name :{self.name}\nyour cards :{self.list_cards_of_player}"

    def __repr__(self):
        return f"name"

    def set_hand(self, deck: DeckOfCards):
        for i in range(self.count_of_cards):
            picked_card = deck.deal_one()
            self.list_cards_of_player.append(picked_card)

    def get_card(self):
        pass

    def add_card(self):
        pass


d = DeckOfCards()
maxim = Player("Maxim", 12)
maxim.set_hand(d)
print(maxim)

