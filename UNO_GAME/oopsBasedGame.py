import random

class UnoDeck:
    def __init__(self):
        self.colors = ["Red", "Green", "Yellow", "Blue"]
        self.values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Reverse", "Skip", "Draw Two", "Wild", "Wild Draw Four"]
        self.deck = [(color, value) for color in self.colors for value in self.values]

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)

class UnoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, num_cards):
        for _ in range(num_cards):
            self.hand.append(deck.draw_card())

    def play_card(self, card_index, discard_pile):
        card = self.hand.pop(card_index)
        discard_pile.append(card)
        return card

class UnoGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = UnoDeck()
        self.deck.shuffle()
        self.players = [UnoPlayer(f"Player {i+1}") for i in range(num_players)]
        self.discard_pile = [self.deck.draw_card()]
        self.current_player = 0
        self.play_direction = 1

        for player in self.players:
            player.draw_cards(self.deck, 7)
            
    def change_direction(self):
        self.play_direction *= -1

    def skip_player(self):
        self.current_player += self.play_direction
        if self.current_player >= self.num_players:
            self.current_player = 0
        elif self.current_player < 0:
            self.current_player = self.num_players - 1

    def draw_cards(self, num_cards, player_index):
        for _ in range(num_cards):
            self.players[player_index].draw_cards(self.deck, 1)

    def play_game(self):
        current_color = self.discard_pile[-1][0]
        card_value = self.discard_pile[-1][1]

        while True:
            player = self.players[self.current_player]
            print(f"{player.name}'s turn")
            print(f"Current Card: {self.discard_pile[-1]}")
            print(f"Your Hand: {player.hand}")

            valid_cards = [(i, card) for i, card in enumerate(player.hand) if card[0] == current_color or card[1] == card_value or card[0] == 'Wild']
            
            if valid_cards:
                card_index = int(input("Enter the index of the card to play: "))
                while card_index < 0 or card_index >= len(valid_cards):
                    card_index = int(input("Invalid index. Enter the index of the card to play: "))

                played_card = player.play_card(valid_cards[card_index][0], self.discard_pile)
                current_color, card_value = played_card[0], played_card[1]

                if card_value == "Wild":
                    new_color = int(input("Choose a new color (1-4): "))
                    current_color = self.deck.colors[new_color - 1]

                if card_value == "Reverse":
                    self.change_direction()
                elif card_value == "Skip":
                    self.skip_player()
                elif card_value == "Draw Two":
                    self.draw_cards(2, self.current_player)
                elif card_value == "Draw Four":
                    self.draw_cards(4, self.current_player)

            else:
                print("You can't play. Drawing a card from the deck.")
                self.draw_cards(1, self.current_player)

            if len(player.hand) == 0:
                print(f"{player.name} has won!")
                break

            self.current_player += self.play_direction
            if self.current_player >= self.num_players:
                self.current_player = 0
            elif self.current_player < 0:
                self.current_player = self.num_players - 1

if __name__ == "__main__":
    num_players = int(input("How many players? "))
    while num_players < 2 or num_players > 4:
        num_players = int(input("Enter a number between 2-4. How many players? "))
    
    game = UnoGame(num_players)
    game.play_game()
