# import
import pygame
# width and height
WIDTH, HEIGHT = 900, 500
# main surface/make window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# window name
pygame.display.set_caption("First Game")



# game loop
def main():
    # run over and over so we can update
    run = True
    while run:
        # get all the events in the loop
        for event in pygame.event.get():
            # if the user quits run is false
            if event.type == pygame.QUIT:
                run = False
    # if run is false then while wont run and pygame will quit
    pygame.quit()

 # run if only in file
if __name__ == "__main__":
    main()
    