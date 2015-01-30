"""
this pygame helper library is designed to help people easily switch from
from text based programs to pygame programs

Source: https://github.com/pddring/pygame-examples
"""

import pygame



"""
Displays text at a given position. 
This is designed as a pygame replacement for print

e.g:
    
from pygame_helper import *
# set up pygame
pygame.init()

# set up the screen in 800 x 600 resolution
screen = pygame.display.set_mode((800,600))

# fill the screen in white
screen.fill((255,255,255)) 

# display hello in red, size 30 at x=100, y=100
print_at(screen, (100,100), "Hello!", 30, (255,0,0))

# update the display
pygame.display.flip()

# pause before quitting
wait_for_key()

"""
def print_at(screen, pos, message, size, color):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, color)
    screen.blit(text, pos)
    
"""
Prompt the user to enter some text
Designed as a pygame replacement for raw_input

e.g. 

from pygame_helper import *
# set up pygame
pygame.init()

# set up the screen in 800 x 600 resolution
screen = pygame.display.set_mode((800,600))

# fill the screen in white
screen.fill((255,255,255)) 

# ask the user's name
name = raw_input_at(screen, (0,0), (0, 20, 200, 20), "What is your name?", 20, (0,0,0)) 
print_at(screen, (0,100), "Hello " + name, 30, (0,0,0))

# update the display
pygame.display.flip()

# pause before quitting
wait_for_key()

"""

def raw_input_at(screen, message_pos, prompt_rect, message, size, color):
    # draw message
    font = pygame.font.Font(None, size)
    text = font.render(message, True, color)
    screen.blit(text, message_pos)
    
    string = ""
    # draw input box
    while True:
        pygame.draw.rect(screen, (0,0,0), prompt_rect, 0)
        text = font.render(string + "_", True, (255,255,255))
        screen.blit(text, prompt_rect)
        pygame.display.flip()
    
        key = wait_for_key()
        
        # stop waiting for key presses if the user presses enter
        if key == pygame.K_RETURN or key == pygame.K_ESCAPE:
            return string
        
        # go back one character if the user presses backspace
        elif key == pygame.K_BACKSPACE:
            string = string[:-1]
        else:
            try:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    string += chr(key).upper()
                else:
                    string += chr(key)
            except:
                pass

"""
wait for the user to press a key and return the keycode
e.g.
key_pressed = wait_for_key()
print("You pressed" + chr(key_pressed))
"""
def wait_for_key():
    e = pygame.event.wait()
    while e.type != pygame.KEYDOWN:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            exit()
    return e.key
