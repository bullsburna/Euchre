class Card(object):
    def __init__(self, suit, number):
        if suit not in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            raise ValueError("Invalid suit")
        if number not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            raise ValueError("Invalid number")
        self._suit = suit
        self._number = number
    def __str__(self):
        return self._number + " of " + self._suit
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, suit):
        if suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            self._suit = suit
        else:
            print("Invalid suit")
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, number):
        if number in ["2","3","4","5","6","7","8","9", "10", "J", "Q", "K", "A"]:
            self._number = number
        else:
            print("Invalid number")
