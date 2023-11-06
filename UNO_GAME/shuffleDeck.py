# Shuffling a list of items passed into it
# Parameters :- Deck list
# Returning :- Null

import random

def shuffleDeck(uno_deck):
    n = len(uno_deck)
    for i in range(n - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        # Swap the elements at indices i and j
        uno_deck[i], uno_deck[j] = uno_deck[j], uno_deck[i]
