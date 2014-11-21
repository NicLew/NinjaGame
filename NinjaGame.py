#!/usr/bin/python3

########################################################################
# File Name: 	NinjaGame.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 1		2/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Main for the Ninja Game
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

def main():
	pygame.init()
	screen = pygame.display.set_mode ((SCREEN_LENGTH, SCREEN_WIDTH))	
	background = Background ()
	ninja = Character()
	targets = TargetGroup ()
	walls = WallGroup()
	
	background.setSurfaceToBackground(screen)
	clock = pygame.time.Clock()

	while True:
		clock.tick (60)
		background.setSurfaceToBackground (screen)
		targets.draw (screen)
		targets.update()
		walls.draw (screen)
		ninja.draw(screen)
		ninja.update(walls)
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == MOUSEBUTTONUP:
				ninja.setIsMoving(True)
				ninja.move(walls)

# invoke main()
if __name__=="__main__":
	main()
