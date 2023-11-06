from BuildDeck import buildDeck
from ShuffelDeck import shuffelDeck
from DrawCards import drawnCards
from ShowHand import showHand


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
    