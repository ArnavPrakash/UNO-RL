# function to check wheter a player is able to play or not
# Parmeters :- top most discarded ca
# return :- boolean

def canPlay(top_discarded_card, player_hand):
    # Extracting the color and value from the top discarded card
    top_color, top_value = top_discarded_card.split()

    # Checking if the player has any cards of the same color or value as the top discarded card
    for card in player_hand:
        card_color, card_value = card.split()
        if card_color == top_color or card_value == top_value:
            return True
    
    # Check if the player has any special action cards (e.g., Skip, Reverse, Wild, Wild Draw Four)
    for card in player_hand:
        if card.startswith("Wild") or card.startswith("Draw Two") or card.startswith("Skip") or card.startswith("Reverse"):
            return True

    # If no matching or special action cards were found, the player cannot play their turn.
    return False
