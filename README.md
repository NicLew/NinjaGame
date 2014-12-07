NinjaGame
=========

###Description

Ninja Game is coded in Python and involves controlling the ninja by having him jump from wall to wall. When
the user clicks, the ninja will jump in the direction of the click. The user can click
a second time to change the ninja's direction and attack type midair. The ninja's first jump will include a sword attack, and his midair
direction change will include a punching attack. The game will have targets that require
different attacks to hit. The goal will be to get every target that appears. If you hit a target with the incorrect attack
type or you let a target time out, you die!

###How to Build and Run the Code

1. Download and install Python 2.7 (https://www.python.org/downloads/)
2. Download and install pygame and pygame documentation on OpenSUSE. Run the following commands in your terminal:

	```sudo zypper install python-pygame```
	
	```sudo zypper install python-pygame-doc```
	
3. Fork the cs360f14/NinjaGame repository to your personal GitHub account.
4. Clone your personal copy of NinjaGame to your computer, replacing USERNAME with your GitHub user name:

	```git clone git@github.com:USERNAME/NinjaGame.git```

5. To run the game, type `python2 NinjaGame.py` in the terminal.
6. To run unit tests, type `python2 -m unittest [Unit Test Module Name]` in the terminal. (For example, `python2 -m unittest CharacterUnitTests`)

###Dependencies

Pygame (1.9.1)

###How to Contribute

If you wish to contribute to the project, go for it! 

#####Bug Reporting

If you wish to file a bug report, please open a GitHub Issue marked as a bug. Here are the things you should include:
* A clear description of the bug you found
* Screenshots where applicable and possible
* Clear instructions on how to replicate the bug, if known
* Where in the code you think the bug may be originating
* If the bug causes the game to crash, show terminal logs

If you wish to fix a bug, choose from the list of GitHub Issues marked as bugs, assign yourself, fix it, and follow instuctions for making a pull request.

#####Adding a Feature
If you wish to add a new feature, these are the steps you should take:

1. Choose from the list of additional features we have listed or imagine your own!

2. If you choose from our list of features, look up the enhancement in GitHub Issues. There you should find a detailed description of what we envision that feature being. Assign yourself that issue to show that it is claimed. If you still have questions, email us at cs.ninja.game@gmail.com.

3. If you imagine your own new feature, email us at cs.ninja.game@gmail.com to get permission to go forward. In this email provide: a clear description of the feature you would like to add, why this feature would improve the game, and an overview of your intended design.

4. If your feature adds any new media (such as new images or sounds), make sure they are under compatible licenses.

List of additional features we would like:
* Fix issue with pygame hit boxes
* Title screen
* Levels/Difficulty curve
* More possible moves
* Targets you should not hit
* Gamemodes
* Choose your character option
* Tracking statistics
* Music and sound effects
* Enhance graphics
* Adding documentation to the wiki

#####Making a Pull Request
Once you have made changes (by either fixing a bug or adding a feature), create a pull request. For your pull request to be merged, follow these guidelines:
* A pull request from outside contributor must have at least two positive reviews
* A pull request must be merged by one of the project leads.
* Please follow Python coding standards (https://www.python.org/dev/peps/pep-0008/) and use PyDocs for all of your functions. Your pull request will not be merged without proper documentation. 
* Write unit tests for all functions, where possible, and make sure all tests are passing before submitting your pull request. We will run your tests before merging.

If you follow all of these guidelines, you will be a successful contributor to our project!

###Goals
Our main goal with this project is to create a fun open source game that we and others can use and contribute to.
Things we would especially like to see in the future:
* Fix issue with pygame hit boxes
* Add sound effects and music
* Balance difficulty curve
* Enhance resolution of images

###Contact Information
If you have any questions, email us at cs.ninja.game@gmail.com or comment on the relevant issue or pull request.

###System information

This code has been tested on a OpenSUSE 13.1 64 bit Operating System.

###Documentation

At this point, all documentation is in the code.

###License Information

This software is under the GNU General Public License (GPL)

All images in this game are licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0): http://creativecommons.org/licenses/by-nc/4.0/


![alt text](https://github.com/cs360f14/NinjaGame/blob/master/images/GameScreenshot.png "Game Screenshot")
