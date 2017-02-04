import math
from pygame import Rect
import Fisica


class GestionDeteccionColisiones(object):
    def __init__(self, tablacolisiones):
        self.colisionesEntrePersonajes = False
        self.colisionElastica = False

    def deteccionColisiones(self, personajes, plataformas, tablaColisiones):
        self.deteccionColisionEntrePersonajesYPlatafromas(personajes, plataformas, tablaColisiones)
        self.deteccionColisionEntrePersonajes(personajes, tablaColisiones)
        self.gravedadActua(personajes)
        """
        for personaje in personajes:
            lista = tablaColisiones[personaje.id]
            print "id: ", personaje.id
            for info in lista:
                print "     id  : ", info[0].id
                print "     lado: ", info[1]
            print "---------------------------"
        """


    def deteccionColisionEntrePersonajesYPlatafromas(self, personajes, plataformas, tablaColisiones):
        for personaje in personajes:

            tablaColisiones[personaje.id] = []

            personaje.ady_left = False
            personaje.ady_right = False
            personaje.ady_down = False
            personaje.ady_up = False

            for plataforma in plataformas:
                colision = False
                if plataforma.rectangulo.colliderect(personaje.rectangulo):
                    colision = True
                #else:
                #    if deteccionEfectoTunel(personaje, plataforma):
                #        colision = True

                if colision:
                    lado = reposicion(personaje, plataforma)
                    #tablaColisiones[personaje.id].append((plataforma, lado))

                if personaje.ady_down == False:
                    personaje.rectangulo.top+=1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_down = True
                        tablaColisiones[personaje.id].append((plataforma, 0))
                    personaje.rectangulo.top-=1

                if personaje.ady_up == False:
                    personaje.rectangulo.top -= 1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_up = True
                        tablaColisiones[personaje.id].append((plataforma, 2))
                    personaje.rectangulo.top += 1

                if personaje.ady_right == False:
                    personaje.rectangulo.left += 1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_right= True
                        tablaColisiones[personaje.id].append((plataforma, 3))
                    personaje.rectangulo.left -= 1

                if personaje.ady_left == False:
                    personaje.rectangulo.left -= 1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_left = True
                        tablaColisiones[personaje.id].append((plataforma, 1))
                    personaje.rectangulo.left += 1

    def gravedadActua(self, personajes):
        for personaje in personajes:
            if personaje.getSalto() == False and personaje.ady_down == False:
                personaje.setCaminar(False)
                personaje.setCorrer(False)
                personaje.setSalto(True)
                personaje.status["parabola"] = (60, 270)
                personaje.reseteo()


    def deteccionColisionEntrePersonajes(self, personajes, tablaColisiones):

        for personaje in personajes:
            for personajeAux in personajes:
                if personaje.id != personajeAux.id:
                    colision = False
                    if personajeAux.rectangulo.colliderect(personaje.rectangulo):
                        colision = True
                    #else:
                    #    if deteccionEfectoTunel(personaje, personajeAux):
                    #        colision = True

                    if colision:
                        lado = reposicion(personaje, personajeAux)
                        #tablaColisiones[personaje.id].append((pla, lado))

                    if personaje.ady_down == False:
                        personaje.rectangulo.top += 1
                        if personajeAux.rectangulo.colliderect(personaje.rectangulo):
                            tablaColisiones[personaje.id].append((personajeAux, 0))
                        personaje.rectangulo.top -= 1

                    if personaje.ady_up == False:
                        personaje.rectangulo.top -= 1
                        if personajeAux.rectangulo.colliderect(personaje.rectangulo):
                            tablaColisiones[personaje.id].append((personajeAux, 2))
                        personaje.rectangulo.top += 1

                    if personaje.ady_right == False:
                        personaje.rectangulo.left += 1
                        if personajeAux.rectangulo.colliderect(personaje.rectangulo):
                            tablaColisiones[personaje.id].append((personajeAux, 3))
                        personaje.rectangulo.left -= 1

                    if personaje.ady_left == False:
                        personaje.rectangulo.left -= 1
                        if personajeAux.rectangulo.colliderect(personaje.rectangulo):
                            tablaColisiones[personaje.id].append((personajeAux, 1))
                        personaje.rectangulo.left += 1


