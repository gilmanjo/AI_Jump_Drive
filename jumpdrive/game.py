import card


class Game(object):
	"""docstring for Game"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg
		
class CardArray(object):
	"""docstring for CardArray"""
	def __init__(self, arg):
		super(CardArray, self).__init__()
		self.arg = arg
	
class Hand(CardArray):
	"""docstring for Hand"""
	def __init__(self, arg):
		super(Hand, self).__init__()
		self.arg = arg

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
		