# Player class
import random

ACTIONS = ['HIT','STAND']

class Player:
    def __init__(self,name,bankRoll=0):
        self.name = name
        self.bankRoll = bankRoll
        self.wallet = []
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.cumReward = [0]
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
    
    def hasBlackjack(self):
        return (self.getPoints() == 21 and len(self.hand) == 2)
    
    # Default action for a player is random
    def getAction(self,_):
        return ACTIONS[random.randint(0,len(ACTIONS)-1)]

class QPolicyPlayer(Player):
    def getAction(self,s):
        qas = {q: Q[q] for q in Q.keys() if q[0:2] == s}
        sa = max(qas.keys(), key=lambda k: qas[k])
        return sa[-1]
    
class OPolicyPlayer(Player):
    def getAction(self,s):
        return BASIC[s]
    