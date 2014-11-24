#!/usr/bin/python3

########################################################################
# File Name: 	NinjaGame.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Main for the Ninja Game
########################################################################

import pygame
from WallGroup import *
from Direction import Direction

class Character(pygame.sprite.Sprite):
	
	
	def __init__(self, x = 440, y = 275, speed = 5, isMoving = False, \
				 imageName = 'NinjaGame_StillNinja.png'):
		""" Constructor for the Character object
		"""
		pygame.sprite.Sprite.__init__(self)
		self._x = x
		self._y = y
		self._speed = speed #may be speed object later on
		self._direction = Direction()
		self._isMoving = False
		#self._isFirstClick = isFirstClick
		
		try:
			self.image = pygame.image.load(imageName)
			
		except pygame.error, message:
			print 'Cannot load image:', imageName
			raise SystemExit, message
		self.image.convert()
		self.rect = self.image.get_rect().move(self._x, self._y)
			
	def draw(self, screen):
		""" Draws the character to the screen
		"""
		screen.blit(self.image, (self._x, self._y))
		
	def update(self, walls):
		self.kill()
		if self._isMoving:
			self.move(walls)
		
	def move(self, walls):
		if walls.checkForCollisions(self) is walls.topWall or \
		   walls.checkForCollisions(self) is walls.bottomWall or \
		   walls.checkForCollisions(self) is walls.leftWall or \
		   walls.checkForCollisions(self) is walls.rightWall:# change to rotate sprite accordingly??? # Add get methods to WallGroup for each Wall?
			self._isMoving = False
		else:
			self.setLocation(self._direction.getXOffset(), self._direction.getYOffset())
			self.rect = self.rect.move(self._direction.getXOffset(), self._direction.getYOffset())# move() adds value to x and y, doesn't replace and returns new Rect
			
	def setDirection(self, mouseX, mouseY):
		self._direction.calcDirection(self._x, self._y, mouseX, mouseY)
			
		
	def setLocation(self, xOffset, yOffset):
		""" Sets the x and y values of the location of the character 
			to the values passed in
		"""
		self.setXLocation(xOffset)
		self.setYLocation(yOffset)
		
	def setXLocation(self, xOffset):
		""" Sets the x value of the location of the character to the
			value passed in
		"""
		self._x = self._x + xOffset
		
	def setYLocation(self, yOffset):
		""" Sets the y value of the location of the character to the
			value passed in
		"""
		self._y = self._y + yOffset
		
	def getXLocation(self):
		""" Returns the value of the x location of the character
		"""
		return self._x
		
	def getYLocation(self):
		""" Returns the value of the y location of the character
		"""
		return self._y
		
	def setIsMoving(self, isMoving):
		self._isMoving = isMoving
		
	def getIsMoving(self):
		return self._isMoving
		
	"""def setIsFirstClick(self, isFirstClick):
		self._isFirstClick = isFirstClick
		
	def getIsFirstClick(self):
		return self._isFirstClick"""
