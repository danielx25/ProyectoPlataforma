import math
from pygame import Rect
import Fisica
import time

class GestionDeteccionColisiones(object):
    def __init__(self, tablacolisiones):
        self.colisionesEntrePersonajes = False
        self.colisionElastica = False

    def deteccionColisiones(self, personajes, plataformas, tablaColisiones):
        self.deteccionColisionEntrePersonajesYPlatafromas(personajes, plataformas, tablaColisiones)
        #self.deteccionColisionEntrePersonajes(personajes, tablaColisiones)
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
                #        print "colsicion tunel"
                #        colision = True

                if colision:
                    print "colision"
                    lado = reposicion(personaje, plataforma)
                    personaje.rectangulo.left = personaje._x
                    personaje.rectangulo.top = personaje._y
                    personaje.setSalto(False)
                    personaje.setGananciaXY((0,0))
                    #personaje.activarGanancia = False
                else:
                    pass
                    #personaje.activarGanancia = True

                if personaje.ady_down == False:
                    personaje.rectangulo.top+=1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_down = True
                        tablaColisiones[personaje.id].append((plataforma, 0))
                        #personaje.setGananciaXY((plataforma.getGananciaXY()))
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
                        #gananciax = plataforma.getGananciaXY()[0]
                        #if gananciax < 0:
                        #    personaje.setGananciaXY((plataforma.getGananciaXY()[0], 0))
                    personaje.rectangulo.left -= 1

                if personaje.ady_left == False:
                    personaje.rectangulo.left -= 1
                    if plataforma.rectangulo.colliderect(personaje.rectangulo):
                        personaje.ady_left = True
                        tablaColisiones[personaje.id].append((plataforma, 1))
                        #gananciax = plataforma.getGananciaXY()[0]
                        #if gananciax > 0:
                        #    personaje.setGananciaXY((plataforma.getGananciaXY()[0], 0))
                    personaje.rectangulo.left += 1



    def gravedadActua(self, personajes):
        for personaje in personajes:
            if personaje.getSalto() == False and personaje.ady_down == False:
                print "ACTUA GRAVEDAD"
                personaje.setCaminar(False)
                personaje.setCorrer(False)
                personaje.setSalto(True)
                personaje.status["parabola"] = (60, -90)
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
                        lado = reposicion(personaje, personajeAux, True)
                        personaje.rectangulo.left = personaje._x
                        personaje.rectangulo.top = personaje._y
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

def reposicion_inteligente(personaje, rectangulo):
    pass

