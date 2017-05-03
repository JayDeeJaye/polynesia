import random
import logging

def hit(p,s):
    p.receive(s.draw())
    logging.debug("New hand: {} ({})".format(p.hand,p.getPoints()))

def newHand(P,s):
    for p in P:
        p.reset()
    deal(P,s)

# Deal
def deal(P,s):
    for i in range(2):
        for p in P:
            p.receive(s.draw())
    
def getReward(p,d):
    if p.getPoints() > 21:
        return -1

    # Blackjack?
    if d.hasBlackjack():
        if p.hasBlackjack():
            return 0
        else:
            return -1
    elif p.hasBlackjack():
        return 1.5
    elif d.getPoints() > 21:
        return 1
    elif p.getPoints() > d.getPoints():
        return 1
    elif p.getPoints() == d.getPoints():
        return 0
    else:
        return -1