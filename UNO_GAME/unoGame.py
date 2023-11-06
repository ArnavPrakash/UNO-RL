from buildDeck import buildDeck
from shuffelDeck import shuffelDeck
from drawCard import drawnCards
from showHand import showHand
from canPlay import canPlay

# Creating Deck
uno_deck = buildDeck()
# Shuffling Deck
shuffelDeck(uno_deck)

# Intialising the Number of Players Playing
players = []
numPlayers = int(input("How many Players ?"))

# Distributing the 5 cards to each player
for player in range(numPlayers):
    players.append(drawnCards(5, uno_deck))

# which player will start 1st
playerTurn = 0
# In what direction game will flow
playDirection = 1
# Defining the playing if true or false
playing = True
discardCards = []
discardCards.append(uno_deck.pop(0))

# Game started
while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile : {}".format(discardCards[-1]))
    canPlay(discardCards[-1],players[playerTurn])
    
    