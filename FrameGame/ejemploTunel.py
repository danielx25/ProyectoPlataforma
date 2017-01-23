import pygame
from pygame.locals import *
import sys
from Motor.Personaje_ import *
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
    p1.x_antes = 100
    p1.y_antes = 300
    p1._x =700
    p1._y = 100
    p1.tam_rectangulos((70,70))
    p1.actualizacionRec()


    p2 = Personaje()
    p2._x = 100
    p2._y = 200
    p2.tam_rectangulos((100, 100))
    p2.actualizacionRec()

    plataforma = Plataforma()
    plataforma.setXY(0, 554)
    plataforma.setTamRect(800, 70)

    rectangulo = Plataforma()
    rectangulo.setXY(650, 100)
    rectangulo.setTamRect(40, 300)

    puntero = Circulo(p1._x, p1._y, p1.ancho, p1.largo)

    rect1 = Rect(0, 0, 300, 200)
    rect2 = Rect(300, 200, 500, 100)
    print "ancho"+ str(rect2.size[0])
    print "alto" + str(rect2.size[1])

    fuente = pygame.font.Font(None, 25)



    grupo = pygame.sprite.Group()
    grupo.add(puntero.sprite)

    #circulo.sprite.rect = circuloRectangulo(circulo.radio)
    lista1 =[]
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                lista1 =deteccionEfectoTunel(p1, rectangulo)

                #p1.setSalto(True)
                #p2.setCorrer(True, False)
                #if rect1.colliderect(rect2):
                #    print "estan colisionando"

        lista1 = deteccionEfectoTunel(p1, rectangulo)
        x, y=pygame.mouse.get_pos()
        puntero.posicion(x, y)
        #p1.saltando()
        #p1.actualizacionRec()
        #p1.runGanancia2()
        #p1.runGanancia2()

        p2.corriendo()
        #p2.setGananciaXY(p1.getGananciaXY())
        #p2.setGananciaXY((1, -1))
        p2.actualizacionRec()
        p2.runGanancia2()

        #deteccionColisiones([p1,p2], [plataforma], None)

        screen.fill((0,0,240))
        pygame.draw.rect(screen, red, p1.rec1)
        pygame.draw.rect(screen, darkBlue, p1.rec3)
        pygame.draw.rect(screen, green, p1.rec2)
        pygame.draw.rect(screen, blue, p1.rec4)


        #pygame.draw.rect(screen, red, p2.rec1)
        #pygame.draw.rect(screen, darkBlue, p2.rec3)
        #pygame.draw.rect(screen, green, p2.rec2)
        #pygame.draw.rect(screen, blue, p2.rec4)

        pygame.draw.rect(screen, red, plataforma.rectangulo)
        pygame.draw.rect(screen, red, rectangulo.rectangulo)
        #for i in lista1:
        #    for l in i:
        #        pygame.draw.rect(screen, white, l, 1)


        #pygame.draw.rect(screen, blue, rect2)
        #puntero.creandoCirculo()

        grupo.update()
        lista = pygame.sprite.spritecollide(puntero.sprite, grupo, False, pygame.sprite.collide_circle_ratio(1.4))
        if len(lista)>1:#pygame.sprite.collide_circle(puntero.sprite, circulo.sprite):
            pygame.draw.rect(screen, darkBlue, puntero.sprite.rect)


        pygame.display.flip()
        #print max_altura(velocidad, angulo, gravedad)




class Circulo(object):
    def __init__(self, x, y, ancho, largo):
        self.sprite = pygame.sprite.Sprite()
        self.radio = 100
        self.x = x
        self.y = y
        self.tamx = ancho
        self.tamy = largo
        self.sprite.rect = Rect(self.x, self.y, self.tamx, self.tamy)
        self.radio = int(math.sqrt(math.pow(self.sprite.rect.width,2)+math.pow(self.sprite.rect.height,2))/2.0)
        self.x_circulo = int(self.x + self.sprite.rect.width / 2.0)
        self.y_circulo = int(self.y + self.sprite.rect.height / 2.0)
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

    def creandoCirculo(self):
        if self.terminar == False:
            self.terminar = True
            self.otro=crearCirculo(self.radio, self.x_circulo, self.y_circulo)




