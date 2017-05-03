import matplotlib.pyplot as plt
import numpy as np
import random
import logging

logger = logging.getLogger()
fhandler = logging.FileHandler(filename='Training.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Intitalize first!
# Train with a number of hands
wins = 0
losses = 0
pushes = 0
R=[0]
n = 100000

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
            a = getTrainAction(Q,N,s)
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
                Q[s+(a,)] = getUpdatedQsa(Q,s+(a,),r,s1,ACTIONS)
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
        Q[s+(a,)] = getUpdatedQsa(Q,s+(a,),r,s1,ACTIONS)
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

logger.removeHandler(fhandler)