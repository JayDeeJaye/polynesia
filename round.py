# Playing a basic round of Blackjack

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

if dealer.getPoints() == 21:
    print("Dealer wins! Player loses :-(")
elif player.getPoints() == 21:
    print("Player wins! Dealer loses!")
else:
    while player.getPoints() < 21 and player.getPoints() < dealer.getPoints():
        print("Player hits...")
        hit(player,shoe)
    print("Player stays.")
    while dealer.getPoints() < 17:
        print("Dealer hits...")
        hit(dealer,shoe)
    print("Dealer stays.")
    if player.getPoints() > 21:
        print("Player busted :-(")
    elif dealer.getPoints() > 21:
        print("Dealer busted :-(")
    elif player.getPoints() > dealer.getPoints():
        print("Player wins!")
    elif dealer.getPoints() > player.getPoints():
        print("Dealer wins :-(")
    else:
        print("Hand is a draw: no winner.")