def deteccionEfectoTunel1(personaje, rectangulo):
    p1 = Circulo(personaje._x, personaje._y, personaje.ancho, personaje.largo)
    p2 = Circulo(personaje.x_antes, personaje.y_antes, personaje.ancho, personaje.largo)

    x1 = p1.x_circulo
    y1 = p1.y_circulo
    x2 = p2.x_circulo
    y2 = p2.y_circulo


    x_medio, y_medio = puntoMedioRecta(x1, y1, x2, y2)
    radio = distanciaEntre2Puntos(x1, y1, x2, y2)/2.0+p1.radio
    circulo = crearCirculo(radio, x_medio, y_medio)

    while True:
        if colicionCirculo(circulo, rectangulo):
            print "colision777"
            circulo1x ,circulo1y = puntoMedioRecta(x1, y1, x_medio, y_medio)
            circulo2x ,circulo2y = puntoMedioRecta(x_medio, y_medio, x2, y2)
            radio1 = distanciaEntre2Puntos(x1, y2, x_medio, y_medio)/2.0+p1.radio
            radio2 = distanciaEntre2Puntos(x_medio, y_medio, x2, y2)/2.0+p1.radio
            circulo1 = crearCirculo(radio1, circulo1x, circulo1y)
            circulo2 = crearCirculo(radio2, circulo2x, circulo2y)

            if colicionCirculo(circulo1, rectangulo) and colicionCirculo(circulo2, rectangulo):
                return [circulo, circulo1, circulo2]
            else:
                if colicionCirculo(circulo1, rectangulo):
                    x2 = x_medio
                    y2 = y_medio
                    x_medio =circulo1x
                    y_medio =circulo1y

                if colicionCirculo(circulo2, rectangulo):
                    x1 = x_medio
                    y1 = y_medio
                    x_medio = circulo2x
                    y_medio = circulo2y
        else:
            return None





def colicionCirculo(circulo, rectangulo):
    for rect in circulo:
        if rect.colliderect(rectangulo.rectangulo):
            return True
    return False
    # crear el circulo pequeno 1 posiciones anteriores
    # crear un circulo con las nuevas posciones
    # rescatar las cordenadas iniciales y finales de cada extremo
    # una vez sacado el diamentro se crea un circulo gigante
    # Si el circulo gigante esta colicionando entonces empezar a buscar de forma binaria
    # se divide el circulo en dos y se vuelve a preguntar si los dos circulos estan colicionando entonces se encontro la colicion
    # de lo contrario se elige el circulo en que se esta colicionando y se vuelve a devidir asi hasta encontrar la colision

def distanciaEntre2Puntos(x1 , y1,  x2, y2):
    dis = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    return dis


def puntoMedioRecta(x1 , y1,  x2, y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    tupla = (x,y)
    return tupla

def crearCirculo1(radio, x_circulo, y_circulo):
    opuesto = 0
    num_division = 10
    otro =[]
    for i in range(num_division):
        opuesto += radio / num_division
        try:
            adyacente = math.sqrt(math.pow(radio, 2) - math.pow(opuesto, 2))
        except ValueError:
            print "radio: ",radio
            print "opuesto; ", opuesto
        otro.append(
            Rect(x_circulo -adyacente, y_circulo, adyacente * 2,
                 opuesto))
    opuesto = 0
    for i in range(num_division):
        opuesto += radio / num_division
        try:
            adyacente = math.sqrt(math.pow(radio, 2) - math.pow(opuesto, 2))
        except ValueError:
            print "radio: ", radio
            print "opuesto; ", opuesto
        otro.append(
            Rect(x_circulo - adyacente, y_circulo - opuesto, adyacente * 2,
                 opuesto))
    return  otro

def crearCirculo(radio, x_circulo, y_circulo):
    opuesto = 0
    num_division = 10
    otro =[]

    angulo = 0
    for i in range(int(num_division)):

        angulo += 85 / num_division
        opuesto = math.sin(math.radians(angulo))*radio
        try:
            adyacente = math.cos(math.radians(angulo))*radio
        except ValueError:
            print "radio: ",radio
            print "opuesto; ", opuesto
        otro.append(
            Rect(x_circulo -adyacente, y_circulo, adyacente * 2,
                 opuesto))
        otro.append(
            Rect(x_circulo - adyacente, y_circulo - opuesto, adyacente * 2,
                 opuesto))
    return  otro

def circuloRectangulo(radio, division = 5.0):
    opuesto = radio/division
    adyacente = math.sqrt(math.pow(radio, 2)-math.pow(opuesto,2))
    cuadrado=Rect(0, 0, adyacente*2, opuesto)
    return  cuadrado

print distanciaEntre2Puntos(2, 1, -3, 2)
main()