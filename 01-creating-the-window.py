# pygame example: github.com/pddring/pygame-examples


"""
This example isn't particularly exciting, it just shows you how to create
a pygame window. 

Here are some things you can do to adapt it:
TODO: Change the title of the window to My Game
TODO: Change the size of the window from 400 pixels wide and 300 pixels high to 800x600
"""
# import pygame module
import pygame

# show the pygame window
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame Example")


# This stops the pygame window from closing straight away
raw_input("Press enter to close")
pygame.quit()
