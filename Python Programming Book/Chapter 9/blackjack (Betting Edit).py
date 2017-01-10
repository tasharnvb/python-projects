# Blackjack (Betting Edit)
# From 1 to 7 players compete against a dealer

# Pg 283, Challenge No. 3
# Improve the Blackjack game by allowing players to bet
# Keep track of each player's moeny and remove any player who runs out of money

import cards, games

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """
    def __init__(self, name):
        super(BJ_Player, self).__init__(name)
        self.money = 20.0
        self.current_bet = None

    def __str__(self):
        rep = super(BJ_Player, self).__str__() + "\t\tBet: " + str(self.current_bet)
        return rep

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")
        self.money -= self.current_bet
        round(self.money, 2)
        if self.money <= 0:
            print(self.name, "is out of money!")

    def win(self):
        print(self.name, "wins.")
        if self.total == 21:
            self.money += self.current_bet * 1.5
        else:
            self.money += self.current_bet
            round(self.money, 2)

    def push(self):
        print(self.name, "pushes.")

    def bet(self, minimum_bet):
        while self.current_bet == None:
            self.current_bet = input("\n" + self.name + ", how much would you like to bet? (Money: " + str(self.money) + ", Minimum bet: " + str(minimum_bet) + "): ")

            try:
                self.current_bet = float(self.current_bet)
            except (TypeError, ValueError):
                print("Please only enter numbers")
                self.current_bet = None

            if self.current_bet != None:
                self.current_bet = round(self.current_bet, 2)
                if self.current_bet < minimum_bet:
                    print("You cannot bet lower than the minimum")
                    self.current_bet = None
                elif self.current_bet > self.money:
                    print("You do not have enough money to make that bet. Please try again with a lower bet")
                    self.current_bet = None


class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.minimum_bet = 1.0

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting() and self.deck:
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # Check that the deck has enough cards in it
        deck_size = len(self.deck.cards)
        n_players = len(self.players) + 1
        if n_players * 2 >= deck_size:
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()

        # take each player's bet
        for player in self.players:
            player.bet(self.minimum_bet)

        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards and remove players with no money left
        for player in self.players:
            player.clear()
            player.current_bet = None
            if player.money <= 0:
                self.players.remove(player)
        self.dealer.clear()


def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter player " + str(i + 1) + " name: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        # Check if there are still players with money left
        if len(game.players) > 0:
            again = games.ask_yes_no("\nDo you want to play again?: ")
        else:
            print("\n\nAll players are out of money! Better luck next time!")
            again = "n"


main()
input("\n\nPress the enter key to exit.")
