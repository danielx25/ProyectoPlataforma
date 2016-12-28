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

    puntero = Circulo()#

    rect1 = Rect(0, 0, 300, 200)
    rect2 = Rect(300, 200, 500, 100)
    print "ancho"+ str(rect2.size[0])
    print "alto" + str(rect2.size[1])
    rect3 = Rect(0, 0, 100, 100)

    fuente = pygame.font.Font(None, 25)

    circulo = Circulo()

    grupo = pygame.sprite.Group()
    grupo.add(circulo.sprite)
    grupo.add(puntero.sprite)

    #circulo.sprite.rect = circuloRectangulo(circulo.radio)

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

        x, y=pygame.mouse.get_pos()
        puntero.posicion(x, y)
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

        pygame.draw.rect(screen, red, plataforma.rectangulo)
        #pygame.draw.rect(screen, blue, rect2)

        circulo.imprimir(screen)
        #puntero.imprimir(screen)
        circulo.creandoCirculo()
        #puntero.creandoCirculo()

        grupo.update()
        lista = pygame.sprite.spritecollide(puntero.sprite, grupo, False, pygame.sprite.collide_circle_ratio(1.4))
        print len(lista)
        if len(lista)>1:#pygame.sprite.collide_circle(puntero.sprite, circulo.sprite):
            pygame.draw.rect(screen, darkBlue, puntero.sprite.rect)


        pygame.display.flip()
        #print max_altura(velocidad, angulo, gravedad)




class Circulo(object):
    def __init__(self):
        self.sprite = pygame.sprite.Sprite()
        self.radio = 100
        self.x = 100
        self.y = 100
        self.tamx = 400
        self.tamy = 400
        self.sprite.rect = Rect(self.x, self.y, self.tamx, self.tamy)
        self.radio = int(math.sqrt(math.pow(self.sprite.rect.width,2)+math.pow(self.sprite.rect.height,2))/2.0)
        self.x_circulo = 0
        self.y_circulo = 0
        #self.sprite.radius = self.radio
        self.terminar = False
        self.otro = []#Rect(0, 0, self.tamx, self.tamy)]

    def imprimir(self, pantalla):
        self.x_circulo = int(self.x+self.sprite.rect.width/2.0)
        self.y_circulo = int(self.y + self.sprite.rect.height / 2.0)
        pygame.draw.rect(pantalla, green, self.sprite.rect, 2)
        pygame.draw.circle(pantalla, red, (self.x_circulo, self.y_circulo), self.radio, 2)
        radio2 = 0
        if self.tamx<self.tamy:
            radio2=self.tamx/2
        else:
            radio2=self.tamy/2
        pygame.draw.circle(pantalla, red, (self.x_circulo, self.y_circulo), radio2, 2)
        for i in self.otro:
            pygame.draw.rect(pantalla, white, i, 1)

    def posicion(self, x, y):
        self.x=self.sprite.rect.left = x
        self.y=self.sprite.rect.top = y


    def colicion(self, circulo2):
        return collision(self.x, self.y, self.tamx, self.tamy, circulo2.x_circulo, circulo2.y_circulo, circulo2.radio)

    def creandoCirculo(self):
        if self.terminar == False:
            self.terminar = True
            self.opuesto = 0
            num_division = 5

            for i in range(num_division):
                self.opuesto += self.radio / num_division
                self.adyacente = math.sqrt(math.pow(self.radio, 2) - math.pow(self.opuesto, 2))
                self.otro.append(
                    Rect(self.x_circulo - self.adyacente, self.y_circulo, self.adyacente * 2,
                         self.opuesto))
            self.opuesto = 0
            for i in range(num_division):
                self.opuesto += self.radio / num_division
                self.adyacente = math.sqrt(math.pow(self.radio, 2) - math.pow(self.opuesto, 2))
                self.otro.append(
                    Rect(self.x_circulo - self.adyacente, self.y_circulo - self.opuesto, self.adyacente * 2,
                         self.opuesto))







def circuloRectangulo(radio, division = 5.0):
    opuesto = radio/division
    adyacente = math.sqrt(math.pow(radio, 2)-math.pow(opuesto,2))
    cuadrado=Rect(0, 0, adyacente*2, opuesto)
    return  cuadrado
main()