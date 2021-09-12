import pygame
pygame.init()
# create window
# width, height
screen = pygame.display.set_mode((800, 600))


# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerIMG = pygame.image.load('spaceship.png')
playerImg = pygame.transform.scale(playerIMG, (50, 50))
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))


# game loops
run = True
while run:
    screen.fill((215, 150, 0))

    playerY -= 0.1
    print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            print(event)

    player(playerX, playerY)
    pygame.display.update()

