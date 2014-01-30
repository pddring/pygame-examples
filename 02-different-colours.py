# pygame example: github.com/pddring/pygame-examples


"""
This example shows you how to experiment with different colours in pygame.
It will fill the whole pygame window in different colours

Here are some things to try to adapt the code:
TODO: Make the screen appear black
TODO: Make the screen appear blue
TODO: Make the screen appear yellow
"""
# import pygame module
import pygame

# show the pygame window
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame Example")

# fill the screen in white (Red = 255/255, Green = 255/255, Blue = 255/255)
screen.fill((255,255,255))

"""
Pygame doesn't draw directly to the screen. If it did, games would look messy
because you'd see each item being drawn one after the other, rather than
just seeing the whole game screen appear 'instantly'

Think of it like drawing a comic book scene on a piece of A4 paper.
You hold up the paper so everyone else can see the blank side whilst you draw
on the side facing you. When you've finished drawing your picture, you flip
over the paper so everyone can see the finished picture while you draw the next
scene on the other side.
"""
# update the display
pygame.display.flip()


# This stops the pygame window from closing straight away
raw_input("Press enter to go red")

# Fill the screen in red (Red = 255/255, Green = 0/255, Blue = 0/255)
screen.fill((255,0,0))
pygame.display.flip()
raw_input("Press enter to quit")

pygame.quit()