def deteccionColisiones(personajes, plataformas, TablaColsiones):
    for personaje in  personajes:
        angulo = personaje.status["angulo"]
        x = personaje._x
        y = personaje._y
        for plataforma in  plataformas:

            if deteccionEfectoTunel(personaje, plataforma):
                print "no deveria pero weenio"
                personaje.setSalto(False)
                personaje.setCorrer(False)
                personaje.setCaminar(False)
            """
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
    if(personaje._x == personaje.x_antes and personaje._y == personaje.y_antes):
        return False
    p1 = Circulo(personaje._x, personaje._y, personaje.ancho, personaje.largo)
    p2 = Circulo(personaje.x_antes, personaje.y_antes, personaje.ancho, personaje.largo)
    x1 = p1.x_circulo
    y1 = p1.y_circulo
    x2 = p2.x_circulo
    y2 = p2.y_circulo


    contador = 0
    while True:
        x_medio, y_medio = Fisica.puntoMedioRecta(x1, y1, x2, y2)
        radio = Fisica.distanciaEntre2Puntos(x1, y1, x2, y2) / 2.0 + p1.radio
        circulo = crearCirculo(radio, x_medio, y_medio)

        if colicionCirculo(circulo, rectangulo):

            circulo1x ,circulo1y = Fisica.puntoMedioRecta(x1, y1, x_medio, y_medio)
            circulo2x ,circulo2y = Fisica.puntoMedioRecta(x_medio, y_medio, x2, y2)
            radio1 = Fisica.distanciaEntre2Puntos(x1, y2, x_medio, y_medio)/2.0+p1.radio
            radio2 = Fisica.distanciaEntre2Puntos(x_medio, y_medio, x2, y2)/2.0+p1.radio
            circulo1 = crearCirculo(radio1, circulo1x, circulo1y)
            circulo2 = crearCirculo(radio2, circulo2x, circulo2y)

            if Fisica.distanciaEntre2Puntos(circulo1x, circulo1y, circulo2x, circulo2y)<=p1.radio:
                return False
            boolCirculo1 = colicionCirculo(circulo1, rectangulo)
            boolCirculo2 = colicionCirculo(circulo2, rectangulo)
            if boolCirculo1 == False and boolCirculo2 == False:
                return False

            if boolCirculo1 and boolCirculo2:
                return True
            else:
                if boolCirculo1:
                    x2 = x_medio
                    y2 = y_medio
                    x_medio =circulo1x
                    y_medio =circulo1y

                if boolCirculo2:
                    x1 = x_medio
                    y1 = y_medio
                    x_medio = circulo2x
                    y_medio = circulo2y
            contador+=1
        else:
            return False



class Circulo(object):
    def __init__(self, x, y, ancho, largo):
        self.radio = 100
        self.x = x
        self.y = y
        self.tamx = ancho
        self.tamy = largo
        self.radio = int(math.sqrt(math.pow(self.tamx,2)+math.pow(self.tamy,2))/2.0)

        if self.tamx < self.tamy:
            self.radio = self.tamx / 2
        else:
            self.radio = self.tamy / 2

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

def reposicion(personaje, rectangulo):
    x = personaje._x
    y = personaje._y
    x_antes = personaje.x_antes
    y_antes = personaje.y_antes
    ancho = personaje.ancho
    largo = personaje.largo

    infx = min([x, x_antes])
    supx = max([x, x_antes])

    infy = min([y, y_antes])
    supy = max([y, y_antes])
    x1 = x
    y1 = rectangulo._y + rectangulo.largo

    x2 = rectangulo._x - ancho
    y2 = y

    x3 = x
    y3 = rectangulo._y - largo

    x4 = rectangulo._x + rectangulo.ancho
    y4 = y


    a = x - x_antes
    b = y - y_antes
    c = x*b
    d = y*a

    cuadros=[float('inf'), float('inf'), float('inf'), float('inf')]

    if b != 0:
        x1 = funcionx(a,b,c,d,y1)
        x3 = funcionx(a, b, c, d, y3)

        if infx <= x1 < supx and  infy<= y1 < supy:
            cuadros[0] = Fisica.distanciaEntre2Puntos(x1, y1, x, y)
        if  infx <= x3 < supx and infy<= y3 < supy:
            cuadros[2] = Fisica.distanciaEntre2Puntos(x3, y3, x, y)


    if a != 0:
        y2 = funciony(a,b,c,d,x2)
        y4 = funciony(a,b,c,d,x4)

        if infx <= x2 < supx and  infy<= y2 < supy:
            cuadros[1] = Fisica.distanciaEntre2Puntos(x2, y2, x, y)
        if infx <= x4 < supx and  infy<= y4 < supy:
            cuadros[3] = Fisica.distanciaEntre2Puntos(x4, y4, x, y)

    if b != 0:
        x1 = funcionx(a,b,c,d,y1)
        x3 = funcionx(a, b, c, d, y3)

    if a != 0:
        y2 = funciony(a,b,c,d,x2)
        y4 = funciony(a,b,c,d,x4)

    if rectangulo._x <= x1 <= rectangulo._x + rectangulo.ancho or rectangulo._x <= x1 + ancho <= rectangulo._x + rectangulo.ancho:
        cuadros[0] = Fisica.distanciaEntre2Puntos(x1, y1, x_antes, y_antes)
    if rectangulo._y <= y2 <= rectangulo._y + rectangulo.largo or rectangulo._y <= y2 + largo <= rectangulo._y + rectangulo.largo:
        cuadros[1] = Fisica.distanciaEntre2Puntos(x2, y2, x_antes, y_antes)
    if rectangulo._x <= x3 <= rectangulo._x + rectangulo.ancho or rectangulo._x <= x3 + ancho <= rectangulo._x + rectangulo.ancho:
        cuadros[2] = Fisica.distanciaEntre2Puntos(x3, y3, x_antes, y_antes)
    if rectangulo._y <= y4 <= rectangulo._y + rectangulo.largo or rectangulo._y <= y4 + largo <= rectangulo._y + rectangulo.largo:
        cuadros[3] = Fisica.distanciaEntre2Puntos(x4, y4, x_antes, y_antes)

    cuadro = cuadros.index(min(cuadros))

    l = []
    l.append((x1,y1))
    l.append((x2, y2))
    l.append((x3, y3))
    l.append((x4, y4))
    if cuadro != float('inf'):
        personaje._x = l[cuadro][0]
        personaje._y = l[cuadro][1]
    print "como?", cuadro
    return cuadro

def funcionx(a, b, c, d, y):
    return (a*y-d+c)/b

def funciony(a, b, c, d, x):
    return (b*x-c+d)/a