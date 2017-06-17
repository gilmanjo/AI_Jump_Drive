#!/usr/bin/env python

import card


class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()

	def setup(self, num_players):
		self.players = []
		for x in range(num_players):
			p = Player(self.getPlayerName(x + 1))
			self.players.append(p)

	def getPlayerName(self, player_num):
		return input("Name for Player " + str(player_num + ":\t"))

	def run():
		pass
		
class Player(object):
	"""docstring for Player"""
	# Constants
	HAND_SIZE_LIMIT = 10

	def __init__(self, name):
		super(Player, self).__init__()
		self.name = name
		self.hand = Hand()
		
	def __str__(self):
		return self.name
		
class CardArray(object):
	"""docstring for CardArray"""
	def __init__(self):
		super(CardArray, self).__init__()
		self.cards = []

	def getCard(self, idx):
		return self.cards[idx]

	def removeCard(self, idx):
		for x in enumerate(self.cards):
			self.cards[(x - idx) % len(self.cards)]

class Deck(CardArray):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		

	def getCard(self):
		card = super(Deck, self).getCard(0)
		super(Deck, self).removeCard(0)
		return card
	
class Hand(CardArray):
	"""docstring for Hand"""
	def __init__(self):
		super(Hand, self).__init__()

class Action(object):
	"""docstring for Action"""
	def __init__(self, arg):
		super(Action, self).__init__()
		self.arg = arg
		
class Explore(Action):
	"""docstring for Explore"""
	def __init__(self, arg):
		super(Explore, self).__init__()
		self.arg = arg
		
class PayCard(Action):
	"""docstring for Explore"""
	def __init__(self, arg):
		super(PayCard, self).__init__()
		self.arg = arg
		