from unittest import TestCase
from Player1.Player import Player
from DeckOfCards1.DeckOfCards import DeckOfCards
from Card1.Card import Card
from unittest import mock


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("maxim", 26)
        self.player2 = Player("shirel", 10)
        self.dec = DeckOfCards()
        self.dec2 = DeckOfCards()

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
        self.assertEqual(self.player2.count_of_cards, 10)

    def test_init_valid_count_of_cards_of_edge_values2(self):
        # Checking edge values for the cards the player will receive
        edge_values = Player('try', 9)
        self.assertEqual(26, edge_values.count_of_cards)
        pass

    def test_init_valid_count_of_cards_of_edge_values3(self):
        # Checking edge values for the cards the player will receive
        self.assertEqual(26, self.player.count_of_cards)

    def test_init_valid_count_of_cards_of_edge_values4(self):
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

    @mock.patch('DeckOfCards1.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, "♦️"))
    def test_set_hand_equal(self, the_mock_deal_one):
        shirel = Player("shirel", 10)
        shirel.set_hand(self.dec)
        self.assertEqual(Card(1, "♦️"), shirel.list_cards_of_player[0])

    def test_set_hand_valid(self):
        # Checking the list that comes out randomly
        a = DeckOfCards()
        b = DeckOfCards()
        self.player.set_hand(a)
        self.player2.set_hand(b)
        self.assertNotEqual(self.player.list_cards_of_player, self.player2.list_cards_of_player)

    def test_set_hand_valid_len_of_list(self):
        # Checking that the player receives the required amount of cards
        a = Player("try", 11)
        a.set_hand(self.dec)
        self.assertEqual(11, len(a.list_cards_of_player))

    def test_set_hand_invalid_len_of_list(self):
        # Checking that the player receives the required amount of cards
        a = Player("try", 9)
        a.set_hand(self.dec)
        self.assertNotEqual(9, len(a.list_cards_of_player))

    def test_get_card_len_valid(self):
        # A test that drops a card from the amount of the player's deck
        a = Player("try", 26)
        a.set_hand(self.dec)
        a.get_card()
        self.assertEqual(25, a.count_of_cards)

    def test_get_card_len_invalid(self):
        # A test that drops a card from the amount of the player's deck
        a = Player("try", 15)
        a.set_hand(self.dec)
        a.get_card()
        self.assertNotEqual(15, a.count_of_cards)

    def test_get_card_random(self):
        # Checking that the received card is random
        self.player.set_hand(self.dec)
        a = [self.player.get_card(), self.player.get_card(), self.player.get_card()]
        self.player2.set_hand(self.dec2)
        b = [self.player2.get_card(), self.player2.get_card(), self.player2.get_card()]
        self.assertNotEqual(a, b)

    def test_get_card_The_card_that_comes_out1(self):
        # Checking the deleted card is the one that came out
        self.player.set_hand(self.dec)
        self.assertIn(self.player.get_card(), self.dec2.cards)

    def test_get_card_The_card_that_comes_out2(self):
        # Checks the deleted card is a card that was on the list
        self.player.set_hand(self.dec)
        self.assertNotIn(self.player.get_card(), self.dec.cards)

    def test_add_card_type_valid(self):
        # A checker that adds a card object to the deck
        card = self.dec.cards[0]
        self.player.add_card(card)
        self.assertEqual(Card, type(self.player.list_cards_of_player[0]))

    def test_add_card_type_invalid(self):
        # A checker that adds a card object to the deck
        with self.assertRaises(TypeError):
            self.player.set_hand(self.dec)
            self.player.add_card(15)

    def test_add_same_card_valid(self):
        # A checker that counts the addition
        card = self.dec.cards[0]
        self.player.add_card(card)
        self.assertEqual(card, self.player.list_cards_of_player[0])

    def test_add_same_card_valid2(self):
        # Checks that the traded card is the one added
        card = self.dec.cards[0]
        self.player.add_card(card)
        self.assertNotEqual(0, self.player.count_of_cards)
