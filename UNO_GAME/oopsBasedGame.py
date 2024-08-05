import random

# Represents a single card in the game
class Card:
    def __init__(self, color, value):
        self.color = color  # Color of the card
        self.value = value  # Value of the card (e.g., number or action)

    def __str__(self):
        return f"{self.color} {self.value}"  # String representation of the card

# Represents the deck of cards used in the game
class Deck:
    def __init__(self):
        self.cards = []  # List of cards currently in the deck
        self.drawnCards = []  # List of cards that have been drawn
        self.colors = ["Red", "Green", "Yellow", "Blue"]  # Valid colors for cards
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]  # Valid values for colored cards
        self.wilds = ["Wild", "Wild Draw Four"]  # Special wild cards
        self.build_deck()  # Initialize the deck with cards

    def build_deck(self):
        # Add numbered cards and action cards for each color (excluding '0' which only appears once)
        for color in self.colors:
            for value in self.values:
                if value != 0:
                    self.cards.append(Card(color, value))
                    self.cards.append(Card(color, value))
        # Add wild cards (4 Wild and 4 Wild Draw Four)
        for _ in range(4):
            self.cards.append(Card(self.wilds[0], "Wild"))
            self.cards.append(Card(self.wilds[1], "Wild Draw Four"))

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffle the deck

    def draw_card(self):
        if self.cards:
            drawn_card = self.cards.pop()  # Draw a card from the deck
            self.drawnCards.append(drawn_card)  # Keep track of drawn cards
            return drawn_card
        else:
            print("The Deck is Empty")
            return None

# Represents a player in the game
class Player:
    def __init__(self, name):
        self.name = name  # Player's name
        self.hand = []  # List of cards in the player's hand

    def show_hand(self):
        print(f"{self.name}'s Hand:")
        print("Player has the following cards:")
        print("-------------------")
        for i, card in enumerate(self.hand, 1):
            print(f"{i}) {card}")  # Display each card in hand with index
        print("")

    def draw_cards(self, deck, num_cards):
        for _ in range(num_cards):
            card = deck.draw_card()  # Draw a specified number of cards from the deck
            if card:
                self.hand.append(card)  # Add the drawn card to player's hand

    def play_card(self, card_index, discard_pile):
        if 0 <= card_index - 1 < len(self.hand):
            card = self.hand.pop(card_index - 1)  # Remove the selected card from player's hand
            discard_pile.append(card)  # Add the played card to the discard pile
            return card
        else:
            print("Invalid card index.")
            return None

# Manages the Uno game
class UnoGame:
    def __init__(self):
        self.deck = Deck()  # Create a deck of cards
        self.players = []  # List of players in the game
        self.discard_pile = []  # Stack of discarded cards

    def add_player(self, name):
        player = Player(name)  # Create a new player
        self.players.append(player)  # Add the player to the list

    def start_game(self):
        self.deck.shuffle()  # Shuffle the deck
        for player in self.players:
            player.draw_cards(self.deck, 7)  # Deal 7 cards to each player
        self.discard_pile.append(self.deck.draw_card())  # Draw the first card to start the discard pile
        self.play_game()  # Start the game loop

    def play_game(self):
        player_turn = 0  # Index of the player whose turn it is
        play_direction = 1  # Direction of play (1 for clockwise, -1 for counter-clockwise)
        current_color = self.discard_pile[-1].color  # Color of the top card in the discard pile
        card_val = self.discard_pile[-1].value if self.discard_pile[-1].value else "Any"  # Value of the top card

        while True:
            player = self.players[player_turn]  # Get the current player
            print(f"{player.name}'s turn:")
            print("Card on top of discard pile:", self.discard_pile[-1])
            player_hand = player.hand
            player.show_hand()  # Show the player's hand

            # Check if the player can play a card
            if UnoGame.can_play(current_color, card_val, player_hand):
                card_index = int(input("Enter the index of the card to play: "))
                played_card = player.play_card(card_index, self.discard_pile)

                if played_card:
                    if played_card.color == "Wild":
                        new_color = int(input("Choose a color (1-4): "))
                        current_color = self.deck.colors[new_color - 1]  # Update the color
                        self.discard_pile[-1].color = current_color
                    card_val = played_card.value
                    if card_val == "Reverse":
                        play_direction *= -1  # Reverse the direction of play
                    elif card_val == "Skip":
                        player_turn += play_direction  # Skip the next player
                    elif card_val == "Draw Two":
                        player_draw = player_turn + play_direction
                        self.players[player_draw].draw_cards(self.deck, 2)  # Draw two cards for the next player
                    elif card_val == "Draw Four":
                        player_draw = player_turn + play_direction
                        if player_draw >= len(self.players):
                            player_draw = 0
                        self.players[player_draw].draw_cards(self.deck, 4)  # Draw four cards for the next player

                        # Prompt the player to choose a color for "Wild Draw Four"
                        new_color = int(input("Choose a color (1-4): "))
                        current_color = self.deck.colors[new_color - 1]
                        self.discard_pile[-1].color = current_color

                if not player.hand:
                    print(f"{player.name} has won!")  # Declare the winner
                    break
            else:
                print("You can't play, you have to draw a card.")
                player.draw_cards(self.deck, 1)  # Draw a card if the player cannot play

            player_turn += play_direction
            if player_turn >= len(self.players):
                player_turn = 0  # Wrap around if necessary

    @staticmethod
    def can_play(current_color, card_val, player_hand):
        # Check if the player has a playable card
        for card in player_hand:
            if "Wild" in card.color:
                return True
            elif current_color == card.color:
                return True
            elif card_val == card.value:
                return True
        return False

    def show_results(self):
        print("Game Over")  # Display a message when the game ends

# Entry point of the script
if __name__ == "__main__":
    uno_game = UnoGame()
    num_players = int(input("How many players (2-4)? "))
    while num_players < 2 or num_players > 4:
        num_players = int(input("Enter a number between 2 and 4: "))
    for i in range(num_players):
        player_name = input(f"Enter the name for Player {i + 1}: ")
        uno_game.add_player(player_name)

    uno_game.start_game()
    uno_game.show_results()
