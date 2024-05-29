class Card:

    def __init__(self, value: int, suit: str):
        """We give to card value and power for Comparison of forces"""
        self.value = value
        self.suit = suit
        self.power = 0

    def __str__(self):
        return f"your card :[{self.value}:{self.suit}]"

    def __repr__(self):
        """Giving Value and suit to our Card"""
        if self.value == 1:
            return f"Ace:{self.suit}:{self.power}"
        if self.value == 11:
            return f"Jack:{self.suit}:{self.power}"
        if self.value == 12:
            return f"Queen:{self.suit}:{self.power}"
        if self.value == 13:
            return f"King:{self.suit}:{self.power}"
        return f"{self.value}:{self.suit}:{self.power}"

    def __gt__(self, other):
        if self.power > other.power:
            return True
        return False

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False
