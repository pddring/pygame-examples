# pygame example: github.com/pddring/pygame-examples


"""
Examples 1 and 2 have used raw_input to get keyboard input. This is irritating,
because you have to click on the console window before typing anything rather
thank pressing a key when the pygame window is active.

This example shows you how to detect key presses in pygame
"""
# import modules
import pygame
import random

# wait for the user to press a key and return the keycode
def wait_for_key():
    e = pygame.event.wait()
    while e.type != pygame.KEYDOWN:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            return pygame.K_ESCAPE
    return e.key


# show the pygame window
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Pygame Example")

# loop around until the user presses escape or Q
looping = True
while looping:
    # choose a random colour
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # fill the screen in the random colour
    screen.fill((red, green, blue))
    pygame.display.flip()

    # wait for a key to be pressed
    key = wait_for_key()

    # stop looping if the user presses Q or escape
    if key == pygame.K_q or key == pygame.K_ESCAPE:
        looping = False

pygame.quit()
