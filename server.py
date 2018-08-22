from bottle import run, get, post, view, request, redirect
from poker import *

dealer = Dealer()
tables = []
tables.append(Table("Poker Table"))
players = []

@get('/')
@view('index')
def index():
    return tables

@get('/hand/<name>')
def playerHand(name):
    for player in players:
        if player.name == name:
            return player.showHand()

run(host='localhost', port=8080)
