from DeckOfCards1.DeckOfCards import DeckOfCards
from Card1.Card import Card
from random import choice


class Player:
    def __init__(self, name: str, count_of_cards: int):
        """make a player with name and amount of cards
         if the amount under 10 or above 26 it's will give automatically will give you 26 card
         and the init have the list cards of players"""
        self.name = name
        self.list_cards_of_player = []
        self.count_of_cards = count_of_cards
        if self.count_of_cards > 26 or self.count_of_cards < 10:
            self.count_of_cards = 26

        if type(self.name) != str:
            raise TypeError("need to be str!")
        if type(self.count_of_cards) != int:
            raise TypeError("need to be int!")

    def __str__(self):
        return f"Player name :{self.name}\nyou have {self.count_of_cards} cards :{self.list_cards_of_player}"

    def __repr__(self):
        return f"Player name :{self.name} you have {self.count_of_cards} cards cards :{self.list_cards_of_player}"

    def set_hand(self, deck: DeckOfCards):
        """Create deck to player from the deck he got According to the quantity required in the initial"""
        if type(deck) == int:
            raise TypeError("it's not deck of cards")
        if type(deck) == str:
            raise TypeError("it's not deck of cards")
        if type(deck) == DeckOfCards:
            for i in range(self.count_of_cards):
                picked_card = deck.deal_one()
                self.list_cards_of_player.append(picked_card)

    def get_card(self):
        """Takes out a random card in the player's deck and calculates the amount accordingly"""
        self.count_of_cards -= 1
        pop_card = choice(range(len(self.list_cards_of_player)))
        return self.list_cards_of_player.pop(pop_card)

    def add_card(self, card: Card):
        """Gets a card object, adds it to the player's deck and calculates it by the player's amount of cards"""
        if type(card) != Card:
            raise TypeError("I only get a card object")
        self.count_of_cards += 1
        self.list_cards_of_player.append(card)
