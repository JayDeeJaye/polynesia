
from player import Player
from shoe import Shoe
from utilities import hit, newHand, deal
import random
from IPython.display import clear_output

def getAction():
    r = random.randint(0,1)
    if r == 0:
        return 'HIT'
    else:
        return 'STAY'

# Initialize
shoe = Shoe(1)
dealer = Player()
player = Player()
allActions=('HIT','STAY',)
Q = defaultdict(float)

# Starting state for a hand/episode
newHand(dealer,player,shoe)

# 1. Choose an action
action = getAction()

# 2. Observe the state
currentState=(player.getPoints(),dealer.hand[0],action)
print("Current state: {}".format(currentState))

# 3. Do the action
if (action == 'HIT'):
    print("Player {}: ".format(action), end=' ')
    hit(player,shoe)
newState = (player.getPoints(),dealer.hand[0])

# Calculate reward
if (action == 'STAY'):
    while dealer.getPoints() < 17:
        print("Dealer HIT: ", end=' ')
        hit(dealer,shoe)
    
    if (player.getPoints() > dealer.getPoints()):
        reward = 1
    elif dealer.getPoints() > 21:
        reward = 1
    elif dealer.getPoints() == player.getPoints():
        reward = 0
    else: 
        reward = -1
else:
    if player.getPoints() > 21:
        reward = -1
    else:
        reward = 0

# 4. Update Q(s,a)
Q[currentState] = Q[currentState] + 0.08*(reward + max(Q[newState+allActions[0:1]],Q[newState+allActions[1:2]]) - Q[currentState])

Q