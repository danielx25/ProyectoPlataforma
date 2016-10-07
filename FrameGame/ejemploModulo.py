import pygame
from pygame.locals import *
import sys
from Motor.Personaje import *
from Motor.Fisica import *
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

    fuente = pygame.font.Font(None, 25)
    texto1 = fuente.render("Texto de pruebas", 0, (255, 255, 255))

    velocidad = 19
    angulo = 45
    gravedad = 9.8
    altura = 0
    tiempo = 2.1

    veloActual=0
    anguloActual=0

    x , y = (0,0)

    vx,vy = (0,0)

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

        cadena = "velocidad: "+str(velocidad)+ " Angulo: "+str(angulo) + " gravedad: "+str(gravedad)+ " altura: "+str(altura)
        x,y = mov_parabolico1(velocidad, altura, angulo, tiempo, gravedad)
        vx,vy = velocidad_InstanteXY(velocidad,angulo,tiempo,gravedad)
        veloActual=velocidad_Instante(vx,vy)
        anguloActual=angulo_actual(vx,vy)

        texto1 = fuente.render(cadena, 0, (255, 255, 255))
        texto2 = fuente.render("x: "+str(x), 0, (255, 255, 255))
        texto3 = fuente.render("y: "+str(y), 0, (255, 255, 255))
        texto4 = fuente.render("vx: " + str(vx), 0, (255, 255, 255))
        texto5 = fuente.render("vy: " + str(vy), 0, (255, 255, 255))
        texto6 = fuente.render("vActual: " + str(veloActual), 0, (255, 255, 255))
        texto7 = fuente.render("anguloActual: " + str(anguloActual), 0, (255, 255, 255))
        screen.blit(texto1,(10,10))
        screen.blit(texto2, (10, 30))
        screen.blit(texto3, (10, 50))
        screen.blit(texto4, (10, 70))
        screen.blit(texto5, (10, 90))
        screen.blit(texto6, (10, 110))
        screen.blit(texto7, (10, 130))
        #pygame.draw.rect(screen, blue, rect2)

        pygame.display.flip()
        print max_altura(velocidad, angulo, gravedad)


main()