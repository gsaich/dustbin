#!/usr/bin/env python
"""
Bounce with sound
A Raspberry Pi test 2
"""

import time # for delays
import os, pygame, sys

pygame.init() # initialise graphics interface
pygame.mixer.quit()
pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 512)
bounceSound = pygame.mixer.Sound("sounds/bounce.ogg")
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce2")
screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background = pygame.Surface((screenWidth, screenHeight))

# define the colours to use for the user interface
cBackground = (0,0,0)
cBlock = (255,255,255)
background.fill(cBackground) # make background colour
box = [int(screenWidth - 80), int(screenHeight - 80)]
# boxFix = 0
delta = [5, 10]
hw = screenWidth / 2
hh = screenHeight / 2
position = [int(hw),int(hh)] # position of the ball
limit = [0, 0, 0, 0] # wall limits
ballRad = 8 # size of the ball

def main():
	global position
	updateBox(0,0) # set up wall limits
	screen.blit(background, [0,0])
	while True:
		checkForEvent()
		time.sleep(0.05)
		drawScreen(position[0], position[1])
		position = moveBall(position)

def moveBall(p):
	global delta
	p[0] += delta[0]
	p[1] += delta[1]
	if p[0] <= limit[0]:
		bounceSound.play()
		delta[0] = -delta[0]
		p[0] = limit[0]
	if p[0] >= limit[1]:
		bounceSound.play()
		delta[0] = -delta[0]
		p[0] = limit[1]
	if p[1] <= limit[2]:
		bounceSound.play()
		delta[1] = -delta[1]
		p[1] = limit[2]
	if p[1] >= limit[3]:
		bounceSound.play()
		delta[1] = -delta[1]
		p[1] = limit[3]
	return p
		
def drawScreen(px,py): # draw to the screen
#global p
	p = [int(px), int(py)]
	screen.blit(background, [0, 0]) # set background colour
	pygame.draw.rect(screen, (0,255,0), (hw - (box[0]/2), hh - (box[1]/2), box[0], box[1]), 2)
	pygame.draw.circle(screen, cBlock, (p[0], p[1]), ballRad, 2)
	pygame.display.update()
	
def updateBox(d, amount):
	global box, limit  # , boxFix
	box[d] += amount # not working, trying long hand
	
	limit[0] = hw - (box[0]/2) + ballRad # leftLimit
	limit[1] = hw + (box[0]/2) - ballRad # rightLimit	
	limit[2] = hh - (box[1]/2) + ballRad # topLimit
	limit[3] = (hh + (box[1]/2)) - ballRad # bottomLimit 
	
def terminate(): # close the program
	print("Closing down, please wait.")
	pygame.quit() # close the program
	sys.exit()
	
def checkForEvent(): # see if you need to quit
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		terminate()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			terminate()
		if event.key == pygame.K_DOWN: # expand / contract the box
			updateBox(1, -2)
		if event.key == pygame.K_UP:
			updateBox(1, 2)
		if event.key == pygame.K_LEFT:
			updateBox(0,-2)
		if event.key == pygame.K_RIGHT:
			updateBox(0,2)
		
if __name__ == '__main__':
	main()