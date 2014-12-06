#!/usr/bin/python2

########################################################################
# File Name: 	CharacterUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Contains unit tests for the Character module
########################################################################

# python2 -m unittest CharacterUnitTests

import unittest
from Character import *

class TestCharacterFunctions(unittest.TestCase):
	
	def setUp(self):
		""" Initializes the ninja
		"""
		pygame.init()
		self._screen = pygame.display.set_mode ((900, 600))	
		self.ninja = Character(x = 0, y = 0)
		
	def tearDown(self):
		""" There is nothing to tear down
		"""
		pass
		
	def test_init(self):
		""" Tests that the correct exception is raised when the
			program cannot load the image file
		"""
		self.assertRaises(SystemExit, self.ninja.__init__, \
						  imageName = 'random.png')
		
	def test_getXLocation(self):
		""" Tests that the function returns the proper value for x
		"""
		self.assertTrue(self.ninja.getXLocation() == 0)
		
	def test_getYLocation(self):
		""" Tests that the function returns the proper value for y
		"""
		self.assertTrue(self.ninja.getYLocation() == 0)
		
	def test_setXLocation(self):
		""" Tests that the function sets x to the correct value
		"""
		self.ninja.setXLocation(33)
		self.assertTrue(self.ninja.getXLocation() == 33)
		
	def test_setYLocation(self):
		""" Tests that the function sets y to the correct value
		"""
		self.ninja.setYLocation(66)
		self.assertTrue(self.ninja.getYLocation() == 66)
		
	def test_setLocationByOffset(self):
		""" Tests that the function sets x and y to the correct values
		"""
		self.ninja.setLocationByOffset(100, 200)
		self.assertTrue(self.ninja.getXLocation() == 100)
		self.assertTrue(self.ninja.getYLocation() == 200)
		
		self.ninja.setLocationByOffset(10, 20)
		self.assertTrue(self.ninja.getXLocation() == 110)
		self.assertTrue(self.ninja.getYLocation() == 220)
		
	def test_setRectLocation(self):
		""" Tests that the function sets x and y of the rect attribute
			to the correct values
		"""
		self.ninja.setRectLocation(100, 300)
		self.assertEqual(self.ninja.rect.x, 100)
		self.assertEqual(self.ninja.rect.y, 300)
		
	def test_setIsMoving(self):
		""" Tests that the function sets isMoving to the correct value
		"""
		self.ninja.setIsMoving(True)
		self.assertTrue(self.ninja._isMoving)
		
		self.ninja.setIsMoving(False)
		self.assertFalse(self.ninja._isMoving)
		
	def test_getIsMoving(self):
		""" Tests that the function returns the proper value for 
			isMoving
		"""
		self.ninja.setIsMoving(True)
		self.assertTrue(self.ninja.getIsMoving())
		
	def test_setCharacterImage(self):
		""" Tests that the correct exception is raised when the
			program cannot load the image file
		"""
		self.assertRaises(SystemExit, self.ninja.setCharacterImage, \
						  imageName = 'random.png')
