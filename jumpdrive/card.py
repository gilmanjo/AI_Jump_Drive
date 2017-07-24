#!/usr/bin/env python

from enum import Enum


class CardType(Enum):
	_unused, DEVELOPMENT, NOVELTY, RARE_ELEMENTS, GENES, \
	ALIEN, REBEL, GENERIC = range(8)

class Icon(Enum):
	_unused, EXPLORE, MILITARY, CHROMOSOME, = range(4)

class EffectType(Enum):
	_unused, SCORE, INCOME, LIMIT, SPECIAL = range(5)

class Card(object):
	"""A game card the players with play in a game of Jump Drive

	Args:
		name - the name of the card
		cost - the base cost of the card
		card_type - specifies development or type of world
		effects - a dictionary of effect associated with the card
				this may very well be changed in the future in favor of
				a more elegant solution
		icons - explore, military, or chromosome icons on the card
		military - boolean specifying a military world
		vps - the base number of vps awarded by this card
		income - the base income awarded by this card
	"""
	def __init__(self, card_id, name, cost, card_type, effects, icons,
				military=False, vps=0, income=0):
		super (Card, self).__init__()
		self.card_id = card_id
		self.name = name
		self.cost = cost
		self.card_type = card_type
		self.effects = effects
		self.military = military
		self.vps = vps
		self.income = income
		
	def __str__(self):
		return self.name

class Effect(object):
	"""Abstract object to represent special card effects

	Args:
		description - a text description of the effect
		effect_type - what general effect this is
	"""
	def __init__(self, description, effect_type=EffectType._unused):
		super(Effect, self).__init__()
		self.effect_type = effect_type
		self.description = description

	def __str__(self):
		return self.name

class CountPer(Effect):
	"""Counts a type of card or icon
	"""
	def __init__(self, card_type, reward, count, icon=None, solo=False, 
				other_player=False):
		super(CountPer, self).__init__()

class Discount(Effect):
	"""Lowers the cost of some card type
	"""
	def __init__(self, card_type=CardType._unused, card_name=""):
		super(Discount, self).__init__()

class SettleSecond(Effect):
	"""Player may settle a second world
	"""
	def __init__(self, military, replace, discount=0):
		super(SettleSecond, self).__init__()

class PayMilitary(Effect):
	"""Player may place non-Alien military as non-military with -1 cost

	One of a few effects that may be broken apart into more general
	effects for clarity's sake
	"""
	def __init__(self, arg):
		super(PayMilitary, self).__init__()

class GiveToMostMilitary(Effect):
	"""Card goes to player with the most military in tableau

	One of a few effects that may be broken apart into more general
	effects for clarity's sake
	"""
	def __init__(self, arg):
		super(GiveToMostMilitary, self).__init__()

class TradePact(Effect):
	"""Can only be played with 0 military or Contact Specialist

	One of a few effects that may be broken apart into more general
	effects for clarity's sake
	"""
	def __init__(self):
		super(TradePact, self).__init__()
		
	def playable(self, military, hand):
		pass

class Unique(Effect):
	"""Only one can be played"""
	def __init__(self, arg):
		super(Unique, self).__init__()