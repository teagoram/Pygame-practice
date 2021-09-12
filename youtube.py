import pygame
import random
import math

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


enemyImg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.transform.scale(pygame.image.load('ufo.png'), (50, 50)))
    enemyX.append(random.randint(0, 747))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(0.3)
    enemyY_Change.append(30)

    # ready - cant see bullet
    # fire - bullet is moving
bullet = pygame.image.load('bullet.png')
yesBullet = pygame.transform.scale(bullet, (20, 20))
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 0.5
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(yesBullet, (x + 15, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # player
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 747:
        playerX = 747

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] = 0.2
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 747:
            enemyX_Change[i] = -0.2
            enemyY[i] += enemyY_Change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    # collision

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
