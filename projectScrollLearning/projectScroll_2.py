#!/usr/bin/env python
"""
Here is the News
This is an Auto Cue Test 2 - reading a text file
"""
import time #for delays
import os, pygame, sys
from _operator import index

pygame.init()    # initialise graphics interface
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Auto Cue test 1")
screenWidth = 980
screenHeight = 610
screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background = pygame.Surface((screenWidth,screenHeight))
segments = 4
segment = 0 # initial start place
textHeight = int((screenHeight / segments)/1) # /n is for text scaling
textSurface = [pygame.Surface((screenWidth, screenHeight)) for s in range(0, segments+1)]

# define the colours to use for the user interface
cBackground =(0,0,0)
cText = (255,255,255)
scrollSize = 30
background.fill(cBackground) # make background colour
font = pygame.font.Font(None,textHeight)
numberOfLines = 0
newsLines = list()

def main():
    print("Here is the news")
    getNews()
    lines=0
    while lines < numberOfLines:
        for i in range(segments, 0, -1): # shuffle up the text boxes
            textSurface[i] = textSurface[i-1]
        lines =setWords(lines,0)
        offset = 0
        while offset < textHeight:
            checkForEvent()
            print("I am about to call draW Screen")
            drawScreen(offset)
            print("I just finisshed call to drawScreen")
            offset += scrollSize
    time.sleep(10.0)
    terminate()
        
def getNews(): #opens new file
    print("I am getting news")
    global numberOfLines, newsLines
    nfile = open("news.txt", "r")
    for line in nfile.readlines():
        newsLines.append(line)
        numberOfLines += 1
    nfile.close()
    
def drawScreen(offset): # draw to the screen
    print("I am drawing the screen")
    global segment
    screen.blit(background,[0,0]) #set background colour
    for index in range(0, segments+1):
        segment +=1
        if (segment > segments): # wraparound segment number
            segment = 0
        drawWords(segment, offset)
        print("I just finished draWords - going to display update")
    time.sleep(0.1) # slow it down
    pygame.display.update()
    print("I ran display update")
    
def setWords(index, segment):
    print("I am setting Words")
    endOfLine = False
    margin = 30 # total gap for the two sides
    words = newsLines[index].split() # get an array of words from the line
    wordsAvailable = len(words)
    wordsToUse = 0
    wordsWidth = 0
    tryLine = " "
    while wordsWidth < screenWidth - margin and wordsAvailable >= wordsToUse + 1:
        tryLine = " "
        wordsToUse += 1
        for test in range(0, wordsToUse):
            tryLine = tryLine + words[test] + " "
        textSurface[segment] = font.render(tryLine, True, cText, cBackground)
        tryWidth = textSurface[segment].get_rect()
        wordsWidth = tryWidth.right
        print(tryLine, " -> is ", wordsWidth, " pixels wide")
    useLine = " "
    if wordsWidth > screenWidth - margin: # for the end of the line
        wordsToUse -=  1 # use one less word
    else:
        endOfLine = True
    for test in range(0, wordsToUse): # build up the line you want
        useLine = useLine + words[test] + " "
    textSurface[segment] = font.render(useLine, True, cText, cBackground)
    print("Using the line: - ", useLine)
    print()
    newsLines[index] = newsLines[index] [(len(useLine)-1) :] # The "-1" fixes a problem with clipping letters 
    # there is still a bug here it occurs when line buffering the -1 above corrects for leading letters being 
    # clipped during a transition - but it is leading to the appending of the last letter of
    # the previous block to the next line.  Should be fun to figure out.
    if endOfLine: # work on the next line next time
        index += 1
    return (index)  # try something to stop chopping text 

def drawWords(index, offset):
    print("I am drawing Words")
    textRect = textSurface[index].get_rect()
    textRect.centerx = screenWidth /2
    textRect.top = screenHeight - (textHeight * index) - offset
    screen.blit(textSurface[index], textRect)
    print("I made it to here " + str(index), str(offset))
    
def terminate():  # close down the program
    print("Closing down please wait ")
    pygame.quit() # close pygame
    sys.exit()
    
def checkForEvent(): # see if you need to quit
    print("I am checking For Events")
    global scrollSize
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        terminate()
    if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 terminate()
             if event.key == pygame.K_DOWN:
                 scrollSize -= 1
                 if scrollSize == 0:
                     scrollSize = 1
             if event.key == pygame.K_UP:
                scrollSize += 1
                
if __name__ == '__main__':
    main()
    


 
    
             