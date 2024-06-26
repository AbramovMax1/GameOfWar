from DeckOfCards1.DeckOfCards import DeckOfCards
from Player1.Player import Player


class CardGame:
    def __init__(self, name1: str, name2: str, amount_of_cards1: int, amount_of_cards2: int):
        if type(name1) != str or type(name2) != str:
            raise TypeError("I accept only str")
        if type(amount_of_cards1) != int or type(amount_of_cards2) != int:
            raise TypeError("I accept only digital numbers")
        """Accept 2 names and amount of cards to each player
         create 2 objects of player with all the info create new deck call the function new game
          and the function shuffle the cards and sort them to each player as we ask"""
        player100 = Player(name1, amount_of_cards1)
        player200 = Player(name2, amount_of_cards2)

        self.player1 = player100
        self.player2 = player200
        self.deck_of_card = DeckOfCards()

        self.new_game()

    def __repr__(self):
        return (f"[{self.player1.name}], Amount of cards in hand :{self.player1.count_of_cards}\n"
                f"and your cards is: {self.player1.list_cards_of_player}\n"
                f"[{self.player2.name}], Amount of cards in hand :{self.player2.count_of_cards}\n"
                f"and your cards is: {self.player2.list_cards_of_player}")

    def new_game(self):
        """function shuffle the deck and sort them to each player randomly"""
        if len(self.deck_of_card.cards) == 52:
            self.deck_of_card.cards_shuffle()
            self.player1.set_hand(self.deck_of_card)
            self.player2.set_hand(self.deck_of_card)
        else:
            raise TypeError("you already used this function")

    def get_winner(self):
        """function return who is the win the game by look who get the most cards in game"""
        if self.player1.count_of_cards > self.player2.count_of_cards:
            return f"{self.player1.name} WINS THIS GAME!!"
        if self.player2.count_of_cards > self.player1.count_of_cards:
            return f"{self.player2.name} WINS THIS GAME"
        if self.player1.count_of_cards == self.player2.count_of_cards:
            return f"TIE no one win!"
