# Global identifiers
from collections import defaultdict

ACTIONS=('HIT','STAND',)

# Learning functions
Q = defaultdict(float)
N = defaultdict(float)

# Learning variables
epsilon = 10
lr = 0.08
discount = 0.99
