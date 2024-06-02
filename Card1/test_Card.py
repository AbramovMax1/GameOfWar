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
        # Checking for compatibility with the received type. valid
        self.assertTrue(int, type(self.card1.value))

    def test_init_valid_suit(self):
        # Checking for compatibility with the received type. valid
        self.assertTrue(str, type(self.card1.suit))

    def test_init_invalid_value(self):
        # Checking for compatibility with the received type. invalid
        with self.assertRaises(TypeError):
            Card("a", "♦️")

    def test_init_invalid_suit(self):
        # Checking for compatibility with the received type. invalid
        with self.assertRaises(TypeError):
            Card(6, 2)

    def test_init_value_less_1(self):
        # Checking for the error that should be received from giving the wrong type to the function
        with self.assertRaises(ValueError):
            Card(0, "♦️")

    def test_init_value_greater_13(self):
        # Checking for the error that should be received from giving the wrong type to the function
        with self.assertRaises(ValueError):
            Card(14, "♦️")

    def test_gt_valid(self):
        # Size comparison test. of edges. valid
        self.assertTrue(self.card4 > self.card1)

    def test_gt_same_value_valid(self):
        # A size comparison test with the same value.valid
        self.assertTrue(self.card4 > self.card3)

    def test_gt_invalid(self):
        # Size comparison test. of edges. invalid
        self.assertFalse(self.card2 > self.card4)

    def test_eq_valid(self):
        # Testing the ability to compare the object according to the value. valid
        self.assertEqual(self.card3.value, self.card4.value)

    def test_eq_invalid(self):
        # Checking the ability to compare the object with the same value. valid
        self.assertTrue(self.card2, self.card4)

    def tearDown(self):
        pass
