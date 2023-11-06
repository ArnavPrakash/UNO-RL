# Creating DrawCards Function that draws specfic no.s of card
# Parameters :- No. of cards to draw , Deck
# Return :- Card Drawn List

def drawnCards(numCards,uno_deck):
    cardsDrawn = []
    for i in range(numCards):
        if uno_deck:
            cardsDrawn.append(uno_deck.pop())
        else:
            print("The Deck is Empty")
            break 
    return cardsDrawn