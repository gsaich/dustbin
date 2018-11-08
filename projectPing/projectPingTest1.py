#!/usr/bin/env python
"""
Bounce
A Rasperry Pi test
"""

import time # for delays
import os, pygame, sys

pygame.init() # initialise graphics interface
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce")
screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background = pygame.Surface((screenWidth, screenHeight))

# define the colours to use for the user interface
cBackground = (0,0,0)
cBlock = (255,255,255)
background.fill(cBackground) # make background colour
dx =5
dy =10

def main():
	X = screenWidth /2
	Y = screenWidth /2
	screen.blit(background, [0,0])
	while True:
		checkForEvent()
		time.sleep(0.05)
		drawScreen(X,Y)
		X += dx
		Y += dy
		checkBounds(X,Y)
		
def checkBounds(px, py):
	global dx, dy
	if px > screenWidth - 10 or px < 0:
		dx = -dx
	if py > screenHeight -10 or py < 0:
		dy = -dy
		
def drawScreen(px, py): # draw to the screen
	screen.blit(background, [0, 0]) # set background colour
	pygame.draw.rect(screen, cBlock, (px, py, 10, 10), 0)
	pygame.display.update()
	
def terminate(): # close the program
	print("Closing down, please wait.")
	pygame.quit() # close the program
	sys.exit()
	
def checkForEvent(): # see if you need to quit
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		terminate()
	if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
		terminate()
		
if __name__ == '__main__':
	main()