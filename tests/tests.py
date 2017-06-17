#!/usr/bin/env python

import sys
sys.path.append("../jumpdrive")
import card
import game
import unittest
from unittest.mock import patch


# Unit tests for running the Jump Drive game
class GameTests(unittest.TestCase):

	def setUp(self):
		self.game = game.Game()

	# Test that a two players exist after running a two player setup
	@patch("game.Game.getPlayerName")
	def testTwoPlayerSetup(self, getPlayerName):
		# Mock player names
		m = unittest.mock.Mock()
		m.side_effect = ["Jordan", "Robot"]
		getPlayerName.return_value = m
		self.game.setup(2)

		self.assertIsInstance(self.game.players[1], game.Player)
		self.assertIsInstance(self.game.players[0], game.Player)

	# Tests that drawn cards are removed from the deck
	def testDeckPopsStack(self):
		d = game.Deck()
		card = d.getCard()
		for x in d.cards:
			self.assertNotEqual(card.id, x.id)

def main():
	unittest.main()

if __name__ == "__main__":
	main()