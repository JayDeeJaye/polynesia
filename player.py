# Player class

class Player:
    def __init__(self):
        self.reset()

    def reset(self):
        self.hand = []
        
    def receive(self,card):
        self.hand += [card]
        
    def getPoints(self):
        points = sum(self.hand)
        if points <= 21:
            return points

        while (points > 21) and (11 in self.hand):
            self.hand[self.hand.index(11)] = 1
            points = sum(self.hand)

        return points
        
