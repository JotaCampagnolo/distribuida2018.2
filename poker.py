# Imports:
import bottle
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

# Definition of Class PLAYER:python3-bottle
class Player(object):
    # Inicialization Method:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        return
    # Show Hand Method:
    def showHand(self):
        print("{}\'s Hand:".format(self.name), end="")
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
        self.cards = []
        self.players = []
        return
    # Start Game Method:
    def start(self):
        while self.discard:
            self.deck.cards.append(self.discard.pop())
        self.deck.shuffle()
        for player in self.players:
            player.points = 0
        for n in range(2):
            for player in self.players:
                player.draw(self.deck)
        for n in range(3):
            self.cards.append(self.deck.cards.pop())
        for n in range(2):
            self.discard.append(self.deck.cards.pop())
            self.cards.append(self.deck.cards.pop())
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
        for card in self.cards:
            card.show()
        print()
    # Show Players Method:
    def showPlayers(self):
        print("===== {} Players =====".format(self.name))
        for player in self.players:
            player.showHand()
        print()
        return

# Definition of Class Dealer:
class Dealer(object):
    # Inicialization Method:
    def __init__(self):
        self.weight = {"A":13, "K":12, "Q":11, "J":10, "10":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
        self.multiplier = {"♣":2, "❤":1.5, "♠":1, "♦":0.5}
        return
    # Player Hand Evaluation:
    def evaluateHand(self, table, player):
        playerPoints = 0
        for card in player.hand:
            playerPoints += self.weight[str(card.value)]*self.multiplier[str(card.suit)]
        return playerPoints

# MAIN of the Program:
dealer = Dealer()
table = Table("Table 01")
players = []
for player in range(1,10):
    players.append(Player("Player " + str(player)))
for player in players:
    player.joinTable(table)

table.start()
table.showCards()
table.showPlayers()
print(dealer.evaluateHand(table, players[0]))
