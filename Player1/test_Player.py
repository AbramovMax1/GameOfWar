from unittest import TestCase
from Player1.Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("maxim", 26)
        print("Test Started")

    def test_init_valid_name(self):
        self.assertTrue(str, self.player.name)

    def test_init_valid_count_of_cards(self):
        self.assertEqual(int, self.player.count_of_cards)

    def test_init_invalid_name(self):
        with self.assertRaises(TypeError):
            Player(3223, 26)

    def test_init_invalid_count_of_cards(self):
        with self.assertRaises(TypeError):
            Player("maxim", "245")

    def test_set_hand(self):
        self.fail()

    def test_get_card(self):
        self.fail()

    def test_add_card(self):
        self.fail()
