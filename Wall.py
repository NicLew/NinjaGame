#1/usr/bin/python3

########################################################################
# File Name: Wall.py
# Authors: Nicole Lewey and Jacob Lundgren
# Date: 12/08/2014
# Class: CS360 - Open Source
# Assignment: Ninja Game - Create Open Source Project
# Purpose: Class for Wall sprite object
########################################################################

import pygame

class Wall(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0, vertical = False):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load ('NinjaGame_Wall.png').convert()
		if vertical:
			self.image = pygame.transform.rotate(self.image, 90)
		self.rect = self.image.get_rect().move (x, y)
			
		
	
