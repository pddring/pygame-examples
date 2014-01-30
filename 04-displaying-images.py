# pygame example: github.com/pddring/pygame-examples


"""
This example shows you how to load an image from a file and display it on
the screen. You can press the up or down arrows to move the image.
This code will need an image called "pygame.png" in a folder called images.

Things to try:
TODO: change the code so that it displays a different image
TODO: change the code so that it can move with the left and right arrows too.
TODO: change the code so that it doesn't move off the edge of the screen.
TODO: make the code display two images. One moves with the arrow keys and one moves with WASD
"""
# import modules
import pygame

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
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Example")

# load image
img_logo = pygame.image.load("images/pygame.png")

# set image coordinates
x = 0
y = 0

# loop around until the user presses escape or Q
looping = True
while looping:
    
    # fill the screen in white
    screen.fill((255, 255, 255))

    # blit copies an image onto the screen
    screen.blit(img_logo, (x,y))
    pygame.display.flip()

    # wait for a key to be pressed
    key = wait_for_key()

    # stop looping if the user presses Q or escape
    if key == pygame.K_q or key == pygame.K_ESCAPE:
        looping = False

    # move the image
    elif key == pygame.K_UP:
        y -= 10
    elif key == pygame.K_DOWN:
        y += 10

pygame.quit()
