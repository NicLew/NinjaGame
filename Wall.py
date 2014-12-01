#1/usr/bin/python2

########################################################################
# File Name: Wall.py
# Authors: Nicole Lewey and Jacob Lundgren
# Date: 12/08/2014
# Class: CS360 - Open Source
# Assignment: Ninja Game - Create Open Source Project
# Purpose: Class for Wall sprite object
########################################################################

import pygame

VERTICAL = 90

class Wall(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, vertical = False):
		"""Constructor for the wall object.
			Sets location to the passed in coordinates.
			If vertical is True, rotate the wall 90 degrees
		"""
		pygame.sprite.Sprite.__init__(self)
		try:
			self.image = pygame.image.load ('images/NinjaGame_Wall.png')
		except pygame.error, message:
			print 'Cannot load image: NinjaGame_Wall.png'
			raise SystemExit, message
		self.image.convert()
		
		if vertical:
			self.image = pygame.transform.rotate(self.image, VERTICAL)
		self.rect = self.image.get_rect().move (x, y)
			
		
	
