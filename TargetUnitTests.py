#1/usr/bin/python3

########################################################################
# File Name: 	TargetUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		UnitTests for the Target object
########################################################################

# python2 -m unittest TargetUnitTests

import unittest
from Target import *

class TestTargetFunctions (unittest.TestCase):
	
	def setUp (self):
		""" Initializes a green and red target
		"""
		self.redTarget = Target ()
		self.greenTarget = Target (isRed = False)
		
	def tearDown (self):
		""" Nothing to tear down
		"""
		pass
		
	def test_update (self):
		""" Tests that update increments the counter.
			Then tests when counter resets, image is changed
		"""
		
		# Test that update increments the counter
		self.redTarget.update()
		self.assertEqual(self.redTarget._counter, 1)
		
		# Test that when counter resets, currentImage increments 
		while self.redTarget._counter > 0:
			self.redTarget.update()
		
		self.assertEqual (self.redTarget._currentImage, 3)
		
	def test_timedOut (self):
		""" Tests that a target successfully times out
		"""
		for x in range (0, COUNTDOWN_FRAME * 5):
			self.greenTarget.update ()
			
		self.assertTrue (self.greenTarget.timedOut)
	
	def test_isRed (self):
		""" Tests isRed
		"""
		self.assertTrue (self.redTarget.isRed ())
	
