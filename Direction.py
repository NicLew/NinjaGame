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
		self._speed = 0

	def calcDirection(self, charX, charY, mouseX, mouseY):
		# y = mx + b
		if not charX == mouseX:
			
			m = (charY - mouseY) / (charX - mouseX)
			b = charY - (m * charX)
			
			self.setSpeed(m)
			
			if mouseX > charX:
				if mouseY > charY:
					newY = m * (charX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = math.fabs(charY - newY)
				else:
					newY = m * (charX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
			else:
				if mouseY > charY:
					newY = m * (charX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = math.fabs(charY - newY)
				else:
					newY = m * (charX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
			
		else:
			self._xOffset = 0
			self._yOffset = 0
			
	def setSpeed(self, m):
		slope = math.fabs(m)
		#print(slope)
		
		if slope > 10:
			self._speed = 1
		elif slope > 5:
			self._speed = 2
		elif slope > 2:
			self._speed = 3
		elif slope > 0.5:
			self._speed = 5
		else:
			self._speed = 6
			
	def getXOffset(self):
		return self._xOffset
		
	def getYOffset(self):
		return self._yOffset
