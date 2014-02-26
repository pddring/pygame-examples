# pygame example: github.com/pddring/pygame-examples


"""
This example shows how to display text in different colours and fonts

for this to work, you'll need to download the font from: 
http://www.1001freefonts.com/five_dozen.font and extract FiveDozen.ttf into the same 
folder as this python file.


Things to try:
TODO: change the code so that all the text is red
TODO: change the code so that it displays "One", "Two" up to "Ten" rather than "Hello"
TODO: change the code so that the text appears in a different font
TODO: change the code so that the background colour is blue
TODO: change the code so that it displays 100 words instead of 50
"""
# import modules
import pygame
import random
import time


# show the pygame window
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Example")

# load the font
try:
    # ideally, try to load a fancy font
    font = pygame.font.Font("FiveDozen.ttf", 36)
except:
    # if FiveDozen.ttf can't be found, just a boring font instead
    print "Download and extract FiveDozen.ttf from http://www.1001freefonts.com/five_dozen.font and save it in this folder to use that font"
    font = pygame.font.Font(None, 36)

# list of messages
messages = ["Hello", "Goodbye", "Bonjour", "A bientot", "Hi", "Salut"]


# fill the screen in white
screen.fill((255, 255, 255))

# loop 50 times
for i in range(50):
    # choose a random messag
    msg = random.choice(messages)
    
    # create the text image in a random colour
    text = font.render(msg, True, (random.randint(0, 255),
                                   random.randint(0,255),
                                   random.randint(0,255)))
    
    # display the text in a random position
    screen.blit(text, (random.randint(0, 800),random.randint(0, 600)))
    
    # update the display and wait for 100ms (0.1s)
    pygame.display.flip()
    time.sleep(0.1)


pygame.quit()
