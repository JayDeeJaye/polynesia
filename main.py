# %load main.py
from player import Player
from shoe import Shoe
from utilities import hit, newHand, deal, getReward, getAction, getUpdatedQsa
from collections import defaultdict
from IPython.display import clear_output

#import logging
#logging.basicConfig(filename='LearningPolicy.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Initialize
shoe = Shoe(1)
dealer = Player()
player = Player()
Q = defaultdict(float)
N = defaultdict(float)
RTG = [] # Reward to Go function
CR = [] # Cumulative reward function
LOSS = [] # Loss function
ACTIONS=('HIT','STAND',)
epsilon = 10
lr = 0.08
discount = 0.99