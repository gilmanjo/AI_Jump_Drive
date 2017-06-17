#!/usr/bin/env python

from setuptool import setup

with open("README", "r") as f:
	long_description = f.read()

setup(
	name="jumpdrive",
	version=0.01,
	description="AI Application to the game 'Jump Drive'",
	author="Jordan Gilman",
	author_email="gilmanjo@oregonstate.edu"
)