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
from Direction import Direction

TOP_WALL = 0
LEFT_WALL = 1
RIGHT_WALL = 2
BOTTOM_WALL = 3
FLIP = 180
COUNTERCLOCKWISE = 90
CLOCKWISE = -90
NO_COLLISIONS = -1
OFF_TOP_WALL = 20
OFF_LEFT_WALL = 20
OFF_RIGHT_WALL = 830
OFF_BOTTOM_WALL = 530

class Character(pygame.sprite.Sprite):
	
	
	def __init__(self, x = 440, y = 275, \
				 imageName = 'NinjaGame_StillNinja.png'):
		""" Constructor for the Character object
		"""
		pygame.sprite.Sprite.__init__(self)
		self._x = x
		self._y = y
		self._direction = Direction()
		self._isMoving = False
		self._isFirstClick = False
		self._currentWall = BOTTOM_WALL
		
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
			#self.spin()
		
	def move(self, walls):
		if walls.checkForCollisions(self) is not NO_COLLISIONS:
			self._isMoving = False
			self.stopAndRotate(walls)
		else:
			self.setLocationByOffset(self._direction.getXOffset(), self._direction.getYOffset())
			self.rect = self.rect.move(self._direction.getXOffset(), self._direction.getYOffset())# move() adds value to x and y, doesn't replace and returns new Rect
			
	def stopAndRotate(self, walls):
		wall = walls.checkForCollisions(self)
		if not self._isMoving:
			if wall == walls.topWall:
				self.image = pygame.transform.rotate(self.image, FLIP)
				self._currentWall = TOP_WALL
				self.setYLocation(OFF_TOP_WALL)
			if wall == walls.leftWall:
				self.image = pygame.transform.rotate(self.image, CLOCKWISE)
				self._currentWall = LEFT_WALL
				self.setXLocation(OFF_LEFT_WALL)
			if wall == walls.rightWall:
				self.image = pygame.transform.rotate(self.image, COUNTERCLOCKWISE)
				self._currentWall = RIGHT_WALL
				self.setXLocation(OFF_RIGHT_WALL)
			if wall == walls.bottomWall:
				self._currentWall = BOTTOM_WALL
				self.setYLocation(OFF_BOTTOM_WALL)
				
			self.setRectLocation(self._x, self._y)				
				
	def rotateAndMove(self):
		if not self._isMoving:
			self.image = pygame.transform.rotate(self.image, 0)
			if self._currentWall == TOP_WALL:
				self.image = pygame.transform.rotate(self.image, FLIP)
			elif self._currentWall == LEFT_WALL:
				self.image = pygame.transform.rotate(self.image, COUNTERCLOCKWISE)
			elif self._currentWall == RIGHT_WALL:
				self.image = pygame.transform.rotate(self.image, CLOCKWISE)
				
	def spin(self):
		#Not sure how to set it back to correct orientation at end of spin...
		self.image = pygame.transform.rotate(self.image, COUNTERCLOCKWISE)
	
	def setDirection(self, mouseX, mouseY):
		self._direction.calcDirection(self._x, self._y, mouseX, mouseY)
		
	def setRectLocation(self, x, y):
		self.rect.x = x
		self.rect.y = y
		
	def setLocationByOffset(self, xOffset, yOffset):
		""" Sets the x and y values of the location of the character 
			to the original values plus the values passed in
		"""
		self.setXLocation(self._x + xOffset)
		self.setYLocation(self._y + yOffset)
		
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
		""" Sets the attribute 'isMoving' to the boolean value passed
			in
		"""
		self._isMoving = isMoving
		
	def getIsMoving(self):
		"""Returns the value of isMoving
		"""
		return self._isMoving
		
	def setIsFirstClick(self, isFirstClick):
		self._isFirstClick = isFirstClick
		
	def getIsFirstClick(self):
		return self._isFirstClick
