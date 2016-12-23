import pygame
from pygame.locals import *
import sys
from Motor.Personaje import *
from Motor.Plataforma import *
from Motor.DeteccionColisiones import *
from Motor.Fisica import *
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
import math

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("tutorial pygame parte 2")

    p1 = Personaje()
    p1._x =100
    p1._y = 500
    p1.tam_rectangulos((50,50))
    p1.actualizacionRec()


    p2 = Personaje()
    p2._x = 100
    p2._y = 400
    p2.tam_rectangulos((50, 50))
    p2.actualizacionRec()

    plataforma = Plataforma()
    plataforma.setXY(0, 554)
    plataforma.setTamRect(800, 70)

    puntero = Rect(0, 0, 100, 100)

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
    tiempo = 0.9

    veloActual=0
    anguloActual=0

    x , y = (0,0)

    vx,vy = (0,0)

    circulo = Circulo()

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                p1.setSalto(True)
                p2.setCorrer(True, False)
                if rect1.colliderect(rect2):
                    print "estan colisionando"

        puntero.left, puntero.top=pygame.mouse.get_pos()
        p1.saltando()
        p1.actualizacionRec()
        p1.runGanancia2()
        #p1.runGanancia2()

        p2.corriendo()
        #p2.setGananciaXY(p1.getGananciaXY())
        #p2.setGananciaXY((1, -1))
        p2.actualizacionRec()
        p2.runGanancia2()

        deteccionColisiones([p1,p2], [plataforma], None)

        screen.fill((0,0,240))
        pygame.draw.rect(screen, red, p1.rec1)
        pygame.draw.rect(screen, darkBlue, p1.rec3)
        pygame.draw.rect(screen, green, p1.rec2)
        pygame.draw.rect(screen, blue, p1.rec4)

        pygame.draw.rect(screen, red, p2.rec1)
        pygame.draw.rect(screen, darkBlue, p2.rec3)
        pygame.draw.rect(screen, green, p2.rec2)
        pygame.draw.rect(screen, blue, p2.rec4)
        pygame.draw.rect(screen, pink, puntero)

        pygame.draw.rect(screen, red, plataforma.rectangulo)

        texto1 = fuente.render("Proyecto en plataforma", 0, (255, 255, 255))
        texto2 = fuente.render("x: "+str(p1.getEjeX()), 0, (255, 255, 255))
        texto3 = fuente.render("y: "+str(p1.getEjeY()), 0, (255, 255, 255))
        texto4 = fuente.render("vx: " + str(p1.getStatus("velocidad x")), 0, (255, 255, 255))
        texto5 = fuente.render("vy: " + str(p1.getStatus("velocidad y")), 0, (255, 255, 255))
        texto6 = fuente.render("vActual: " + str(p1.getStatus("velocidad")), 0, (255, 255, 255))
        texto7 = fuente.render("anguloActual: " + str(p1.getStatus("angulo")), 0, (255, 255, 255))
        texto8 = fuente.render("gananciaxy: " + str(p1.getDiferenciaXY()), 0, (255, 255, 255))
        screen.blit(texto1,(10,10))
        screen.blit(texto2, (10, 30))
        screen.blit(texto3, (10, 50))
        screen.blit(texto4, (10, 70))
        screen.blit(texto5, (10, 90))
        screen.blit(texto6, (10, 110))
        screen.blit(texto7, (10, 130))
        screen.blit(texto8, (10, 150))
        #pygame.draw.rect(screen, blue, rect2)
        circulo.imprimir(screen)
        pygame.display.flip()
        #print max_altura(velocidad, angulo, gravedad)




class Circulo(object):
    def __init__(self):
        self.sprite = pygame.sprite.Sprite()

        self.radio = 100
        self.x = 100
        self.y = 200
        self.sprite.rect = Rect(self.x, self.y, 100, 200)
        self.radio = int(math.sqrt(math.pow(self.sprite.rect.width,2)+math.pow(self.sprite.rect.height,2))/2.0)

    def imprimir(self, pantalla):
        x_circulo = int(self.x+self.sprite.rect.width/2.0)
        y_circulo = int(self.y + self.sprite.rect.height / 2.0)
        pygame.draw.rect(pantalla, green, self.sprite.rect)
        pygame.draw.circle(pantalla, red, (x_circulo, y_circulo), self.radio, 2)

        #circle(Surface, color, pos, radius, width=0)

main()