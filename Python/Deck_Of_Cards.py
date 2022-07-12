class Card:
	def __init__(self, value, suit):
		self.suit = suit
		self.value = value


class Deck:
	pass


c = Card("A", "Hearts")
print(__repre__(c))