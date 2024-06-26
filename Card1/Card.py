class Card:

    def __init__(self, value: int, suit: str):
        """We give to card value and power for Comparison of forces"""
        if type(value) != int:
            raise TypeError("I accept only digit numbers")
        if type(suit) != str:
            raise TypeError("I accept only string here")
        if value < 1 or value > 13:
            raise ValueError("invalid value")

        self.value = value
        self.suit = suit
        self.power = 0

    def __repr__(self):
        """Giving Value and suit to our Card1"""
        if self.value == 1:
            return f"A{self.suit}"
        if self.value == 11:
            return f"J{self.suit}"
        if self.value == 12:
            return f"Q{self.suit}"
        if self.value == 13:
            return f"K{self.suit}"
        return f"{self.value}{self.suit}"

    def __gt__(self, other):
        """measure which object (card) is bigger"""
        if self.power > other.power:
            return True
        return False

    def __eq__(self, other):
        """compares objects (cards)"""
        if self.power == other.power:
            return True
        return False
