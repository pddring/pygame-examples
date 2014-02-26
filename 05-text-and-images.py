# pygame example: github.com/pddring/pygame-examples


"""
This example shows you how to display text and combine it with images
in the pygame graphics window.

Things to try:
TODO: Change the "Press Q to quit" from red to blue
TODO: Make "Press Q to quit" appear at the bottom of the screen in the middle
TODO: "Press any key..." is displayed nice and smoothly but "Press Q..." is
        all blotchy. This is because "Press any key..." uses anti-aliasing.
        Make "Press Q..." use anti-aliasing too so that it displays smoothly too.
TODO: Add a joker to the pack

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
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Example")

# load images
try:
    img_card = pygame.image.load("images/card-back.png")
    img_heart = pygame.image.load("images/card-heart.png")
    img_club = pygame.image.load("images/card-club.png")
    img_spade = pygame.image.load("images/card-club.png")
    img_diamond = pygame.image.load("images/card-diamond.png")
except:
    print "Error: Could not load images: you can download them from github.com/pddring/pygame-examples"
    print "They should be saved in a folder called images in the same place as this python file"
    exit()
    
images_suits = [img_heart, img_club, img_spade, img_diamond]

# create a font
font = pygame.font.Font(None, 36)

# use the font to make an image containg some text
text = font.render("Press any key to show a random card", True, (0, 0, 0))
text_quit = font.render("Press Q to quit", False, (255, 0, 0))

# loop around until the user presses escape or Q
looping = True
while looping:
    
    # fill the screen in white
    screen.fill((255, 255, 255))

    # display the card
    screen.blit(img_card, (100,100))
    screen.blit(text, (0,0))
    screen.blit(text_quit, (0,400))
    
    # update the screen
    pygame.display.flip()

    # display a white rectangle over the centre of the card
    pygame.draw.rect(screen, (255,255,255), (110, 110, 180, 260), 0)

    # choose a suit at random
    suit = random.choice(images_suits)
    screen.blit(suit, (130, 150))

    # choose a number at random
    number = random.choice(["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
    screen.blit(font.render(number, 1, (0, 0, 0)), (120, 120))
    pygame.display.flip()

    key = wait_for_key()

    # stop looping if the user presses Q or escape
    if key == pygame.K_q or key == pygame.K_ESCAPE:
        looping = False


pygame.quit()
