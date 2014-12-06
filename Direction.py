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

MAX_SLOPE = 10
MIN_SLOPE = -10
SLOPE_INC_1 = 5
SLOPE_INC_2 = 3
SLOPE_INC_3 = 0.5
SPEED_INC_1 = 1
SPEED_INC_2 = 3
SPEED_INC_3 = 4
SPEED_INC_4 = 6
SPEED_INC_5 = 7

class Direction:
	
	def __init__(self):
		""" Constructor for the Direction object
		"""
		self._xOffset = 0
		self._yOffset = 0
		self._speed = 0
		self._counter = 0
		self._rise = 0
		self._run = 0

	def calcDirection(self, charX, charY, mouseX, mouseY):
		""" Calculates the x and y offsets that should
			be used to go in the correct direction.
			
			Uses the current position of the character, the current
			position of the mouse, and the formula y = mx + b to 
			calculate the offsets.
		"""
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
			
	"""def calcDirection(self, charX, charY, mouseX, mouseY):
		centerX = charX + 50
		centerY = charY + 50
		
		if not centerX == mouseX:
			self._rise = centerY - mouseY
			self._run = centerX - mouseX
			m = self._rise / self._run
			if m > MAX_SLOPE:
				m = MAX_SLOPE
				self._rise = MAX_SLOPE
				self._run = 1
			elif m < MIN_SLOPE:
				m = MIN_SLOPE
				self._rise = MIN_SLOPE
				self._run = 1
				
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
			self._yOffset = 0"""
			
	def setSpeed(self, m):
		""" Sets the speed according to the steepness of the slope.
		"""
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
		""" Returns the value of the x offset
		"""
		return self._xOffset
		
	def getYOffset(self):
		""" Returns the value of the y offset
		"""
		return self._yOffset
