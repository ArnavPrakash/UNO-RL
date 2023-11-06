# Creating DrawCards Function that draws specfic no.s of card
# Parameters :- No. of cards to draw , Deck
# Return :- Card Drawn List

def drawnCards(numCards,uno_deck):
    cardsDrawn = []
    for i in range(numCards):
        cardsDrawn.append(uno_deck.pop(i))
    return cardsDrawn