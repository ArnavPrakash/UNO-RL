# A function for seeing the cards in the player's Hand
# Parameters :- player_Number , player_Card_List
# Return :- None

def showHand(player,playerHand):
    print("Player {}".format(player+1))
    print("Player have the cards :-")
    print("-------------------")
    for card in playerHand:
        print(card)
    print("")