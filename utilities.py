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
    
# Updated getAction() using exploration/exploitation
def getTrainAction(Q,N,s):
    e = epsilon/(epsilon + N[s])
    rr = random.random()
    if rr < e:
        logging.debug("Exploring (N[s] = {}, e = {}, rr = {}): Random action selected".format(N[s],e,rr))
        return ACTIONS[random.randint(0,1)]
    else:
        # Use what we've learned
        logging.debug("Exploiting (N[s] = {}, e = {}, rr = {}): Optimal action selected".format(N[s],e,rr))
        if Q[s+('HIT',)] > Q[s+('STAND',)]:
            return 'HIT'
        else:
            return 'STAND'

# Updated Q(s,a) value
def getUpdatedQsa(Q,sa,r,s1,A):
    return Q[sa] + 0.08*(r + discount*max(Q[s1+A[0:1]],Q[s1+A[1:2]]) - Q[sa])

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