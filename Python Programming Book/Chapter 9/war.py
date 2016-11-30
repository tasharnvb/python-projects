# War
# 2 Players compete to win all of the cards

# Pg 283, Challenge No. 2
# Write a one card version of the game War

import cards
import games

class WarCard(cards.Card):
    """A War Card."""
    @property
    def value(self):
        """Determine the value of the card"""
        value = WarCard.RANKS.index(self.rank) + 1
        # ace is the highest card
        if value == 1:
            value = len(WarCard.RANKS) + 1
        return value

class WarDeck(cards.Deck):
    """A War Deck."""
    def populate(self):
        """Populate the deck"""
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))

class WarPlayer(cards.Hand):
    """A War player"""
    def __init__(self, name):
        super(WarPlayer, self).__init__()
        self.name = name

    def __str__(self):
        info = self.name + "'s card: " + str(self.cards[0])
        return info

class WarGame(object):
    """A War Game"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)

        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        """Play a game"""
        winner = None
        while winner is None:
            # Check that the deck has enough cards in it
            deck_size = len(self.deck.cards)
            n_players = len(self.players)
            if n_players >= deck_size:
                self.deck.clear()
                self.deck.populate()
                self.deck.shuffle()

            # deal 1 card to each player (Note to self: the per_hand argument is one by default)
            self.deck.deal(self.players, per_hand=1)

            # display everyone's cards
            for player in self.players:
                print(player)

            # compare each players cards
            highest = [self.players[0]]
            for player in self.players:
                if highest[0] is not player:
                    if player.cards[0].value > highest[0].cards[0].value:
                        highest = [player]
                    elif player.cards[0].value == highest[0].cards[0].value:
                        highest.append(player)

            # remove everyone's cards
            for player in self.players:
                player.clear()

            # was there a winner?
            if len(highest) == 1:
                winner = highest[0]
            else:
                # if not, the losers should not play again
                self.players = highest
                print("There was no clear winner, players must go to war again!")

        print(winner.name + " is the winner!")

def main():
    """Main method"""
    print("\t\tWelcome to War!\n")

    names = []
    number = games.ask_number("How many players? (2 - 7): ", low=2, high=8)
    for i in range(number):
        name = input("Enter player " + str(i + 1) + " name: ")
        names.append(name)
    print()

    game = WarGame(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")
        print()
        print()

main()
input("\n\nPress the enter key to exit.")
