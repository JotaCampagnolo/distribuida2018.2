# Imports:
import random

# Definition of Class CARD:
class Card(object):
    # Inicialization Method:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        return
    # Show Card Method:
    def show(self):
        print("[ {} of {} ]".format(self.value, self.suit))
        return

# Definition of Class DECK:
class Deck(object):
    # Inicialization Method:
    def __init__(self):
        self.cards = []
        self.build()
        return
    # Build Deck Method:
    def build(self):
        for suit in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(suit, value))
        return
    # Show Deck Method:
    def show(self):
        for c in self.cards:
            c.show()
        print
        return
    # Shuffle Deck Method:
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        return
    # Draw Card Method:
    def draw(self):
        return self.cards.pop()

# Definition of Class PLAYER:
class Player(object):
    # Inicialization Method:
    def __init__(self, name):
        self.name = name
        self.hand = []
        return
    # Shows Player Hand Method:
    def showHand(self):
        print("{}\'s Hand:".format(self.name))
        for card in self.hand:
            card.show()
        print
    # Draw Card from Deck Method:
    def draw(self, deck):
        self.hand.append(deck.draw())
        return

# Definition of Class TABLE:
class Table(object):
    # Inicialization Method:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.players = []
        return
    # Build Table Method:
    def build(self):
        self.deck.shuffle()
        return
    # Shows Table Method:
    def show(self):
        print("=== Table: {} ===\n".format(self.name))
        print("== Table Deck ==")
        self.deck.show()
        print("== Table Players ==")
        for player in self.players:
            player.showHand()
        return

# MAIN of the Program:
table = Table("Table 01")
table.build()
table.show()
