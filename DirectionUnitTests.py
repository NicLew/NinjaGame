#!/usr/bin/python2

########################################################################
# File Name: 	DirectionUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Contains unit tests for the Direction module
########################################################################

# python2 -m unittest DirectionUnitTests

import unittest
from Direction import *

class TestDirectionFunctions(unittest.TestCase):
	
	def setUp(self):
		""" Initializes the direction object
		"""
		self.direction = Direction()
		
	def tearDown(self):
		""" There is nothing to tear down
		"""
		pass
		
	def test_getXOffset(self):
		""" Tests that the function returns the proper value for x
			offset
		"""
		self.assertTrue(self.direction.getXOffset() == 0)
		
	def test_getYOffset(self):
		""" Tests that the function returns the proper value for y
			offset
		"""
		self.assertTrue(self.direction.getYOffset() == 0)
		
	def test_setSpeed(self):
		""" Tests that the functions sets the correct speed according
			to the slope of the direction
		"""
		self.direction.setSpeed(0)
		self.assertEqual(self.direction._speed, SPEED_INC_5)
		
		self.direction.setSpeed(10)
		self.assertEqual(self.direction._speed, SPEED_INC_1)
		
		self.direction.setSpeed(6)
		self.assertEqual(self.direction._speed, SPEED_INC_2)
		
		self.direction.setSpeed(5)
		self.assertEqual(self.direction._speed, SPEED_INC_3)
		
		self.direction.setSpeed(3)
		self.assertEqual(self.direction._speed, SPEED_INC_4)
		
		self.direction.setSpeed(0.5)
		self.assertEqual(self.direction._speed, SPEED_INC_5)
		
	def test_calcDirection(self):
		""" Tests that the correct x and y offsets are being calculated
		"""
		self.direction.calcDirection(0, 0, 10, 10)
		self.assertEqual(self.direction._xOffset, -6)
		self.assertEqual(self.direction._yOffset, -6)
