#1/usr/bin/python2

########################################################################
# File Name: 	WallGroupUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class:		CS360 - Open Source
# Assignment:	Ninja Game - Create Open Source Project
# Purpose: 		UnitTests for the Wall Group object
########################################################################

# python2 -m unittest WallGroupUnitTests

import unittest
from WallGroup import *

class TestWallGroupFunctions (unittest.TestCase):
	
	def setUp (self):
		""" Initializes pygame and Wall Group
		"""
		pygame.init()
		screen = pygame.display.set_mode ((900, 600))
		self.theGroup = WallGroup ()
		
	def tearDown (self):
		""" Nothing to tear down
		"""
		pass
		
	def test_checkForCollisions (self):
		""" Tests collision with two test walls.
			The first one should collide with the top wall.
			The second one should not collide with any walls.
		"""
		testWall1 = Wall (50, -50, True)
		testWall2 = Wall (-50, -50)
		
		self.assertEqual (self.theGroup.checkForCollisions (testWall1),\
		 self.theGroup.topWall)
		self.assertEqual (self.theGroup.checkForCollisions (testWall2), -1)
		 
