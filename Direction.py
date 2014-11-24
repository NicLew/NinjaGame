#!/usr/bin/python2

########################################################################
# File Name: 	NinjaGame.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Main for the Ninja Game
########################################################################

import math

class Direction:
	
	def __init__(self):
		self._xOffset = 0
		self._yOffset = 0
		self._speed = 5

	def calcDirection(self, charX, charY, mouseX, mouseY):
		# y = mx + b
		if not charX == mouseX:
			
			m = (charY - mouseY) / (charX - mouseX)
			b = charY - (m * charX)
			
			if mouseX > charX:
				if mouseY > charY:
					newY = m * (charX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = math.fabs(charY - newY)
					print('4\n')
				else:
					newY = m * (charX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
					print('2\n')
			else:
				if mouseY > charY:
					newY = m * (charX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = math.fabs(charY - newY)
					print('3\n')
				else:
					newY = m * (charX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
					print('1\n')
			
		else:
			self._xOffset = 0
			self._yOffset = 0
			
	def getXOffset(self):
		return self._xOffset
		
	def getYOffset(self):
		return self._yOffset
