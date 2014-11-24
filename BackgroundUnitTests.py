#1/usr/bin/python2

########################################################################
# File Name: 	BackgroundUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		UnitTests for the background object
########################################################################

# python2 -m unittest BackgroundUnitTests

import pygame
from Background import *
import unittest

class TestBackgroundFunctions (unittest.TestCase):
	
	def setUp (self):
		""" Initialize pygame and background
		"""
		pygame.init()
		screen = pygame.display.set_mode ((900,600))
		self.background = Background()
		
	def tearDown (self):
		""" Nothing to tear down
		"""
		pass
		
	def test_init (self):
		""" Tests that exception is raised when the passed in file
			cannot be opened
		"""
		self.assertRaises(SystemExit, self.background.__init__, \
						  imageName = 'random.png')
						  
	def test_setBackgroundImage (self):
		""" Tests that exception is raised when the passed in file
			cannot be opened
		"""
		self.assertRaises(SystemExit, self.background.__init__, \
						  imageName = 'random.png')
