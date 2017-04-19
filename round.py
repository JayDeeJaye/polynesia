# Playing a round of Blackjack

from player import Player
from shoe import Shoe

def hit(p,s):
    p.receive(s.draw())
    print("New hand: {} ({})".format(p.hand,p.getPoints()))

def newHand(d,p,s):
    p.reset()
    d.reset()
    deal(d,p,s)

# Deal
def deal(d,p,s):
    d.receive(s.draw())
    p.receive(s.draw())
    d.receive(s.draw())
    p.receive(s.draw())
    print("Dealer's hand: {} ({})".format(dealer.hand,dealer.getPoints()))
    print("Player's hand: {} ({})".format(player.hand,player.getPoints()))

#
# Start up
#

shoe = Shoe(1)
dealer = Player()
player = Player()

deal(dealer,player,shoe)


