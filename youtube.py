import pygame
import random

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
playerX_Change = 0

enemyIMG = pygame.image.load('ufo.png')
enemyImg = pygame.transform.scale(enemyIMG, (50, 50))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loops
run = True
while run:
    screen.fill((215, 150, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 747:
        playerX = 747

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
