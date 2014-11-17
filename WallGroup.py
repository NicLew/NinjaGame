#1/usr/bin/python3

########################################################################
# File Name: WallGroup.py
# Authors: Nicole Lewey and Jacob Lundgren
# Date: 12/08/2014
# Class: CS360 - Open Source
# Assignment: Ninja Game - Create Open Source Project
# Purpose: Sets up 4 walls in a sprite group and provides functions
#			for that sprite group
########################################################################

import pygame
from Wall import *

class WallGroup:
	def __init__(self, screen):
		"""Constructor for the WallGroup object
			Sets the sprite group to hold the top, right, bottom,
			and left walls. 
		"""
		self._walls = pygame.sprite.Group()
		topWall = Wall()
		rightWall = Wall (880, 0, True)
		bottomWall = Wall(0, 580)
		leftWall = Wall(0, 0, True)
		self._walls.add (topWall)
		self._walls.add (rightWall)
		self._walls.add (bottomWall)
		self._walls.add (leftWall)
	
	def draw (self, screen):
		""" Draws the walls to the screen
		"""
		self._walls.draw(screen)
		
	def checkForCollisions (self, checkedSprite):
		""" Checks if the passed in sprite collides with any of the 
			walls.
			If a collision is found, return the wall that is being
			collided into. Otherwise, return -1.
		"""
		for wall in self._walls.sprites():
			if pygame.sprite.collide_rect(checkedSprite, wall):
				return wall
		return -1
		
	
