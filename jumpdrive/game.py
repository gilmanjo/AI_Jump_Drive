#!/usr/bin/env python

import card
import os
import random


class Game(object):
	"""Contains all the game players, elements, etc.
	"""
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
	"""Corresponds a player to their hand, name, and score
	"""
	# Constants
	HAND_SIZE_LIMIT = 10

	def __init__(self, name):
		super(Player, self).__init__()
		self.name = name
		self.hand = Hand()
		
	def __str__(self):
		return self.name
		
class CardArray(object):
	"""Abstract object for collections of cards
	"""
	def __init__(self):
		super(CardArray, self).__init__()
		self.cards = []

	def getCard(self, idx):
		return self.cards[idx]

	def removeCard(self, idx):
		"""Removes a card from the array, given an index
		"""
		self.cards.pop(idx)

class Deck(CardArray):
	"""Container for all cards in a single game
	"""
	def __init__(self):
		super(Deck, self).__init__()
		self.loadDeck()

	def _parseCardData(self, card_data):
		"""Given a list of card data, parses it into an object
		"""
		card_id = card_data[0]
		name = card_data[1]
		cost = card_data[2]
		card_type = card.CardType[card_data[3]]
		
		# Check for effects to load
		effects = {}
		if card_data[4] != "None":
			pass
		
		# Check for icons to load
		icons = []
		if card_data[5] != "None":

			for icon in card_data[5].strip().split(","):
				icons.append(card.Icon[icon])

		# Check for the optional arguments
		military = False
		vps = 0
		income = 0
		for x in range(6, len(card_data)):

			if card_data[x].find("military") != -1:
				military = bool(card_data[x][card_data[x].find("military")+9:])

			elif card_data[x].find("vps") != -1:
				vps = int(card_data[x][card_data[x].find("vps")+4:])

			elif card_data[x].find("income") != -1:
				income = int(card_data[x][card_data[x].find("income")+7:])

		return card.Card(card_id, name, cost, card_type, effects, icons,
						military, vps, income)

	def drawCard(self):
		"""Gets and removes the first card from the deck
		"""
		return self.cards.pop(0)

	def loadDeck(self):
		"""Initializes the deck from a text file
		"""
		CARD_DATA_FN = "./card_data.txt"
		abspath = os.path.abspath(__file__)
		dname = os.path.dirname(abspath)
		os.chdir(dname)
		with open(CARD_DATA_FN, "r") as f:

			for line in f.readlines():

				# skip 'comment' lines
				if line[0] == "#":
					continue

				new_card_data = line.strip().split("\t")
				self.cards.append(self._parseCardData(new_card_data))

			# shuffle the deck
			random.shuffle(self.cards)
	
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
		