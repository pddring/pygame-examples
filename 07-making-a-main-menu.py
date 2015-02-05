# pygame example: github.com/pddring/pygame-examples


"""

This example shows how you can create a main menu using 
print_at() and raw_input_at() functions

It will show a main menu with 4 options:
1: Change main menu title colour
2: Change menu option text colour
3: Load and display an image
Q: Quit

Here are some things you can do to adapt it:
TODO: Change the background colour to red, blue or green
TODO: Add an additional menu option (4) to display a random number between 1 and 10
TODO: Change option (3) so that it asks you the x and y coordinates to display the image
TODO: Change option (3) so that you can move the image left/right/up/down with the arrow keys
"""

try:
    from pygame_helper import *
except:
    print "You need to download pygame_helper.py from https://github.com/pddring/pygame-examples"
    exit() 
    
# set up pygame
pygame.init()

# set up the screen in 800 x 600 resolution
screen = pygame.display.set_mode((800,600))

import random

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


text_color = random_color()
title_color = random_color()

# main menu
while True:
    # fill the screen in random colour
    screen.fill((255,255,255))
    
    print_at(screen, (200, 200), "Main menu:", 50, title_color)
    print_at(screen, (200, 250), "1: Change text colour", 20, text_color)
    print_at(screen, (200, 275), "2: Change title colour", 20, text_color)
    print_at(screen, (200, 300), "3: Load image", 20, text_color)
    print_at(screen, (200, 325), "Q: Quit", 20, text_color)

    option = raw_input_at(screen, (100, 400), (160, 400, 200, 20), "Choice:", 20, (0, 0, 0))
    
    # Quit
    if option == "Q":
        break
    
    # Change option text colour
    elif option =="1":
        text_color = random_color()
        
    # change title text colour
    elif option == "2":
        title_color = random_color()
    
    # load image
    elif option == "3":
        
        # ask for the filename
        screen.fill((255,255,255))
        filename = raw_input_at(screen, (0, 0), (0, 50, 800, 20),  "Filename", 20, (0,0,0))
        
        # attempt to load the file
        try:
            img = pygame.image.load(filename)
            screen.blit(img, (0,100))
            pygame.display.flip()
        except:
            print_at(screen, (0, 100), filename + " could not be found", 20, (255,0,0))
        
        # wait for user to press a key
        wait_for_key()
