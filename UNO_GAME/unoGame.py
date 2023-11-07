from buildDeck import buildDeck
from shuffleDeck import shuffleDeck
from drawCard import drawnCards
from showHand import showHand
from canPlay import canPlay
from distributeCards import distrbuteCards

# Creating Deck
uno_deck = buildDeck()
# Shuffling Deck
shuffleDeck(uno_deck)


# # Intialising the Number of Players Playing
players = []
colors = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many Players ?"))
while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(input("Enter a number between 2-4. How many Players ?"))
 # Distributing the 7 cards to each player
for player in range(numPlayers):
    players.append(drawnCards(7, uno_deck))

# # which player will start 1st
playerTurn = 0
# # In what direction game will flow
playDirection = 1
# # Defining the playing if true or false
playing = True
discardCards = []
discardCards.append(uno_deck.pop(0))
splitCards = discardCards[0].split(" ", 1)
currentColor = splitCards[0]
if currentColor != "Wild":
    cardVal = splitCards[1]
else:
    cardVal = "Any"

# Game started
while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile : {}".format(discardCards[-1]))
    if (canPlay(currentColor, cardVal, players[playerTurn])):
        cardChoosen = int(input("Enter the index of card :"))
        while(cardChoosen<1 or cardChoosen>len(players[playerTurn])):
            print("Please enter vaild index")
            cardChoosen = int(input("Enter the index of card :"))

        while not canPlay(currentColor, cardVal, [players[playerTurn][cardChoosen-1]]):
            cardChoosen = int(input("Not a valid card,Enter the index of card :"))
        print("You played {}".format(players[playerTurn][cardChoosen-1]))
        discardCards.append(players[playerTurn].pop(cardChoosen-1))


        # Checking for special cards
        splitCards = discardCards[-1].split(" ", 1)
        currentColor = splitCards[0]
        if (len(splitCards) == 1):
            cardVal = "Any"
        else:
            cardVal = splitCards[1]
        if (currentColor == "Wild"):
            for x in range(len(colors)):
                print("{}) {}".format(x+1, colors[x]))
            newColor = int(input("What color would you like to choose ?"))
            while newColor < 1 or newColor > 4:
                newColor = int(
                    input("What color would you like to choose,you entered invalid index ?"))
            currentColor = colors[newColor-1]
            discardCards[-1] = "wild" + currentColor
        if cardVal == "Reverse":
            playDirection = playDirection * -1
        elif cardVal == "Skip":
            playerTurn += playDirection
            if (playerTurn >= numPlayers):
                playerTurn = 0
            elif playerTurn < 0:
                playerTurn = numPlayers-1
        elif cardVal == "Draw Two":
            playerDraw = playerTurn+playDirection
            if (playerDraw == numPlayers):
                playerDraw = 0
            elif playerDraw < 0:
                playerDraw = numPlayers-1
            players[playerDraw].extend(drawnCards(2, uno_deck))
        elif cardVal == "Draw Four":
            playerDraw = playerTurn+playDirection
            if (playerDraw == numPlayers):
                playerDraw = 0
            elif playerDraw < 0:
                playerDraw = numPlayers-1
            players[playerDraw].extend(drawnCards(4, uno_deck))

    else:
        print("You can't play, You have to take a card from deck")
        players[playerTurn].extend(drawnCards(1, uno_deck))
    print("")

    playerTurn += playDirection
    if (playerTurn >= numPlayers):
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1
    
    for player in players:
        if len(player) == 0:
            print(f"Player {players.index(player) + 1} has won!")
            playing = False
            break


print("Game Over")