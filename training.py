import matplotlib.pyplot as plt
import numpy as np
import random
import logging

logger = logging.getLogger()
fhandler = logging.FileHandler(filename='Training.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Intitalize first!
# Train with a number of hands
bankroll = 500.00
netWins = 0
wins = 0
losses = 0
pushes = 0
WALLET=[]
RMS=[]
R=[0]
n = 1000000

# print("Starting bankroll: {}".format(bankroll))
# Training
for i in range(n):
    # Initialize s
    newHand([dealer,player],shoe)
    logging.debug("Dealer's hand: {} ({})".format(dealer.hand,dealer.getPoints()))
    logging.debug("Player's hand: {} ({})".format(player.hand,player.getPoints()))
    s = (player.getPoints(),dealer.hand[0],)
    done = False
    while True:
        logging.debug("Current state: {}".format(s))
        # choose an action
        a = getTrainAction(Q,N,s)
        logging.debug("Player {}: ".format(a))

        # Take the action
        if a == 'HIT':
            hit(player,shoe)
            if player.getPoints() > 21:
                done = True
        else:
            # Player stands; play out the dealer
            while dealer.getPoints() < 17:
                logging.debug("Dealer HIT: ")
                hit(dealer,shoe)
            done = True
        s1 = (player.getPoints(),dealer.hand[0],)

        # Calculate the reward
        if not done:
            r = 0
        else:
            r = getReward(player,dealer)

        # Update Q(s,a)
        Q[s+(a,)] = getUpdatedQsa(Q,s+(a,),r,s1,ACTIONS)
        N[s] += 1
        s = s1    

        # Stop if we're at the terminal state
        if done:
            break

    # Calculate and keep track of wins/losses
    if r < 0:
        logging.debug("Lose ({})".format(r))
        losses += 1
    elif r > 0:
        logging.debug("Win ({})".format(r))
        wins += 1
    else:
        logging.debug("Push ({})".format(r))
        pushes += 1

    # Data from the episode    
    #R.append(r)
    #RTG.append(sum([(R[t]*(discount**t)) for t in range(len(R))]))
    #CR.append(sum(R))

print("\n\tWins: {} %\n\tOutcome: {}".format(100*(wins/(wins+losses+pushes)),sum(R)))

#fig = plt.figure(1,figsize=(12,6))

#plt.subplot(121)
#plt.plot(CR)
#plt.title('Cumulative reward for {} hands'.format(n))

#plt.subplot(122)
#plt.plot(RTG)
#plt.title('Discounted Reward to Go for {} hands'.format(n))

#fig.tight_layout()
logger.removeHandler(fhandler)