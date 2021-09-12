import sys, os, pygame
pygame.init()

WIDTH = 600
HEIGHT = 500
BLUE = (0, 0, 255)
OK = (0, 255, 0)
NAME =  pygame.display.set_caption("Game")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.circle(SCREEN, OK, (3, 3), 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        else:
            print(event)
    SCREEN.fill(BLUE)
    pygame.display.flip()