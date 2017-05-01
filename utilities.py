import random
import logging

def hit(p,s):
    p.receive(s.draw())
    logging.debug("New hand: {} ({})".format(p.hand,p.getPoints()))

def newHand(d,p,s):
    p.reset()
    d.reset()
    deal(d,p,s)

# Deal
def deal(d,p,s):
    d.receive(s.draw())
    p.receive(s.draw())
    d.receive(s.draw())
    p.receive(s.draw())
    logging.debug("Dealer's hand: {} ({})".format(d.hand,d.getPoints()))
    logging.debug("Player's hand: {} ({})".format(p.hand,p.getPoints()))
    
def getAction():
    r = random.randint(0,1)
    if r == 0:
        return 'HIT'
    else:
        return 'STAND'

# Updated Q(s,a) value
def getUpdatedQsa(Q,sa,r,s1,A):
    return Q[sa] + 0.08*(r + max(Q[s1+A[0:1]],Q[s1+A[1:2]]) - Q[sa])

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