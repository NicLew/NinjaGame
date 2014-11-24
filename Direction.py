#!/usr/bin/python2

########################################################################
# File Name: 	NinjaGame.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Main for the Ninja Game
########################################################################

class Direction:
	
	def __init__(self):
		self._xOffset = 0
		self._yOffset = 0
		self._speed = 2

	def calcDirection(self, charX, charY, mouseX, mouseY):
		# y = mx + b
		if not 0 == charX - mouseX:
			
			m = (charY - mouseY) / (charX - mouseX)
			b = charY - (m * charX)
			
			if mouseX > charX:
				if mouseY > charY:
					newY = m * (charX - self._speed) + b# 4, x and y get larger
					self._yOffset = charY - newY
					print('4\n')
				else:
					newY = m * (charX - self._speed) + b# 2, x gets larger, y gets smaller, WORKS
					self._yOffset = charY - newY
					print('2\n')
			else:# mouseX < charX
				if mouseY > charY:
					newY = m * (charX + self._speed) + b# 3, x gets smaller, y gets larger
					self._yOffset = charY - newY
					print('3\n')
				else:
					newY = m * (charX + self._speed) + b# 1, x and y get smaller, WORKS
					self._yOffset = charY - newY
					print('1\n')
			
			self._xOffset = self._speed
			#self._yOffset = charY - newY
			
		else:
			self._xOffset = 0
			self._yOffset = 0
			
	def getXOffset(self):
		return self._xOffset
		
	def getYOffset(self):
		return self._yOffset
