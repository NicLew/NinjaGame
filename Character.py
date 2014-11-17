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

class Character(pygame.sprite.Sprite):
	
	def __init__(self, x = 440, y = 535, speed = 0, \
				 imageName = 'NinjaGame_StillNinja.png'):
		""" Constructor for the Character object
		"""
		pygame.sprite.Sprite.__init__(self)
		self._x = x
		self._y = y
		self._speed = speed #may be speed object later on
		
		try:
			self._characterImage = pygame.image.load(imageName)
			
		except pygame.error, message:
			print 'Cannot load image:', imageName
			raise SystemExit, message
		
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
		
	def setLocation(self, x, y):
		""" Sets the x and y values of the location of the character 
			to the values passed in
		"""
		self.setXLocation(x)
		self.setYLocation(y)
		
	def draw(self, screen):
		""" Draws the character to the screen
		"""
		screen.blit(self._characterImage, (self._x, self._y))
