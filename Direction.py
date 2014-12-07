#!/usr/bin/python2

########################################################################
# File Name: 	Direction.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Direction module
########################################################################

import math

SPEED = 10
NINJA_CENTER = 25

class Direction:
	
	def __init__(self):
		""" Constructor for the Direction object
		"""
		self._xOffset = 0
		self._yOffset = 0
		self._speed = SPEED

	def calcDirection(self, charX, charY, mouseX, mouseY):
		""" Calculates the x and y offsets that should
			be used to go in the correct direction.
			
			Uses the current position of the character and the current
			position of the mouse.
		"""
		centerX = charX + NINJA_CENTER
		centerY = charY + NINJA_CENTER
		
		if not centerX == mouseX:
			angle = math.atan2((mouseY - centerY), (mouseX - centerX))
			self._yOffset = self._speed * math.sin(angle)
			self._xOffset = self._speed * math.cos(angle)
		else:
			self._yOffset = 0
			self._xOffset = 0
			
	def getXOffset(self):
		""" Returns the value of the x offset
		"""
		return self._xOffset
		
	def getYOffset(self):
		""" Returns the value of the y offset
		"""
		return self._yOffset
