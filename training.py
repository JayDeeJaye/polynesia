import logging
import random
from utilities import *
from global_identifiers import *

#
# Global references:
# N - the state-action counter for greedy-epsilon exploration function
# Q - the Q(s,a) function

# Get an action using exploration/exploitation based in the current state
def getTrainAction(s):
    global Q
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
def getUpdatedQsa(sa,r,s1):
    global Q
    logging.debug("Updating Q{} {} ...".format(sa,Q[sa]))
    q = Q[sa] + 0.08*(r + discount*max(Q[s1+ACTIONS[0:1]],Q[s1+ACTIONS[1:2]]) - Q[sa])
    logging.debug("Updated Q{} {} ...".format(sa,q))
    return q


def trainQLAgent(dealer,players,shoe,n):
    global Q, N
    # Train with a number of hands
    wins = 0
    losses = 0
    pushes = 0

    # print("Starting bankroll: {}".format(bankroll))
    # Training
    for i in range(n):
        # New episode
        logging.debug("==== Episode {} ====".format(i))
        newHand([dealer]+players,shoe)
        logging.debug("Dealer's hand: {} ({})".format(dealer.hand,dealer.getPoints()))

        for p in players:
            logging.debug("{}'s hand: {} ({})".format(p.name,p.hand,p.getPoints()))
            p.lastState = (p.getPoints(),dealer.hand[0],)
            done = False
            while not done:
                s = p.lastState

                # choose an action
                logging.debug("Current state: {}".format(s))
                a = getTrainAction(s)
                logging.debug("{} {}: ".format(p.name,a))

                # Take the action
                if a == 'HIT':
                    hit(p,shoe)
                    if p.getPoints() > 21:
                        done = True
                else:
                    done = True

                # Update the intermediary Q(s,a)
                if not done:
                    r = 0
                    s1 = (p.getPoints(),dealer.hand[0],)

                    # Update Q(s,a)
                    Q[s+(a,)] = getUpdatedQsa(s+(a,),r,s1)
                    N[s] += 1
                    p.lastState = s1
                    p.lastAction = a

                # This player has reached her terminal state

        # All players stand or busted; play out the dealer
        while dealer.getPoints() < 17:
            logging.debug("Dealer HIT: ")
            hit(dealer,shoe)
        logging.debug("Dealer STAND: ")

        # Update final Q(s,a)
        for p in players:
            r = getReward(p,dealer)
            s = p.lastState
            s1 = (p.getPoints(),dealer.hand[0],)
            Q[s+(a,)] = getUpdatedQsa(s+(a,),r,s1)
            N[s] += 1

            # Metrics
            if r < 0:
                logging.debug("Lose ({})".format(r))
                losses += 1
            elif r > 0:
                logging.debug("Win ({})".format(r))
                wins += 1
            else:
                logging.debug("Push ({})".format(r))
                pushes += 1

    print("\n\tWins: {} %".format(100*(wins/(wins+losses+pushes))))