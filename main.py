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
shoe = Shoe(1)
dealer = Player("Dealer")
player = Player("Player1")
Q = defaultdict(float)
N = defaultdict(float)
RTG = [] # Reward to Go function
CR = [] # Cumulative reward function
LOSS = [] # Loss function
ACTIONS=('HIT','STAND',)
epsilon = 10
lr = 0.08
discount = 0.99

#logger.removeHandler(fhandler)