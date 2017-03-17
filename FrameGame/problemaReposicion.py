import math
from pygame import Rect
from Motor import Fisica
from Motor.Personaje_ import *
from Motor.Plataforma_ import *

p1 = Personaje()
p1._x = 219
p1._y = 191
p1.x_antes = 231
p1.y_antes = 207
p1.tam_rectangulos((100, 100))
p1.actualizacionRec()


plataforma2 = Plataforma()
plataforma2._x = 213
plataforma2._y = 2
plataforma2.x_antes = 210
plataforma2.y_antes = 2
plataforma2.setTamRect(20, 800)
plataforma2.actualizacionRec()



def reposicion(personaje, rectangulo, roce = True):
    rec1 = Rect(personaje._x, personaje._y, personaje.ancho, personaje.largo  )  # Personaje

    rec2 = Rect(rectangulo._x, rectangulo._y, rectangulo.ancho, rectangulo.largo)
    rec3 = Rect(rectangulo.x_antes, rectangulo.y_antes, rectangulo.ancho, rectangulo.largo)

    resPuntoPersonaje = rec1.colliderect(rec2) and rec1.colliderect(rec3)
    # cuando el avance del personaje coliciona con las dos plataformas la del presente y pasado entonces
    # entonces la reposicion tiene que ser desde el personaje
    # pasa los mismo con la plataforma
    rec1 = Rect(rectangulo._x, rectangulo._y, rectangulo.ancho, rectangulo.largo  )  # Rectangulo

    rec2 = Rect(personaje._x, personaje._y, personaje.ancho, personaje.largo)
    rec3 = Rect(personaje.x_antes, personaje.y_antes, personaje.ancho, personaje.largo)

    resPuntoRectangulo = rec1.colliderect(rec2) and rec1.colliderect(rec3)
    intercambio = False

    print "resPuntoPersonaje:  ", resPuntoPersonaje
    print "resPuntoRectangulo: " ,resPuntoRectangulo

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

    print "x1, y1: ", x1, y1
    print "x2, y2: ", x2, y2
    print "x3, y3: ", x3, y3
    print "x4, y4: ", x4, y4

    a = x - x_antes
    b = y - y_antes
    c = x* b
    d = y * a
    print "a: ",a
    print "b: ",b
    print "c: ",c
    print "d: ",d

    cuadros = [float('inf'), float('inf'), float('inf'), float('inf')]

    if b != 0:
        x1 = funcionx(a, b, c, d, y1)
        x3 = funcionx(a, b, c, d, y3)

        print "infx, supx: ", infx, supx
        print "infy, supy: ", infy, supy
        print "xy1: ", x1, y1
        print "xy2: ", x2, y2
        print "xy3: ", x3, y3
        print "xy4: ", x4, y4
        print infx," <= ", x3," <= ",supx ," AND ", infy," <= ", y3," <= ",supy

        if infx <= x1 <= supx and infy <= y1 <= supy:
            cuadros[0] = Fisica.distanciaEntre2Puntos(x1, y1, x, y)
        if infx <= x3 <= supx and infy <= y3 <= supy:
            cuadros[2] = Fisica.distanciaEntre2Puntos(x3, y3, x, y)

    if a != 0:
        y2 = funciony(a, b, c, d, x2)
        y4 = funciony(a, b, c, d, x4)
        print "y2_mejor: ", y2
        print "y4_mejor: ", y4
        print "infx, supx: ", infx, supx
        print "infy, supy: ", infy, supy
        print "xy1: ", x1, y1
        print "xy2: ", x2, y2
        print "xy3: ", x3, y3
        print "xy4: ", x4, y4
        print infx, " <= ", x2, " <= ", supx, " AND ", infy, " <= ", y2, " <= ", supy

        if infx <= x2 <= supx and infy <= y2 <= supy:
            print "entro aqui1"
            cuadros[1] = Fisica.distanciaEntre2Puntos(x2, y2, x, y)
        if infx <= x4 <= supx and infy <= y4 <= supy:
            print "entro aqui2"
            cuadros[3] = Fisica.distanciaEntre2Puntos(x4, y4, x, y)

    if b != 0:
        x1 = funcionx(a, b, c, d, y1)
        x3 = funcionx(a, b, c, d, y3)

    if a != 0:
        y2 = funciony(a, b, c, d, x2)
        y4 = funciony(a, b, c, d, x4)

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
    print "x1, y1: ", x1, y1
    print "x2, y2: ", x2, y2
    print "x3, y3: ", x3, y3
    print "x4, y4: ", x4, y4
    print "        RECTANGULO"
    print "x, y: ", recx, recy
    print "x_antes, y_antes: ", rectangulo.x_antes, rectangulo.y_antes
    print "Cuadro Antes: ", cuadro
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
    l.append((x1, y1))
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
        print x1, y1
        print x2, y2
        print x3, y3
        print x4, y4
        # time.sleep(1)

    return cuadro

def funcionx(a, b, c, d, y):
    return (a*y-d+c)/b

def funciony(a, b, c, d, x):
    return (b*x-c+d)/a

reposicion(p1, plataforma2)