import pygame

pygame.init()
# create window
screen = pygame.display.set_mode((800, 600))



# game loops
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            print(event)


