#!/usr/bin/python2

########################################################################
# File Name: 	NinjaGame.py
# Authors: 		Nicole Lewey and Jacob Lundgren
# Date: 1		2/08/2014
# Class: 		CS360 - Open Source
# Assignment: 	Ninja Game - Create Open Source Project
# Purpose: 		Main for the Ninja Game
########################################################################

from Gameplay import *

SCREEN_LENGTH = 900
SCREEN_WIDTH = 600

def main():
	""" The main of Ninja Game
	"""
	gameplay = Gameplay ()
	gameplay.gameplayLoop ()
	

# invoke main()
if __name__=="__main__":
	main()
