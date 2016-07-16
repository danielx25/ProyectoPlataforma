import pygame
from pygame.locals import *
import sys

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)


def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("tutorial pygame parte 2")

    rect1 = Rect(0, 0, 200, 200)
    rect2 = Rect(600, 0, 200, 200)
    rect3 = Rect(0, 0, 100, 100)
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if rect1.colliderect(rect2):
                    print "estan colisionando"

        pygame.draw.rect(screen, red, rect1)
        pygame.draw.rect(screen, green, rect2)
        pygame.draw.rect(screen, darkBlue, rect3)

        pygame.display.flip()


main()