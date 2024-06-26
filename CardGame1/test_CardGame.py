from unittest import TestCase
from CardGame1.CardGame import CardGame
from DeckOfCards1.DeckOfCards import DeckOfCards
from Player1.Player import Player


class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("max", "shirel", 26, 26)
        self.player1 = self.game.player1
        self.player2 = self.game.player2
        self.Deck = self.game.deck_of_card
        self.deck2 = DeckOfCards()

    def test_init_valid(self):
        # checking if name is str
        self.assertEqual(str, type(self.game.player1.name))

    def test_init_valid2(self):
        # checking if name2 is str
        self.assertEqual(str, type(self.game.player1.name))

    def test_init_valid3(self):
        # checking if name is int
        self.assertEqual(int, type(self.game.player1.count_of_cards))

    def test_init_valid4(self):
        # checking if name is int
        self.assertEqual(int, type(self.game.player1.count_of_cards))

    def test_init_invalid1(self):
        # checking if his giving error at name 1 int
        with self.assertRaises(TypeError):
            CardGame(213, "shirel", 26, 26)

    def test_init_invalid2(self):
        # checking if his giving error at name 2 int
        with self.assertRaises(TypeError):
            CardGame("max", 1233, 26, 26)

    def test_init_invalid3(self):
        # checking if his giving error at amount of card 1 str
        with self.assertRaises(TypeError):
            CardGame("max", "shirel", "max", 26)

    def test_init_invalid4(self):
        # checking if his giving error at amount of card 2 str
        with self.assertRaises(TypeError):
            CardGame("max", "shirel", 26, "shirel")

    def test_init_valid_self_player1(self):
        # Checking that the name in init goes into the name in the player
        a = CardGame("max", "shirel", 26, 10)
        self.assertEqual("max", a.player1.name)

    def test_init_valid_self_player2(self):
        # Checking that the name in init goes into the name in the player
        a = CardGame("max", "shirel", 26, 10)
        self.assertEqual("shirel", a.player2.name)

    def test_init_valid_object_play(self):
        # Checking that the init inserted object player
        self.assertEqual(Player, type(self.player1))

    def test_init_valid_object_play2(self):
        # Checking that the init inserted object player
        self.assertEqual(Player, type(self.player2))

    def test_init_self_deck_of_cards(self):
        # Checking that init inserted a deck object
        self.assertEqual(DeckOfCards, type(self.Deck))

    def test_init_new_game(self):
        # A test that the init called for a new game. and created a deck of random cards for the player
        self.assertNotEqual(self.deck2.cards[:26], self.game.player1.list_cards_of_player)

    def test_init_new_game2(self):
        # A test that the init called for a new game. and created a deck of random cards for the player
        self.assertNotEqual(self.deck2.cards[26:], self.game.player2.list_cards_of_player)

    def test_init_new_game3(self):
        # A test that the init called for a new game.
        # and created a deck of random cards for the player not the same the other player.
        self.assertNotEqual(self.game.player1.list_cards_of_player, self.game.player2.list_cards_of_player)

    def test_init_new_game4(self):
        # A test that the init called for a new game. and gave the players the correct amount of cards
        a = CardGame("max", "shirel", 10, 9)
        self.assertEqual(10, a.player1.count_of_cards)
        self.assertEqual(26, a.player2.count_of_cards)
        self.assertEqual(16, len(a.deck_of_card.cards))

    def test_new_game(self):
        # Checking that new game function is already running
        with self.assertRaises(TypeError):
            self.game.new_game()

    def test_get_winner(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 26, 11)
        self.assertIn("max", a.get_winner())

    def test_get_winner2(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 23, 28)
        self.assertIn("shirel", a.get_winner())

    def test_get_winner_tie(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 26, 26)
        self.assertIn("TIE no one win!", a.get_winner())

    def test_get_winner1_invalid(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 26, 11)
        self.assertNotIn("shirel", a.get_winner())
        self.assertNotIn("TIE no one win!", a.get_winner())

    def test_get_winner2_invalid(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 11, 26)
        self.assertNotIn("max", a.get_winner())
        self.assertNotIn("TIE no one win!", a.get_winner())

    def test_get_winner3_invalid(self):
        # Checking function return the winner and not the loser or tie
        a = CardGame("max", "shirel", 26, 26)
        self.assertNotIn("shirel", a.get_winner())
        self.assertNotIn("max", a.get_winner())
