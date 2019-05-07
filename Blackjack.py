from random import shuffle

DEALER = []
PLAYER = []
PLAYER_STAY = 15
DEALER_STAY = 17

PLAYER_BUST = False
DEALER_BUST = False


CARDS = {
        "ACE" : 11,
        "KING" : 10,
        "QUEEN" : 10,
        "JACK" : 10,
        "10" : 10,
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5,
        "4" : 4,
        "3" : 3,
        "2" : 2
    }

DECK = []

def buildDeck():
  for card in CARDS:
    for i in range(4):
        DECK.append(card)
  shuffle(DECK)
        

def deal():
    DECK.pop()
    PLAYER.append(DECK.pop())
    DEALER.append(DECK.pop())
    PLAYER.append(DECK.pop())
    DEALER.append(DECK.pop())

#Takes either player stay_val and players hand
# or dealers stay val, and dealers hand
def hit(stay_val, hand):
    curVal = getHandVal(hand)
    if curVal >= stay_val:
        return False
    else:
        hand.append(DECK.pop())
        hit(stay_val, hand)


def getHandVal(hand):
    sum = 0
    for card in hand:
        sum += CARDS[card]
    if sum > 21 and hasAce(hand):
        sum -=10
    return sum

def hasAce(hand):
    if "ACE" in hand:
        return True
    return False


def findWinner():
    dlr = getHandVal(DEALER)
    plyr = getHandVal(PLAYER)
    if plyr > 21:
        PLAYER_BUST = True
        return -1
    elif  dlr > 21:
        DEALER_BUST = True
        return 1
    elif plyr < dlr:
        return -1
    elif plyr == dlr:
        return 0
    else:
        return 1
    return


#print(DECK)
#print(PLAYER)
#print(DEALER)
games = 1000000
PLAYER_STAY = 15
for PLAYER_STAY in range(21):
    outcome = 0
    for i in range(games):
        if len(DECK) < 15:
            buildDeck()
        deal()
        hit(PLAYER_STAY, PLAYER)
        hit(DEALER_STAY, DEALER)
        outcome += findWinner()
        DEALER = []
        PLAYER = []
    
    print("When player stays at: ", PLAYER_STAY)
    print("Then win percentage is: ", 100*(outcome+games)/(2*games), "%")
    print("")


