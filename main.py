#from player import Player
from shoe import Shoe
#from utilities import hit, newHand, deal, getReward, getAction, getUpdatedQsa
from collections import defaultdict
from IPython.display import clear_output

#import logging
#logger = logging.getLogger()
#fhandler = logging.FileHandler(filename='Training.log', mode='a')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
#logger.setLevel(logging.DEBUG)

# Initialize
# Game elements
shoe = Shoe(1)
dealer = Player("Dealer")
players = [Player("Player 1")]
players.append(Player("Player 2"))

ACTIONS=('HIT','STAND',)

# Learning functions
Q = defaultdict(float)
N = defaultdict(float)

# Learning variables
epsilon = 10
lr = 0.08
discount = 0.99

#logger.removeHandler(fhandler)