#1/usr/bin/python2

########################################################################
# File Name: Background.py
# Authors: Nicole Lewey and Jacob Lundgren
# Date: 12/08/2014
# Class: CS360 - Open Source
# Assignment: Ninja Game - Create Open Source Project
# Purpose: Class for the background module
########################################################################

import pygame

class Background:
	
	def __init__ (self, imageName = 'NinjaGame_Background.png'):
		""" Constructor for the Background object
		"""
		try:
			self._backgroundImage = pygame.image.load(imageName)
			
		except pygame.error, message:
			print 'Cannot load image:', imageName
			raise SystemExit, message
			
		self._backgroundImage.convert()
		
	def setSurfaceToBackground(self, screen):
		""" Draw the Background image onto the passed in Surface object
		"""
		screen.blit (self._backgroundImage, (0, 0))
		
	def setBackgroundImage (self, imageName):
		""" Sets the Background to the passed in image file name
		"""
		try:
			self._backgroundImage = pygame.image.load(imageName)
			
		except pygame.error, message:
			print 'Cannot load image:', imageName
			raise SystemExit, message
			
		self._backgroundImage.convert()
