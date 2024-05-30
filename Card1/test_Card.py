from unittest import TestCase
from Card1.Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("Test started")
        self.card1 = Card(1, "♦️")  # ♦️♠️♥️♣️
        self.card2 = Card(13, "♣️")
        self.card3 = Card(1, "♦️")
        self.card4 = Card(1, "♣️")

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            Card("a", "♦️")

    def test_init_invalid_suit(self):
        with self.assertRaises(TypeError):
            Card(6, 2)

    def test_init_valid_value(self):
        self.assertEqual(self.card1, self.card1)

    def test_init_valid_suit(self):
        self.assertEqual(self.card2, self.card2)

    def test_gt_invalid(self):
        self.assertFalse(self.card2 > self.card4)

    def test_gt_valid(self):
        """שיראל תתיקן את הבעיה הזאת בבקשה"""
        self.assertTrue(self.card4 > self.card1)

    def tearDown(self):
        pass

