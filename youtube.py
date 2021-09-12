import pygame
import random

pygame.init()
# create window
# width, height
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('background.jpg')

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
enemyX = random.randint(0, 747)
enemyY = random.randint(50, 150)
enemyX_Change = 0.3
enemyY_Change = 30

# ready - cant see bullet
# fire - bullet is moving
bullet = pygame.image.load('bullet.png')
yesBullet = pygame.transform.scale(bullet, (20, 20))
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 0.5
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(yesBullet, (x + 15, y + 10))


# game loops
run = True
while run:
    screen.fill((215, 150, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 747:
        playerX = 747

    enemyX += enemyX_Change
    if enemyX <= 0:
        enemyX_Change = 0.2
        enemyY += enemyY_Change
    elif enemyX >= 747:
        enemyX_Change = -0.2
        enemyY += enemyY_Change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
