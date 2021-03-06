#!/usr/bin/env python
"""
Here is the News
This is an Auto Cue Test 3 - reading a text file w/ controls
"""
import time #for delays
import os, pygame, sys

pygame.init()    # initialise graphics interface
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Auto Cue Test 3")
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
scrollSize = .5 #30
background.fill(cBackground) # make background colour
font = pygame.font.Font(None,textHeight)
numberOfLines = 0
newsLines = list()
fName = "news.txt" # name of the file to use
mirror = False
pause = False
anymore = False

def main():
#    print("Here is the news")
    global anymore
    while True: 
        getNews()
        lines=0
        while lines < numberOfLines:
            for i in range(segments, 0, -1): # shuffle up the text boxes
                textSurface[i] = textSurface[i-1]
            lines =setWords(lines,0)
            offset = 0
            while offset < textHeight:
                checkForEvent()
                if not pause:
                    drawScreen(offset)
                    offset += scrollSize
        anymore = False
        while not anymore:
            checkForEvent()
#        time.sleep(3.0)
#        terminate()
        
def getNews(): #opens new file
    global numberOfLines, newsLines
    numberOfLines = 0
    newsLines = list()
    nfile = open(fName, "r")
    for line in nfile.readlines():
        newsLines.append(line)
        numberOfLines += 1
    nfile.close()
    
def drawScreen(offset): # draw to the screen
    global segment
    screen.blit(background,[0,0]) #set background colour
    for index in range(0, segments+1):
        segment +=1
        if (segment > segments): # wraparound segment number
            segment = 0
        drawWords(segment, offset)
#        time.sleep(0.005) # slow it down
    pygame.display.update()
 
def setWords(index, segment):
#    print("I am setting Words")
    endOfLine = False
    margin = 30 # total gap for the two sides
    words = newsLines[index].split() # get an array of words from the line
    wordsAvailable = len(words)
    wordsToUse = 0
    wordsWidth = 0
    tryLine = " " #  the space between the quotes might be the source of my formatting bug
    while wordsWidth < screenWidth - margin and wordsAvailable >= wordsToUse + 1:
        tryLine = " "
        wordsToUse += 1
        for test in range(0, wordsToUse):
            tryLine = tryLine + words[test] + " "
        textSurface[segment] = font.render(tryLine, True, cText, cBackground)
        tryWidth = textSurface[segment].get_rect()
        wordsWidth = tryWidth.right
    useLine = " " #  the space between the quotes might be the source of my formatting bug
    if wordsWidth > screenWidth - margin: # for the end of the line
        wordsToUse -=  1 # use one less word
    else:
        endOfLine = True
    for test in range(0, wordsToUse): # build up the line you want
        useLine = useLine + words[test] + " "
        if len(useLine) > 3:
            useOne = useLine[1]
            useTwo = useLine[2]
            if useTwo is " ":
                if useOne is "a":
                    pass
                elif useOne is "A":
                    pass
                elif useOne is "I":
                    pass
                else:
                    useLine = " " + (useLine[2:])       
    textSurface[segment] = font.render(useLine, True, cText, cBackground)
    print("Using the line: - ", useLine)
    newsLines[index] = newsLines[index] [(len(useLine)-1) :] # The "-1" fixes a problem with clipping letters 
    # there is still a bug here it occurs when line buffering the -1 above corrects for leading letters being 
    # clipped during a transition - but it is leading to the appending of the last letter of
    # the previous block to the next line.  Should be fun to figure out.
    if endOfLine: # work on the next line next time
        index += 1
    return (index)  # try something to stop chopping text 

def drawWords(index, offset):
    textRect = textSurface[index].get_rect()
    textRect.centerx = screenWidth /2
    textRect.top = screenHeight - (textHeight * index) - offset
    if mirror:
        screen.blit(pygame.transform.flip(textSurface[index], True, False), textRect)
    else:
        screen.blit(textSurface[index], textRect)
    
def terminate():  # close down the program
#    print("Closing down please wait ")
    pygame.quit() # close pygame
    sys.exit()
    
def checkForEvent(): # see if you need to quit
#    print("I am checking For Events")
    global scrollSize, pause, anymore, fName, mirror
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
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_m:
                mirror = not mirror
            if event.key == pygame.K_0:
                anymore = True
                fName = "news.txt"
            if event.key == pygame.K_1:
                anymore = True    
                fName = "news1.txt"
            if event.key == pygame.K_2:
                anymore = True    
                fName = "news2.txt"
            if event.key == pygame.K_3:
                anymore = True    
                fName = "news3.txt"
                
if __name__ == '__main__':
    main()
    


 
    
             