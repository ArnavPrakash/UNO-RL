# distributing specific num of cards to specific number of players 
# Parameters :- number of Players(int), number of Cards(int), uno_deck (list) 
# return :- players(list) containing list of cards players having

from drawCard import drawnCards

def distrbuteCards(numOfPlayers,numOfCards,uno_deck):
    players=[]
    for player in range(numOfPlayers):
        players.append(drawnCards(numOfCards,uno_deck))
    return players