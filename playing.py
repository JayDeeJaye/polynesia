import matplotlib.pyplot as plt
import numpy as np
import random
from IPython.core.debugger import Pdb
pdb = Pdb()
#pdb.set_trace()

import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='Playing.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Intitalize first!
# Play 100,000 hands
bankroll = 1000.00
wins = 0
losses = 0
pushes = 0
WALLET=[]
R=[0]
n = 100
dealer = Player("Dealer")
players=[QPolicyPlayer("Q Player",1000.0)]
players.append(OPolicyPlayer("Basic Player",1000.0))
players.append(Player("Random Player",1000.0))

#player1 = QPolicyPlayer("Q-Player",1000.0)
#player2 = OPolicyPlayer("BasicPlayer",1000.0)

# Play hands for both players simultaneously

for i in range(n):
    # Initialize s
    newHand([dealer]+players,shoe)
    logging.debug("Dealer's hand: {} ({})".format(dealer.hand,dealer.getPoints()))
    # All players play in turn. Rewards are calculated at the end of the hand
    for p in players:
        logging.debug("{}'s hand: {} ({})".format(p.name,p.hand,p.getPoints()))

        while True:
            s = (p.getPoints(),dealer.hand[0],)
            a = p.getAction(s)
            logging.debug("{} {}: ".format(p.name,a))
    
            if a == 'HIT':
                hit(p,shoe)
            else:
                break
            
            if p.getPoints() > 21:
                break
    
    # Players done; play out the dealer
    while dealer.getPoints() < 17:
        logging.debug("Dealer HIT: ")
        hit(dealer,shoe)

    for p in players:
        r = getReward(p,dealer)*5

        # Calculate and keep track of wins/losses
        if r < 0:
            logging.debug("Lose ({})".format(r))
            p.losses += 1
        elif r > 0:
            logging.debug("Win ({})".format(r))
            p.wins += 1
        else:
            logging.debug("Push ({})".format(r))
            p.pushes += 1

        # Data from the episode    
        p.bankRoll += r
        p.cumReward.append(p.cumReward[-1]+r)
        p.wallet.append(p.bankRoll)

print("Results over {} hands:".format(n))
fig, ax = plt.subplots()
for p in players:
    print("\n\t{} Wins: {} %\n\tOutcome: {}".format(p.name,100*(p.wins/(p.wins+p.losses+p.pushes)),p.bankRoll))
    ax.plot(p.cumReward,label=p.name)

ax.legend(loc='best')
plt.show()

#fig = plt.figure(1,figsize=(12,6))

#plt.subplot(121)
#plt.plot(CR)
#plt.title('Cumulative reward for {} hands'.format(n))

#plt.subplot(122)
#plt.plot(WALLET)
#plt.title('Bankroll over {} hands assuming $5 bet'.format(n))

#fig.tight_layout()
logger.removeHandler(fhandler)