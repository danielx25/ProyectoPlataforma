from  Motor.Personaje import Personaje
import pygame


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))

    p = Motor.Personaje.Personaje()

    pygame.display.set_caption("ProyectoPlataforma")
    reloj1 = pygame.time.Clock()
    salir = False

    while salir == False:

        lista = pygame.event.get()
        for event in lista:
            if event.type == pygame.QUIT:
                salir = True
        pantalla.fill((0, 0, 240))
        reloj1.tick(60)
        pygame.display.update()
    pygame.quit()


main()
