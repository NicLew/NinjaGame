#!/usr/bin/python3

########################################################################
# File Name: 	TargetGroupUnitTests.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Unit tests for the Target Group objects
########################################################################

# python2 -m unittest TargetUnitTests

import unittest
from TargetGroup import *

class TestTargetGroupFunctions (unittest.TestCase):
	
	def setUp (self):
		""" Initializes the target group
		"""
		self.theGroup = TargetGroup()
		
	def tearDown (self):
		""" Nothing to tear down
		"""
		pass
		
	def test_addTargets (self):
		""" Tests that addTarget adds at least one target to the group
		"""
		self.theGroup.addTarget ()
		self.assertTrue (len (self.theGroup._targets) > 0)
		
	def test_update (self):
		""" Tests that update increments the counter.
			Then tests that when the counter is reset, new targets
			are added to the group.
		"""
		self.theGroup.update ()
		self.assertEqual (self.theGroup._counter, 1)
		
		while self.theGroup._counter > 0:
			self.theGroup.update ()
			
		self.assertTrue (len (self.theGroup._targets) > 0)

	def test_checkForCollisions (self):
		""" Adds a target to the group, then tests for collisions with
			two test targets.
			The first test target will collide.
			The second test target will not.
		"""
		testTarget1 = Target (10, 10)
		testTarget2 = Target (20, 20)
		testTarget3 = Target (300, 300)
		
		self.theGroup._targets.add (testTarget1)
		
		self.assertEqual(self.theGroup.checkForCollisions (testTarget2), testTarget1)
		self.assertEqual (self.theGroup.checkForCollisions (testTarget3), -1)
