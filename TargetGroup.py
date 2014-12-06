#!/usr/bin/python2

########################################################################
# File Name: 	TargetGroup.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Class for a Target group object
########################################################################

import pygame
import random
from Target import *

MAX_TARGETS = 15
INITIAL_MIN_TARGET_DELAY = 30
INITIAL_MAX_TARGET_DELAY = 60
INITIAL_MAX_TARGET_ADDED = 1
TARGET_X_RANGE = 70, 780
TARGET_Y_RANGE = 70, 480

class TargetGroup:
	def __init__ (self):
		""" Constructor for the TargetGroup object
		"""
		self._targets = pygame.sprite.Group()
		self._counter = 0
		self._minAddTargetDelay = INITIAL_MIN_TARGET_DELAY
		self._maxAddTargetDelay = INITIAL_MAX_TARGET_DELAY
		self._maxTargetsAddedAtOnce = INITIAL_MAX_TARGET_ADDED
		
		# The random amount of time between target additions
		self._addTargetFrame = random.randint (self._minAddTargetDelay,\
		 self._maxAddTargetDelay)
	
	def draw (self, screen):
		""" Draws the targets to the screen
		"""
		self._targets.draw(screen)
		
	def addTarget (self):
		""" Adds new targets to the group.
		
			Function adds a random number of targets as long as the
			number of targets doesn't exceed the maximum number of
			targets.
			
			New targets are given a random location that doesn't 
			collide with existing targets. The color of new targets
			are also chosen randomly.
		"""
		# Determine number of targets to add
		numNewTargets = random.randint (1, self._maxTargetsAddedAtOnce)
		i = 0
		
		while i < numNewTargets and len (self._targets) < MAX_TARGETS:
			
			# Make random target with random color
			newTarget = Target \
			(random.randint(TARGET_X_RANGE[0], TARGET_X_RANGE[1]),\
			random.randint(TARGET_Y_RANGE[0], TARGET_Y_RANGE[1]), \
			random.randint (0, 1))
			
			# Make sure new target doesn't collide with existing targets
			while True:
				if self.checkForCollisions (newTarget) == -1:
					self._targets.add (newTarget)
					break
				else:
					newTarget = Target \
					(random.randint(TARGET_X_RANGE[0], TARGET_X_RANGE[1]),\
					random.randint(TARGET_Y_RANGE[0], TARGET_Y_RANGE[1]), \
					random.randint (0, 1))
			i += 1
		
	def update (self, addTarget = True):
		""" Updates all targets in the group.
			
			If addTarget is True, then new targets will be added to
			the group. When the ninja is flying, addTarget should be
			set to false.
			
			If a target times out, kill the target.
		"""
		deadTarget = False
		self._targets.update()
		self._counter += 1
		
		if self._counter > self._addTargetFrame and addTarget:
			self._addTargetFrame = random.randint \
			(self._minAddTargetDelay, self._maxAddTargetDelay)
			self._counter = 0
			self.addTarget ()
			
		for target in self._targets:
			if target.timedOut():
				target.kill()
				deadTarget = True
				
		return deadTarget
				
	def checkForCollisions(self, checkedSprite):
		""" Checks for collisions between all targets and the passed-in
			sprite.
			If a collision is detected, return the target that collides.
			Otherwise, return -1
		"""
		for target in self._targets.sprites():
			if pygame.sprite.collide_circle(checkedSprite, target):
				return target
		return -1
	

