import pygame
from pygame.locals import *
import sys
from Motor.Personaje import *

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)


def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("tutorial pygame parte 2")

    p1 = Personaje()
    p1.tam_rectangulos((100,100))
    p1.pos_rectangulos(200,200, 100,100)

    rect1 = Rect(0, 0, 300, 200)
    rect2 = Rect(300, 200, 500, 100)
    print "ancho"+ str(rect2.size[0])
    print "alto" + str(rect2.size[1])
    rect3 = Rect(0, 0, 100, 100)
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if rect1.colliderect(rect2):
                    print "estan colisionando"

        pygame.draw.rect(screen, red, p1.rec1)
        pygame.draw.rect(screen, darkBlue, p1.rec3)
        pygame.draw.rect(screen, green, p1.rec2)
        pygame.draw.rect(screen, blue, p1.rec4)

        #pygame.draw.rect(screen, blue, rect2)

        pygame.display.flip()


main()