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
	"""docstring for Card"""
	def __init__(self, name, cost, card_type, effects, icons, military=False, 
				vps=0, income=0):
		super (Card, self).__init__()
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
	"""docstring for Effect"""
	def __init__(self, description, effect_type=EffectType._unused):
		super(Effect, self).__init__()
		self.effect_type = effect_type
		self.description = description

	def __str__(self):
		return self.name

class CountPer(Effect):
	"""Counts a type of card or icon and """
	def __init__(self, card_type, reward, count, icon=None, solo=False, 
				other_player=False):
		super(CountPer, self).__init__()

class Discount(Effect):
	""""""
	def __init__(self, card_type=CardType._unused, card_name=""):
		super(Discount, self).__init__()

class SettleSecond(Effect):
	"""Player may settle a second world"""
	def __init__(self, military, replace, discount=0):
		super(SettleSecond, self).__init__()

class PayMilitary(Effect):
	"""Player may place non-Alien military as non-military with -1 cost"""
	def __init__(self, arg):
		super(PayMilitary, self).__init__()

class GiveToMostMilitary(Effect):
	"""Card goes to player with the most military in tableau"""
	def __init__(self, arg):
		super(GiveToMostMilitary, self).__init__()

class TradePact(Effect):
	"""Can only be played with 0 military or Contact Specialist"""
	def __init__(self):
		super(TradePact, self).__init__()
		
	def playable(self, military, hand):
		pass

class Unique(Effect):
	"""Only one can be played"""
	def __init__(self, arg):
		super(Unique, self).__init__()