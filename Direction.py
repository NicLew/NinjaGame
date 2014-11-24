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
			
			if mouseX < charX:
				if mouseY < charY:
					newY = m * (charX + self._speed) + b# 4, x and y get larger
					self._xOffset = self._speed
					self._yOffset = math.fabs(charY - newY)
					print('4\n')
				else:
					newY = m * (charX + self._speed) + b# 2, x gets larger, y gets smaller, WORKS
					self._xOffset = self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
					print('2\n')
			else: # if mouseX < charX
				if mouseY < charY:
					newY = m * (charX - self._speed) + b# 3, x gets smaller, y gets larger
					self._xOffset = -self._speed
					self._yOffset = math.fabs(charY - newY)
					print('3\n')
				else:
					newY = m * (charX - self._speed) + b# 1, x and y get smaller, WORKS
					self._xOffset = -self._speed
					self._yOffset = -1 * math.fabs(charY - newY)
					print('1\n')
			
			"""if mouseX > charX:
				if mouseY > charY:
					newY = m * (charX + self._speed) + b# 4, x and y get larger
					self._xOffset = self._speed
					print('4\n')
				else:
					newY = m * (charX + self._speed) + b# 2, x gets larger, y gets smaller, WORKS
					self._xOffset = self._speed
					print('2\n')
			else: # if mouseX < charX
				if mouseY > charY:
					newY = m * (charX - self._speed) + b# 3, x gets smaller, y gets larger
					self._xOffset = -self._speed
					print('3\n')
				else:
					newY = m * (charX - self._speed) + b# 1, x and y get smaller, WORKS
					self._xOffset = -self._speed
					print('1\n')"""
			
			#self._yOffset = charY - newY
			
		else:
			self._xOffset = 0
			self._yOffset = 0
			
	def getXOffset(self):
		return self._xOffset
		
	def getYOffset(self):
		return self._yOffset
