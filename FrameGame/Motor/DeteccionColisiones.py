import math
from pygame import Rect
import Fisica
def deteccionColisiones(personajes, plataformas, TablaColsiones):
    for personaje in  personajes:
        angulo = personaje.status["angulo"]
        x = personaje._x
        y = personaje._y
        for plataforma in  plataformas:

            if personaje.rec1.top < plataforma._y:
                if plataforma.rectangulo.colliderect(personaje.rec1):
                    print "asdasd"
                    personaje.setSalto(False)
                    personaje.setCorrer(False)
                    personaje.setCaminar(False)
                    #personaje._y = plataforma._y - personaje.largo

            if personaje.rec2.left + personaje.rec2.width > plataforma._x + plataforma.ancho:
                if plataforma.rectangulo.colliderect(personaje.rec2):
                    personaje.setSalto(False)
                    personaje.setCorrer(False)
                    personaje.setCaminar(False)
                    personaje._x = plataforma._x + plataforma.ancho

            if personaje.rec3.left < plataforma._x:
                if plataforma.rectangulo.colliderect(personaje.rec3):
                    personaje.setSalto(False)
                    personaje.setCorrer(False)
                    personaje.setCaminar(False)
                    personaje._x = plataforma._x - personaje.ancho

            if personaje.rec4.top + personaje.rec4.height > plataforma._y + plataforma.largo:
                if plataforma.rectangulo.colliderect(personaje.rec4):
                    personaje.setSalto(False)
                    personaje.setCorrer(False)
                    personaje.setCaminar(False)
                    personaje._y = plataforma._y + plataforma.largo


"""
            if angulo < 0 and angulo >= -90:
                if personaje.rec1.top < plataforma._y:
                    if plataforma.rectangulo.colliderect(personaje.rec1):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._y = plataforma._y - personaje.largo

                if personaje.rec3.left < plataforma._x:
                    if plataforma.rectangulo.colliderect(personaje.rec3):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._x = plataforma._x - personaje.ancho

            if (angulo <-90 and angulo >= -180) or angulo == 180:
                if personaje.rec1.top < plataforma._y:
                    if plataforma.rectangulo.colliderect(personaje.rec1):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._y = plataforma._y - personaje.largo

                if personaje.rec2.left+personaje.rec2.width > plataforma._x+plataforma.ancho:
                    if plataforma.rectangulo.colliderect(personaje.rec2):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._x = plataforma._x + plataforma.ancho


            if angulo < 180 and angulo >=90:
                if personaje.rec2.left + personaje.rec2.width > plataforma._x + plataforma.ancho:
                    if plataforma.rectangulo.colliderect(personaje.rec2):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._x = plataforma._x + plataforma.ancho

                if personaje.rec4.top+personaje.rec4.height>plataforma._y+plataforma.largo:
                    if plataforma.rectangulo.colliderect(personaje.rec4):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._y = plataforma._y+plataforma.largo

            if angulo < 90 and angulo >=0:
                if personaje.rec4.top + personaje.rec4.height > plataforma._y + plataforma.largo:
                    if plataforma.rectangulo.colliderect(personaje.rec4):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._y = plataforma._y + plataforma.largo

                if personaje.rec3.left < plataforma._x:
                    if plataforma.rectangulo.colliderect(personaje.rec3):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        personaje._x = plataforma._x - personaje.ancho

            if plataforma.rectangulo.colliderect(personaje.rec1):
                personaje.setSalto(False)
                personaje._y = plataforma._y - personaje.largo

            if plataforma.rectangulo.colliderect(personaje.rec2):
                personaje.setSalto(False)
                personaje._x = plataforma._x+plataforma.ancho

            if plataforma.rectangulo.colliderect(personaje.rec3):
                personaje.setSalto(False)
                personaje.x = plataforma.x-personaje.ancho

            if plataforma.rectangulo.colliderect(personaje.rec4):
                pass"""


def restituir_pos(p, entorno, _lado, sentido=False):

    if sentido == True:
        if _lado == 1:
            _lado = 4

        elif _lado == 2:
            _lado = 3

        elif _lado == 3:
            _lado = 2

        elif _lado == 4:
            _lado = 1

    if _lado == 1:
        p._y = entorno._y - p.largo
    elif _lado == 2:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left + entorno.imagen.sprite.rect.size[0] + 3
    elif _lado == 3:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left - p.imagen.sprite.rect.size[0] - 3
    elif _lado == 4:
        p.imagen.sprite.rect.top  = entorno.imagen.sprite.rect.top + entorno.imagen.sprite.rect.size[1] + 2
    p.pos_rectangulos()


def deteccionEfectoTunel(personaje, rectangulo):
    p1 = Circulo(personaje._x, personaje._y, personaje.ancho, personaje.largo)
    p2 = Circulo(personaje.x_antes, personaje.y_antes, personaje.ancho, personaje.largo)

    x1 = p1.x_circulo
    y1 = p1.y_circulo
    x2 = p2.x_circulo
    y2 = p2.y_circulo


    x_medio, y_medio = Fisica.puntoMedioRecta(x1, y1, x2, y2)
    radio = Fisica.distanciaEntre2Puntos(x1, y1, x2, y2)/2.0+p1.radio
    circulo = crearCirculo(radio, x_medio, y_medio)

    while True:
        if colicionCirculo(circulo, rectangulo):
            print "colision777"
            circulo1x ,circulo1y = Fisica.puntoMedioRecta(x1, y1, x_medio, y_medio)
            circulo2x ,circulo2y = Fisica.puntoMedioRecta(x_medio, y_medio, x2, y2)
            radio1 = Fisica.distanciaEntre2Puntos(x1, y2, x_medio, y_medio)/2.0+p1.radio
            radio2 = Fisica.distanciaEntre2Puntos(x_medio, y_medio, x2, y2)/2.0+p1.radio
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



class Circulo(object):
    def __init__(self, x, y, ancho, largo):
        self.radio = 100
        self.x = x
        self.y = y
        self.tamx = ancho
        self.tamy = largo
        self.radio = int(math.sqrt(math.pow(self.tamx,2)+math.pow(self.tamy,2))/2.0)
        self.x_circulo = int(self.x + self.tamx / 2.0)
        self.y_circulo = int(self.y + self.tamy / 2.0)
        #self.sprite.radius = self.radio
        self.terminar = False
        self.otro = []#Rect(0, 0, self.tamx, self.tamy)]
    """
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
    """
    def posicion(self, x, y):
        self.x=self.sprite.rect.left = x
        self.y=self.sprite.rect.top = y

    def creandoCirculo(self):
        if self.terminar == False:
            self.terminar = True
            self.otro=crearCirculo(self.radio, self.x_circulo, self.y_circulo)



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

def colicionCirculo(circulo, rectangulo):
    for rect in circulo:
        if rect.colliderect(rectangulo.rectangulo):
            return True
    return False