#!/usr/bin/python2

########################################################################
# File Name: 	Gameplay.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 1		2/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Gameplay module
########################################################################

import pygame

from Wall import *
from WallGroup import *
import os, sys
from Background import *
from Character import *
from Target import *
from TargetGroup import *
from pygame.locals import *

SCREEN_LENGTH = 900
SCREEN_WIDTH = 600
FONT_SIZE = 72
FONT_COLOR = (255,255,255)
SCORE_LOCATION =  25, 20
GAMEOVER_TEXT_LOCATION = 300, 250
CLICKSCREEN_TEXT_LOCATION = 210, 300
MAX_FRAME_RATE = 60


class Gameplay:
	
	def __init__ (self):
		""" Initializes gameplay object
		"""
		pygame.init()
		self._screen = pygame.display.set_mode ((SCREEN_LENGTH, SCREEN_WIDTH))	
		self._background = Background ()
		self._ninja = Character()
		self._targets = TargetGroup ()
		self._walls = WallGroup()
		self._clock = pygame.time.Clock()
		self._points = 0
		self._cutting = False
		self._kicking = False
		self._gameover = False
		
	def gameplayLoop (self):
		""" The main game loop
		"""
		while True:
			self._clock.tick (MAX_FRAME_RATE)
			
			# Draw background objects
			self._background.setSurfaceToBackground (self._screen)
			self._walls.draw (self._screen)
			
			# Update and draw targets and ninja
			if not self._gameover:
				if self._targets.update(not self._ninja.getIsMoving ()):
					self._gameover = True
				self._targets.draw (self._screen)
				self._ninja.update(self._walls)
				self._ninja.draw(self._screen)
			
				hitTarget = self._targets.checkForCollisions (self._ninja)
				
				if hitTarget is not -1:
					if (self._cutting and hitTarget.isRed ()) or \
					 (self._kicking and not hitTarget.isRed ()):
						hitTarget.kill ()
						self._points += 1
					else:
						self._gameover = True
			
			if not self._ninja.getIsMoving ():
				self._cutting = False
				self._kicking = False
			
			# Draw text 
			if pygame.font:
				font = pygame.font.Font (None, FONT_SIZE)
				score = font.render (str(self._points), 1, FONT_COLOR)
				textpos1 = score.get_rect ().move(SCORE_LOCATION)
				self._screen.blit (score, textpos1)
				
				if self._gameover:
					gameoverText = font.render ("GAME OVER", 1, FONT_COLOR)
					textpos2 = gameoverText.get_rect().move (GAMEOVER_TEXT_LOCATION)
					clickScreenText = font.render ("CLICK TO RESTART", 1, FONT_COLOR)
					textpos3 = clickScreenText.get_rect().move (CLICKSCREEN_TEXT_LOCATION)
					self._screen.blit (gameoverText, textpos2)
					self._screen.blit (clickScreenText, textpos3)
				
			pygame.display.update()
			
			# Event handler
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				if event.type == MOUSEBUTTONUP:
					if not self._kicking and not self._gameover: 
					#if not self._gameover:CHANGE BACK, TOOK OUT FOR EASIER DIRECTION TESTING
						x, y = pygame.mouse.get_pos()
						self._ninja.setDirection(x, y)
						self._ninja.rotateAndMove()
						self._ninja.setIsMoving(True)
						
						if not self._cutting:
							self._cutting = True
							self._ninja.setCharacterImage ("images/NinjaGame_SwordNinja.png")
							
						else:
							self._cutting = False
							self._kicking = True
							self._ninja.setCharacterImage ("images/NinjaGame_PunchNinja.png")
					
					# If game is over, reset the game		
					if self._gameover:
						self._ninja = Character()
						self._targets = TargetGroup ()
						self._clock = pygame.time.Clock()
						self._points = 0
						self._cutting = False
						self._kicking = False
						self._gameover = False
		
