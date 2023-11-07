import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
        self.drawnCards = []
        self.colors = ["Red", "Green", "Yellow", "Blue"]
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
        self.wilds = ["Wild", "Wild Draw Four"]
        self.build_deck()

    def build_deck(self):
        for color in self.colors:
            for value in self.values:
                if value != 0:
                    self.cards.append(Card(color, value))
                    self.cards.append(Card(color, value))
        for _ in range(4):
            self.cards.append(Card(self.wilds[0], "Wild"))
            self.cards.append(Card(self.wilds[1], "Wild Draw Four"))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            drawn_card = self.cards.pop()
            self.drawnCards.append(drawn_card)
            return drawn_card
        else:
            print("The Deck is Empty")
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_hand(self):
        print(f"{self.name}'s Hand:")
        print("Player has the following cards:")
        print("-------------------")
        for i, card in enumerate(self.hand, 1):
            print(f"{i}) {card}")
        print("")

    def draw_cards(self, deck, num_cards):
        for _ in range(num_cards):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

    def play_card(self, card_index, discard_pile):
        if 0 <= card_index - 1 < len(self.hand):
            card = self.hand.pop(card_index - 1)
            discard_pile.append(card)
            return card
        else:
            print("Invalid card index.")
            return None

class UnoGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.discard_pile = []

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.draw_cards(self.deck, 7)
        self.discard_pile.append(self.deck.draw_card())
        self.play_game()

    def play_game(self):
        player_turn = 0
        play_direction = 1
        current_color = self.discard_pile[-1].color
        card_val = self.discard_pile[-1].value if self.discard_pile[-1].value else "Any"

        while True:
            player = self.players[player_turn]
            print(f"{player.name}'s turn:")
            print("Card on top of discard pile:", self.discard_pile[-1])
            player_hand = player.hand
            player.show_hand()

            if UnoGame.can_play(current_color, card_val, player_hand):
                card_index = int(input("Enter the index of the card to play: "))
                played_card = player.play_card(card_index, self.discard_pile)

                if played_card:
                    if played_card.color == "Wild":
                        new_color = int(input("Choose a color (1-4): "))
                        current_color = self.deck.colors[new_color - 1]
                        self.discard_pile[-1].color = current_color
                    card_val = played_card.value
                    if card_val == "Reverse":
                        play_direction *= -1
                    elif card_val == "Skip":
                        player_turn += play_direction
                    elif card_val == "Draw Two":
                        player_draw = player_turn + play_direction
                        self.players[player_draw].draw_cards(self.deck, 2)
                    # Correct the card type to "Draw Four"
                    elif card_val == "Draw Four":
                        player_draw = player_turn + play_direction
                        if player_draw >= len(self.players):
                            player_draw = 0
                        self.players[player_draw].draw_cards(self.deck, 4)

                        # Prompt the player to choose a color for "Wild Draw Four"
                        new_color = int(input("Choose a color (1-4): "))
                        current_color = self.deck.colors[new_color - 1]
                        self.discard_pile[-1].color = current_color

                if not player.hand:
                    print(f"{player.name} has won!")
                    break
            else:
                print("You can't play, you have to draw a card.")
                player.draw_cards(self.deck, 1)

            player_turn += play_direction
            if player_turn >= len(self.players):
                player_turn = 0

    @staticmethod
    def can_play(current_color, card_val, player_hand):
        for card in player_hand:
            if "Wild" in card.color:
                return True
            elif current_color == card.color:
                return True
            elif card_val == card.value:
                return True
        return False

    def show_results(self):
        print("Game Over")

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
