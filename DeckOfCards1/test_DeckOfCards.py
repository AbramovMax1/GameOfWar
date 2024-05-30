from unittest import TestCase
from DeckOfCards1.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()
        print("test started")

    def test_init_cards_list_valid(self):
        self.assertEqual(list, type(self.deck.cards))

    def test_init_cards_list_invalid(self):
        with self.assertRaises(TypeError):
            dad = DeckOfCards()
            int(dad.cards)

    def test_init_count_of_cards_in_list_valid(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_init_count_of_cards_in_list_invalid(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_cards_shuffle_valid(self):
        self.deck.cards_shuffle()
        mec = DeckOfCards()
        self.assertTrue(mec.cards[:3], self.deck.cards[:3])

    def test_card_shuffle_invalid(self):
        mec = DeckOfCards()
        self.assertEqual(mec.cards[:3], self.deck.cards[:3])

    def test_deal_one_valid(self):
        self.deck.deal_one()
        mec = DeckOfCards()
        self.assertTrue(mec.deal_one(), self.deck.deal_one())

    def test_deal_one_valid2(self):
        a = self.deck.deal_one()
        self.assertIn(a, self.deck.cards)

    def test_deal_one_invalid2(self):
        a = self.deck
        self.assertTrue(a, self.deck.cards)

    def test_deal_one_invalid(self):
        mec = DeckOfCards()

    def tearDown(self):
        pass

