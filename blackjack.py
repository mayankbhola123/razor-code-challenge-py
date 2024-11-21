from deck import Deck
import random
from collections import defaultdict

class Blackjack:
    def __init__(self, num_decks=1):
        """
        Initialize the Blackjack table with a specified number of decks.
        :param num_decks: Number of decks to use at the table.
        """
        self.blackjack_cards = []
        self.active_hands = defaultdict(list) # key: player_name and value: [cards they hold]
        for _ in range(num_decks):
            new_deck = Deck()
            self.blackjack_cards.extend(new_deck.cards)
        # print(self.blackjack_cards)
        # print(len(self.blackjack_cards))

    def reset(self):
        """Reset the table by shuffling all decks together and clearing active hands."""
        # return all the cards back to deck
        self.__init__()
        # self.active_hands = {}

        random.shuffle(self.blackjack_cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise IndexError("No cards are left in the deck.")

    def deal(self, player):
        """
        Deal two cards to a player.
        :param player: The player's identifier (e.g., a name or number).
        """
        self.active_hands[player].append(self.draw)
        self.active_hands[player].append(self.draw)

    def hit(self, player):
        """
        Add a card to the player's hand.
        :param player: The player's identifier.
        """
        self.active_hands[player].append(self.draw)

    def split(self, player):
        """
        Split a player's hand into two if the first two cards are of the same rank.
        You can only split after the initial deal, not after you already hit
        Also adds a card to each new hand.
        :param player: The player's identifier.
        """
        first_card = self.active_hands[player].pop()
        second_card = self.active_hands[player].pop()
        
        # split the cards into two
        if first_card[0] == second_card[0]:
            
            # put the first card back and add 1
            self.active_hands[player].append(first_card)
            self.active_hands[player].append(self.draw)
            
            # put the second card as a new player with key same as "startsWith" of the existing player
            # add 1 card
            self.active_hands[player+"1"].append(second_card)
            self.active_hands[player+"1"].append(self.draw)

    def fold(self, player):
        """
        Fold the player's hand, removing them from the active hands.
        :param player: The player's identifier.
        """
        del self.active_hands[player]
        if (player+"1") in self.active_hands.keys():
            del self.active_hands[player+"1"]



new_Blackjack=Blackjack(num_decks=2)
