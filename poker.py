# Imports:
import random

# Definition of Class CARD:
class Card(object):
    # Inicialization Method:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        return
    # Show Method:
    def show(self):
        print("[ {} {:{width}} ]".format(self.suit, self.value, width='2'), end="")
        return

# Definition of Class DECK:
class Deck(object):
    # Inicialization Method:
    def __init__(self):
        self.cards = []
        self.build()
        return
    # Build Method:
    def build(self):
        for suit in ["♣", "❤", "♠", "♦"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(suit, value))
        return
    # Show Method:
    def show(self):
        for c in self.cards:
            c.show()
        print
        return
    # Shuffle Method:
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        return
    # Draw Method:
    def draw(self):
        return self.cards.pop()

# Definition of Class PLAYER:
class Player(object):
    # Inicialization Method:
    def __init__(self, name):
        self.name = name
        self.hand = []
        return
    # Show Hand Method:
    def showHand(self):
        print("{}\'s Hand:".format(self.name))
        for card in self.hand:
            card.show()
        print()
    # Draw Card Method:
    def draw(self, deck):
        self.hand.append(deck.draw())
        return
    # Discard Card Method:
    def discard(self, table):
        while len(self.hand) > 0:
            table.discard.append(self.hand.pop())
        return
    # Join Table Method:
    def joinTable(self, table):
        table.players.append(self)
        return

# Definition of Class TABLE:
class Table(object):
    # Inicialization Method:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.discard = []
        self.flop = []
        self.turn = []
        self.river = []
        self.players = []
        return
    # Build Method:
    def build(self):
        self.deck.shuffle()
        return
    # Start Game Method:
    def start(self):
        for n in range(2):
            for player in self.players:
                player.draw(self.deck)
        for n in range(3):
            self.flop.append(self.deck.cards.pop())
        return
    # Show Deck Method:
    def showDeck(self):
        print("===== {} Deck =====".format(self.name))
        self.deck.show()
        print()
        return
    # Show Table Cards Method:
    def showCards(self):
        print("===== {} Table Cards =====".format(self.name))
        if self.flop:
            for card in self.flop:
                card.show()
        else:
            print("[ #### ]"*3, end='')
        if self.turn:
            for card in self.turn:
                card.show()
        else:
            print("[ #### ]", end='')
        if self.river:
            for card in self.river:
                card.show()
        else:
            print("[ #### ]")
    # Show Players Method:
    def showPlayers(self):
        print("===== {} Players =====".format(self.name))
        for player in self.players:
            player.showHand()
        print()
        return

# MAIN of the Program:
table = Table("Table 01")
table.build()

players = []
for player in range(1,10):
    players.append(Player("Player " + str(player)))
for player in players:
    player.joinTable(table)

table.start()
table.showCards()
table.showPlayers()
