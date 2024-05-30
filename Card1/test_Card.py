from unittest import TestCase
from Card1.Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("Test started")
        self.card1 = Card(2, "♦️")  # ♦️♠️♥️♣️
        self.card1.power = 5
        self.card2 = Card(13, "♣️")
        self.card2.power = 52
        self.card3 = Card(1, "♥️")
        self.card3.power = 55
        self.card4 = Card(1, "♣️")
        self.card4.power = 56

    def test_init_valid_value(self):
        self.assertTrue(int, type(self.card1.value))

    def test_init_valid_suit(self):
        self.assertTrue(str, type(self.card1.suit))

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            Card("a", "♦️")

    def test_init_invalid_suit(self):
        with self.assertRaises(TypeError):
            Card(6, 2)

    def test_init_value_less_1(self):
        with self.assertRaises(ValueError):
            Card(0, "♦️")

    def test_init_value_greater_13(self):
        with self.assertRaises(ValueError):
            Card(14, "♦️")

    def test_gt_valid(self):
        self.assertTrue(self.card4 > self.card1)

    def test_gt_same_value_valid(self):
        self.assertTrue(self.card4 > self.card3)

    def test_gt_invalid(self):
        self.assertFalse(self.card2 > self.card4)

    def test_eq_valid(self):
        self.assertEqual(self.card3, self.card4)

    def test_eq_invalid(self):
        self.assertTrue(self.card2, self.card4)

    def tearDown(self):
        pass
