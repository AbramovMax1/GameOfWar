from Card.Card import Card
from random import shuffle
from random import choice


class DeckOfCards:
    def __init__(self):
        """Here we are making deck of cards"""
        self.cards = []
        # The suit are build with 2 index!!!
        list_of_suits = ["♦️", "♣️", "♥️", "♠️"]

        for value in range(1, 14):
            for suit in list_of_suits:

                card = Card(value, suit)
                self.cards.append(card)
        count = 0
        for i in self.cards:
            count += 1
            i.power = count
        # self.cards_shuffle()

    def __str__(self):
        return f"The cards is:{self.cards}"

    def cards_shuffle(self):
        """Here the deck of cards will be shuffled"""
        shuffle(self.cards)

    def deal_one(self):
        pop_card = choice(range(len(self.cards)))
        return self.cards.pop(pop_card)


maxim = DeckOfCards()
print(maxim.cards)
print("\n")
print(maxim.deal_one())
print("\n")
print(maxim.cards)
print("maxim")
