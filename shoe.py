import random

class Shoe:
    #
    # Cards are dealt from a shoe, or a chute containing a number
    # of decks of cards which are randomly shuffled.
    # For this exercise, there's no need to differentiate between
    # individual cards, so we'll keep instances of point value instead.
    #
    # There are 52 cards in a deck. Each deck contains 4 suits of 13 cards each:
    #     numbered cards with value 2-10
    #     face cards: Jack, Queen, King, and Ace valued at 10, 10, 10, and 11/1 respectively
    #

    _suit = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    _shoeSize = 0
    
    def __init__(self,deckCount):
        self._shoeSize = deckCount
        self._shuffle()

    def _shuffle(self):
        # [re]fill the shoe and shuffle the order of cards in it
        self.cards = []
        for i in range(self._shoeSize*4):
            self.cards += self._suit
        random.shuffle(self.cards)

    def draw(self):
        # Give out one card from the end of the shoe
        if len(self.cards) < ((self._shoeSize*52) * .20):
            self._shuffle()
            
        return self.cards.pop()
