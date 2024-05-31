from unittest import TestCase
from DeckOfCards1.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()
        print("test started")

    def test_init_cards_list_valid(self):
        # Checking the type of value received in the property. valid
        self.assertEqual(list, type(self.deck.cards))

    def test_init_cards_list_invalid(self):
        # Checking the cursed acceptance from giving an incorrect type
        with self.assertRaises(TypeError):
            dad = DeckOfCards()
            int(dad.cards)

    def test_init_count_of_cards_in_list_valid(self):
        # Checking whether 52 cards were received. valid
        self.assertEqual(52, len(self.deck.cards))

    def test_init_count_of_cards_in_list_invalid(self):
        # Checking whether 52 cards were received. invalid
        self.assertNotEqual(0, len(self.deck.cards))

    def test_cards_shuffle_valid(self):
        # Checking that part of the deck is mixed
        self.deck.cards_shuffle()
        mec = DeckOfCards()
        self.assertNotEqual(mec.cards[:5], self.deck.cards[:5])

    def test_card_shuffle_valid2(self):
        # Checking that the whole deck is mixed
        mec = DeckOfCards()
        mec.cards_shuffle()
        self.assertNotEqual(mec.cards, self.deck.cards)

    def test_deal_one_valid(self):
        # Checking that a card has been deleted from the list
        mec = DeckOfCards()
        missed = mec.deal_one()
        self.assertEqual(51, len(mec.cards))

    def test_deal_one_valid2(self):
        # Checking that deal_one  is deleted from the card deck
        a = self.deck.deal_one()
        self.assertNotIn(a, self.deck.cards)

    def test_deal_one_invalid2(self):
        # Checking that one deal is deleted randomly and not just from the end
        popay = DeckOfCards()
        popay.deal_one()
        self.assertEqual(self.deck.cards[-1], popay.cards[-1])

    def test_deal_one_invalid(self):
        # Testing that deal_one  deletes other members each time
        mec = DeckOfCards()
        a = mec.deal_one()
        b = mec.deal_one()
        self.assertNotEqual(a, b)

    def tearDown(self):
        pass

