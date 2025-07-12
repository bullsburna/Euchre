from cards import Card
class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)
    def populate(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        numbers = ["9", "10", "J", "Q", "K", "A"]
        cards = []
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

