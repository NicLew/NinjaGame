#!/usr/bin/python3

########################################################################
# File Name: 	Target.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 		12/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Class for a Target sprite object
########################################################################

import pygame

COUNTDOWN_FRAME = 60

class Target(pygame.sprite.Sprite):
	
	def __init__ (self, x = 0, y = 0, isRed = True):
		""" Constructor for the Target Sprite Class
		
			If isRed is true, set up the sprite as a red target.
			Otherwise, set up the sprite as a green target.
		"""
		pygame.sprite.Sprite.__init__(self)
		self._isRed = isRed
		self._imageList = []
		
		# Set up red target images
		if self._isRed:	
			try:
				imageName = 'NinjaGame_RedTarget1.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_RedTarget2.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_RedTarget3.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_RedTarget4.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_RedTarget5.png'
				self._imageList.append (pygame.image.load (imageName))
			except pygame.error, message:
				print 'Cannot load image:', imageName
				raise SystemExit, message
		
		# Set up green target images
		else:
			try:
				imageName = 'NinjaGame_GreenTarget1.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_GreenTarget2.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_GreenTarget3.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_GreenTarget4.png'
				self._imageList.append (pygame.image.load (imageName))
				imageName = 'NinjaGame_GreenTarget5.png'
				self._imageList.append (pygame.image.load (imageName))
			except pygame.error, message:
				print 'Cannot load image:', imageName
				raise SystemExit, message
				
		self._currentImage = 4
		self._counter = 0
		self._timedOut = False
		self.image = self._imageList[self._currentImage]
		self.rect = self.image.get_rect().move (x, y)
		
	def update(self):
		""" Updates the Target
			Increments counter by 1.
			Once counter reaches COUNTDOWN_FRAME, set target's image to
			the next image in the list. If the target is already at the
			last image in the list, set ._timedOut to True.
		"""
		self._counter += 1
		
		if self._counter > COUNTDOWN_FRAME and not self._timedOut:
			self._counter = 0
			if self._currentImage > 0:
				self._currentImage -= 1
				self.image = self._imageList[self._currentImage]
			else:
				self._timedOut = True
				
	def timedOut (self):
		""" Returns whether or not the target has timed out
		"""
		return self._timedOut
		
	def isRed (self):
		""" Returns wheter or not the target is red
		"""
		return self._isRed
	
