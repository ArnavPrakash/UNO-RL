# function to check wheter a player is able to play or not
# Parmeters :- colour , number of card , player hand list
# return :- boolean

def canPlay(color,number, player_hand):

    for card in player_hand:
        
        if "Wild" in card:
            return True
        elif color in card:
            return True
        elif number in card:
            return True
    return False

