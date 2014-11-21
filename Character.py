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
		#calc direction (new x, y coord. * speed)
		#newX, newY = self.calcDirection(walls)
		#call setLocation, move until hit a wall
		if walls.checkForCollisions(self) is walls.topWall or \
		   walls.checkForCollisions(self) is walls.bottomWall or \
		   walls.checkForCollisions(self) is walls.leftWall or \
		   walls.checkForCollisions(self) is walls.rightWall:# change to rotate sprite accordingly??? # Add get methods to WallGroup for each Wall?
			self._isMoving = False
		else:
			#self.setLocation(newX, newY)# How to incorporate speed???
			self.setLocation(self._x, self._y - self._speed)
			self.rect = self.rect.move(self._x - self._x, self._y - self._y - self._speed)# move() adds value to x and y, doesn't replace and returns new Rect
			#self.rect = self.rect.move(self._x - x, self._y - y)# will change to something like this once the direction is calculated
			
	"""def calcDirection(self, walls):
		mouseX, mouseY = pygame.mouse.get_pos()
		if (mouseX - self._x) != 0:
			slope = (mouseY - self._y) / (mouseX - self._x)
			b = mouseY - (slope * mouseX)
			print(str(slope), str(b))
			
			if walls.checkForCollisions(self) is not walls.leftWall and \
			   b > 530 and b < 20:
				   x = 20
				   y = (slope * x) + b
			else:
				x = 30
				y = 30
			
		else:
			x = mouseX
			y = 30
		
		return (x, y) # Return offset instead???"""
		
	def setLocation(self, x, y):
		""" Sets the x and y values of the location of the character 
			to the values passed in
		"""
		self.setXLocation(x)
		self.setYLocation(y)
		
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
		
	"""def setIsFirstClick(self, isFirstClick):
		self._isFirstClick = isFirstClick
		
	def getIsFirstClick(self):
		return self._isFirstClick"""
