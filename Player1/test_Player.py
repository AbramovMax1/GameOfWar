from unittest import TestCase
from Player1.Player import Player
from DeckOfCards1.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("maxim", 26)
        self.player2 = Player("shirel", 10)
        self.dec = DeckOfCards()

    def test_init_valid_name(self):
        # Checking to receive str in the name.
        self.assertEqual(str, type(self.player.name))

    def test_init_valid_count_of_cards(self):
        # Checking for getting an int in the number of cards that will be dealt to the player
        self.assertEqual(int, type(self.player.count_of_cards))

    def test_init_invalid_name(self):
        # Error checking for invalid type
        with self.assertRaises(TypeError):
            Player(3, 26)

    def test_init_invalid_count_of_cards(self):
        # Error checking for invalid type
        with self.assertRaises(TypeError):
            Player("maxim", "david")

    def test_init_valid_count_of_cards_of_edge_values1(self):
        # Checking edge values for the cards the player will receive
        self.assertEqual(self.player2.count_of_cards,10)

    def test_init_valid_count_of_cards_of_edge_values1(self):
        # Checking edge values for the cards the player will receive
        edge_values = Player('try',9)
        self.assertEqual(26,edge_values.count_of_cards)
        pass

    def test_init_valid_count_of_cards_of_edge_values1(self):
        # Checking edge values for the cards the player will receive
        self.assertEqual(26, self.player.count_of_cards)

    def test_init_valid_count_of_cards_of_edge_values1(self):
        # Checking edge values for the cards the player will receive
        edge_values = Player('try', 27)
        self.assertEqual(26, edge_values.count_of_cards)

    def test_init_invalid_count_of_cards_of_edge_values1(self):
        # Checking edge values for the cards the player will receive
        edge_values = Player('try', 27)
        self.assertNotEqual(27, edge_values.count_of_cards)

    def test_set_hand_invalid(self):
        # Checking the type of the receiving function
        with self.assertRaises(TypeError):
            self.player.set_hand(12)

    def test_set_hand_valid(self):
        # Checking the list that comes out randomly
        a = DeckOfCards()
        b = DeckOfCards()
        self.player.set_hand(a)
        self.player2.set_hand(b)
        self.assertNotEqual(self.player.list_cards_of_player,self.player2.list_cards_of_player)

    def test_set_hand_valid_len_of_list(self):
        # Checking that the player receives the required amount of cards
        a = Player("try", 11)
        a.set_hand(self.dec)
        self.assertEqual(11,len(a.list_cards_of_player))

    def test_set_hand_invalid_len_of_list(self):
        # Checking that the player receives the required amount of cards
        a = Player("try", 9)
        a.set_hand(self.dec)
        self.assertNotEqual(9,len(a.list_cards_of_player))

    def test_get_card(self):
        pass

    def test_add_card(self):
        pass