def reposicion(personaje, rectangulo, roce = True):
    rec1 = Rect(personaje._x, personaje._y, personaje.ancho, personaje.largo)#Personaje

    rec2 = Rect(rectangulo._x, rectangulo._y, rectangulo.ancho, rectangulo.largo)
    rec3 = Rect(rectangulo.x_antes, rectangulo.y_antes, rectangulo.ancho, rectangulo.largo)

    resPuntoPersonaje = rec1.colliderect(rec2) and rec1.colliderect(rec3)
    #cuando el avance del personaje coliciona con las dos plataformas la del presente y pasado entonces
    #entonces la reposicion tiene que ser desde el personaje
    #pasa los mismo con la plataforma
    rec1 = Rect(rectangulo._x, rectangulo._y, rectangulo.ancho, rectangulo.largo)#Rectangulo

    rec2 = Rect(personaje._x, personaje._y, personaje.ancho, personaje.largo)
    rec3 = Rect(personaje.x_antes, personaje.y_antes, personaje.ancho, personaje.largo)

    resPuntoRectangulo = rec1.colliderect(rec2) and rec1.colliderect(rec3)
    intercambio = False

    print "resPuntoPersonaje:  ", resPuntoPersonaje
    print "resPuntoRectangulo: ",resPuntoRectangulo

    if resPuntoPersonaje == False and resPuntoRectangulo == True:
        intercambio = True

    if resPuntoPersonaje == False and resPuntoRectangulo == False:
        if personaje._x == personaje.x_antes and personaje._y == personaje.y_antes:
            intercambio = True

        if (personaje._x != personaje.x_antes or personaje._y != personaje.y_antes) and \
                (rectangulo._x != rectangulo.x_antes or rectangulo._y != rectangulo.y_antes):
            intercambio = True

    if rectangulo._x == rectangulo.x_antes and rectangulo._y == rectangulo.y_antes:
        intercambio = False

    if resPuntoPersonaje == True and resPuntoRectangulo == True:
        intercambio = True

    if intercambio:
        aux = rectangulo
        rectangulo = personaje
        personaje = aux
        intercambio = True

    x = Fisica.truncate(personaje._x)
    y = Fisica.truncate(personaje._y)
    x_antes = Fisica.truncate(personaje.x_antes)
    y_antes = Fisica.truncate(personaje.y_antes)
    ancho = personaje.ancho
    largo = personaje.largo
    
    recx = Fisica.truncate(rectangulo._x)
    recy = Fisica.truncate(rectangulo._y)
    

    infx = min([x, x_antes])
    supx = max([x, x_antes])

    infy = min([y, y_antes])
    supy = max([y, y_antes])
    x1 = x
    y1 = recy + rectangulo.largo

    x2 = recx - ancho
    y2 = y

    x3 = x
    y3 = recy - largo

    x4 = recx + rectangulo.ancho
    y4 = y


    a = x - x_antes
    b = y - y_antes
    c = x*b
    d = y*a

    cuadros=[float('inf'), float('inf'), float('inf'), float('inf')]


    if b != 0:
        x1 = funcionx(a,b,c,d,y1)
        x3 = funcionx(a, b, c, d, y3)

        #print "infx, supx: ", infx, supx
        #print "infy, supy: ", infy, supy
        #print "xy1: ", x1, y1
        #print "xy2: ", x2, y2
        #print "xy3: ", x3, y3
        #print "xy4: ", x4, y4
        #print infx," <= ", x3," <= ",supx ," AND ", infy," <= ", y3," <= ",supy

        if infx <= x1 <= supx and  infy<= y1 <= supy:
            cuadros[0] = Fisica.distanciaEntre2Puntos(x1, y1, x, y)
        if  infx <= x3 <= supx and infy<= y3 <= supy:
            cuadros[2] = Fisica.distanciaEntre2Puntos(x3, y3, x, y)


    if a != 0:
        y2 = funciony(a,b,c,d,x2)
        y4 = funciony(a,b,c,d,x4)

        if infx <= x2 <= supx and  infy<= y2 <= supy:
            cuadros[1] = Fisica.distanciaEntre2Puntos(x2, y2, x, y)
        if infx <= x4 <= supx and  infy<= y4 <= supy:
            cuadros[3] = Fisica.distanciaEntre2Puntos(x4, y4, x, y)

    if b != 0:
        x1 = funcionx(a,b,c,d,y1)
        x3 = funcionx(a, b, c, d, y3)

    if a != 0:
        y2 = funciony(a,b,c,d,x2)
        y4 = funciony(a,b,c,d,x4)

    if recx <= x1 <= recx + rectangulo.ancho or recx <= x1 + ancho <= recx + rectangulo.ancho:
        cuadros[0] = Fisica.distanciaEntre2Puntos(x1, y1, x_antes, y_antes)
    if recy <= y2 <= recy + rectangulo.largo or recy <= y2 + largo <= recy + rectangulo.largo:
        cuadros[1] = Fisica.distanciaEntre2Puntos(x2, y2, x_antes, y_antes)
    if recx <= x3 <= recx + rectangulo.ancho or recx <= x3 + ancho <= recx + rectangulo.ancho:
        cuadros[2] = Fisica.distanciaEntre2Puntos(x3, y3, x_antes, y_antes)
    if recy <= y4 <= recy + rectangulo.largo or recy <= y4 + largo <= recy + rectangulo.largo:
        cuadros[3] = Fisica.distanciaEntre2Puntos(x4, y4, x_antes, y_antes)

    cuadro = cuadros.index(min(cuadros))

    print "x, y: ", x, y
    print "x_antes, y_antes: ", x_antes, y_antes
    print cuadros
    print "x1, y1: ",x1, y1
    print "x2, y2: ",x2, y2
    print "x3, y3: ",x3, y3
    print "x4, y4: ",x4, y4
    print "        RECTANGULO"
    print "x, y: ", recx, recy
    print "x_antes, y_antes: ", rectangulo.x_antes, rectangulo.y_antes

    if intercambio:
        aux = personaje
        personaje = rectangulo
        rectangulo = aux

        x = Fisica.truncate(personaje._x)
        y = Fisica.truncate(personaje._y)
        x_antes = Fisica.truncate(personaje.x_antes)
        y_antes = Fisica.truncate(personaje.y_antes)
        ancho = personaje.ancho
        largo = personaje.largo

        recx = Fisica.truncate(rectangulo._x)
        recy = Fisica.truncate(rectangulo._y)

        a = x - x_antes
        b = y - y_antes
        c = x * b
        d = y * a

        if cuadro == 0:
            print "abajo"
            x0 = x
            y0 = recy - largo
            if roce == True and b != 0:
                x0 = funcionx(a, b, c, d, y0)

            cuadro = 2
        elif cuadro == 1:
            print "izquierdo"
            x0 = recx + rectangulo.ancho
            y0 = y
            cuadro = 3
        elif cuadro == 2:
            print "arriba"
            x0 = x
            y0 = recy + rectangulo.largo
            cuadro = 0
        elif cuadro == 3:
            print "derecha"
            x0 = recx - ancho
            y0 = y
            cuadro = 1

        personaje._x = x0
        personaje._y = y0
        print "Rectangulo?", cuadro
        return cuadro

    l = []
    l.append((x1,y1))
    l.append((x2, y2))
    l.append((x3, y3))
    l.append((x4, y4))
    if cuadro != float('inf'):
        personaje._x = l[cuadro][0]
        personaje._y = l[cuadro][1]
    print "Personaje?", cuadro
    if cuadro == 3:
        print x, y
        print x_antes, y_antes
        print cuadros
        print x1,y1
        print x2, y2
        print x3, y3
        print x4, y4
        #time.sleep(1)

    return cuadro

def funcionx(a, b, c, d, y):
    return (a*y-d+c)/b

def funciony(a, b, c, d, x):
    return (b*x-c+d)/a