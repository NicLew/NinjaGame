#!/usr/bin/python2

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

class Character(pygame.sprite.Sprite):
	
	def __init__(self, x = 440, y = 530, speed = 5, isMoving = False, \
				 imageName = 'NinjaGame_StillNinja.png'):
		""" Constructor for the Character object
		"""
		pygame.sprite.Sprite.__init__(self)
		self._x = x
		self._y = y
		self._speed = speed #may be speed object later on
		self._isMoving = isMoving
		
		try:
			self._characterImage = pygame.image.load(imageName)
			
		except pygame.error, message:
			print 'Cannot load image:', imageName
			raise SystemExit, message
		self._characterImage.convert()
		self.rect = self._characterImage.get_rect()
		self.rect.move(self._x, self._y)
			
	def draw(self, screen):
		""" Draws the character to the screen
		"""
		screen.blit(self._characterImage, (self._x, self._y))
		
	def update(self, walls):
		self.kill()
		if self._isMoving:
			self.move(walls)
		
	def move(self, walls):
		#calc direction (new x, y coord. * speed)
		#call setLocation, move until hit a wall
		if walls.checkForCollisions(self) == walls.topWall:# change to rotate sprite accordingly??? # Add get methods to WallGroup for each Wall?
			self._isMoving = False
		else:
			self.setLocation(self._x, self._y - self._speed)
		
	def setLocation(self, x, y):
		""" Sets the x and y values of the location of the character 
			to the values passed in
		"""
		self.setXLocation(x)
		self.setYLocation(y)
		self.rect.move(self._x, self._y)
		
	def setXLocation(self, x):
		""" Sets the x value of the location of the character to the
			value passed in
		"""
		self._x = x
		
	def setYLocation(self, y):
		""" Sets the y value of the location of the character to the
			value passed in
		"""
		self._y = y
		
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
