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

MAX_SLOPE = 10
MIN_SLOPE = -10
SLOPE_INC_1 = 5
SLOPE_INC_2 = 2
SLOPE_INC_3 = 0.5
SPEED_INC_1 = 1
SPEED_INC_2 = 2
SPEED_INC_3 = 3
SPEED_INC_4 = 5
SPEED_INC_5 = 6

class Direction:
	
	def __init__(self):
		self._xOffset = 0
		self._yOffset = 0
		self._speed = 0

	def calcDirection(self, charX, charY, mouseX, mouseY):
		# y = mx + b
		
		centerX = charX + 50
		centerY = charY + 50
		
		if not centerX == mouseX:
			m = (centerY - mouseY) / (centerX - mouseX)
			if m > MAX_SLOPE:
				m = MAX_SLOPE
			elif m < MIN_SLOPE:
				m = MIN_SLOPE
				
			b = centerY - (m * centerX)
				
			self.setSpeed(m)
			
			if mouseX > centerX:
				if mouseY > centerY:
					newY = m * (centerX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = math.fabs(centerY - newY)
				else:
					newY = m * (centerX + self._speed) + b
					self._xOffset = self._speed
					self._yOffset = -1 * math.fabs(centerY - newY)
			else:
				if mouseY > centerY:
					newY = m * (centerX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = math.fabs(centerY - newY)
				else:
					newY = m * (centerX - self._speed) + b
					self._xOffset = -self._speed
					self._yOffset = -1 * math.fabs(centerY - newY)
			
		else:
			self._xOffset = 0
			self._yOffset = 0
			
	def setSpeed(self, m):
		slope = math.fabs(m)
		
		if slope == MAX_SLOPE:
			self._speed = SPEED_INC_1
		elif slope > SLOPE_INC_1:
			self._speed = SPEED_INC_2
		elif slope > SLOPE_INC_2:
			self._speed = SPEED_INC_3
		elif slope > SLOPE_INC_3:
			self._speed = SPEED_INC_4
		else:
			self._speed = SPEED_INC_5
			
	def getXOffset(self):
		return self._xOffset
		
	def getYOffset(self):
		return self._yOffset
