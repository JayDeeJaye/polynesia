# %load round.py
import matplotlib.pyplot as plt
import numpy as np
import random
import logging

logging.basicConfig(filename='LearningPolicy.log', filemode='w', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Updated getAction() using exploration/exploitation
def getAction(Q,N,s):
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

def getUpdatedQsa(Q,sa,r,s1,A):
    return Q[sa] + 0.08*(r + discount*max(Q[s1+A[0:1]],Q[s1+A[1:2]]) - Q[sa])

def discountedRewardToGo(R):
    pass

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
n = 10000

# print("Starting bankroll: {}".format(bankroll))
for i in range(n):
    # Initialize s
    newHand(dealer,player,shoe)
    s = (player.getPoints(),dealer.hand[0],)
    done = False
    while True:
        logging.debug("Current state: {}".format(s))
        # choose an action
        a = getAction(Q,N,s)
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
    bankroll += r*5
    WALLET.append(bankroll)
    R.append(r)
    RMS.append(np.sqrt(sum((np.fromiter(iter(Q.values()), dtype=float))**2)/len(Q)))
    RTG.append(sum([(R[t]*(discount**t)) for t in range(len(R))]))
    CR.append(sum(R))

logging.info("\n\tWins: {}\n\tLosses: {}\n\tPushes: {}\n\tOutcome: {}".format(wins,losses,pushes,sum(R)))

fig = plt.figure(1,figsize=(12,6))

plt.subplot(221)
plt.plot(CR)
plt.title('Cumulative reward for {} hands'.format(n))

plt.subplot(222)
plt.plot(RTG)
plt.title('Discounted Reward to Go for {} hands'.format(n))

plt.subplot(223)
plt.plot(WALLET)
plt.title('Bankroll over {} hands assuming $5 bet'.format(n))

plt.subplot(224)
plt.plot(RMS)
plt.title('Root Mean Square of Q for {} hands'.format(n))

fig.tight_layout()