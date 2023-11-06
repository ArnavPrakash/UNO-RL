# A function for seeing the cards in the player's Hand
# Parameters :- player_Number(which player) , player's_Card_List
# Return :- None

def showHand(player_number, player_hand):
    print(f"Player {player_number + 1}'s Hand:")
    print("Player has the following cards:")
    print("-------------------")
    y=1
    for card in player_hand:
        print("{}) {}".format(y,card))
        y+=1
    
    print("")