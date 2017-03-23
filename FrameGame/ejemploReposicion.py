
from pygame import Rect

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

    #print "resPuntoPersonaje:  ", resPuntoPersonaje
    #print "resPuntoRectangulo: " ,resPuntoRectangulo

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

    """
    if intercambio:
        aux = rectangulo
        rectangulo = personaje
        personaje = aux
        intercambio = True
    """
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
    c = x* b
    d = y * a


    if b != 0:
        x1 = funcionx(a, b, c, d, y1)
        x3 = funcionx(a, b, c, d, y3)

    if a != 0:
        y2 = funciony(a, b, c, d, x2)
        y4 = funciony(a, b, c, d, x4)


    """
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
    """

    l = []
    l.append(Rect(x1, y1, ancho, largo))
    l.append(Rect(x2, y2, ancho, largo))
    l.append(Rect(x3, y3, ancho, largo))
    l.append(Rect(x4, y4, ancho, largo))

    indice = 0
    lista = []
    for contador in range(4):
        if contador ==0:
            recNew = Rect(x1, y1-1, ancho, largo)
            if recNew.colliderect(rectangulo.rectangulo):
                lista.append((x1, y1))

        if contador == 1 :
            recNew = Rect(x2+1, y2, ancho, largo)
            if recNew.colliderect(rectangulo.rectangulo):
                lista.append((x2, y2))

        if contador == 2:
            recNew = Rect(x3 , y3+1, ancho, largo)
            if recNew.colliderect(rectangulo.rectangulo):
                lista.append((x3, y3))

        if contador == 3:
            recNew = Rect(x4 - 1, y4, ancho, largo)
            if recNew.colliderect(rectangulo.rectangulo):
                lista.append((x4, y4))
    l=[]
    for x_, y_ in lista:
        if infx <= x_ <= supx and infy <= y_ <= supy:
            l.append(Rect(x_, y_, ancho, largo))
        else:
            infx1 = min([x, x_])
            supx1= max([x, x_])

            infy1 = min([y, y_])
            supy1 = max([y, y_])
            if infx1 <= x_antes <= supx1 and infy1 <= y_antes <= supy1:
                l.append(Rect(x_, y_, ancho, largo))

    if len(l)>0:
        pass
        #personaje._x = l[0][0]
        #personaje._y =l[0][1]
    # return [l[cuadro]]
    return l


def funcionx(a, b, c, d, y):
    return (a*y-d+c)/b

def funciony(a, b, c, d, x):
    return (b*x-c+d)/a


import pygame
from Motor import*

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)



def main():

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.FULLSCREEN


    pygame.display.set_caption("ProyectoPygame")
    reloj1=pygame.time.Clock()
    salir=False

    p1 = Personaje()
    p1._x = 430
    p1._y = 180
    p1.x_antes = 50
    p1.y_antes = 50
    p1.tam_rectangulos((70, 70))
    p1.actualizacionRec()

    p2 = Personaje()
    p2._x = 100
    p2._y = 200
    p2.tam_rectangulos((100, 100))
    p2.actualizacionRec()

    plataforma2 = Plataforma()
    plataforma2.setXY(250, 200)
    plataforma2.setTamRect(300, 100)

    p1_antes = Rect(p1.x_antes, p1.y_antes, 70, 70)

    motor = MotorVideojuego()
    motor.conjuntoPersonajes = [p1, p2]
    #motor.start()
    start = pygame.time.get_ticks()/1000

    iter=0
    limit=1000

    l = reposicion(p1, plataforma2)
    while salir == False:

        lista=pygame.event.get()#((pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT, pygame.MOUSEBUTTONDOWN))
        for event in lista:
            #----------Escuchando Eventos del Usuario-#
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    p1.setSalto(True)
                    print "SAlta"
            if event.type == pygame.MOUSEMOTION:
                xy=pygame.mouse.get_pos()
                p1.x_antes = xy[0]
                p1.y_antes = xy[1]
                p1_antes.left = xy[0]
                p1_antes.top = xy[1]
                l = reposicion(p1, plataforma2)

        pantalla.fill((0,0,240))
        if pygame.time.get_ticks()>limit:
            #print iter
            limit+=1000
            iter=0
        iter+=1



        pygame.draw.rect(pantalla, green, plataforma2.rectangulo)
        pygame.draw.rect(pantalla, red, p1.rectangulo)
        pygame.draw.rect(pantalla, red, p1_antes)

        for rec in l:
            pygame.draw.rect(pantalla, darkBlue, rec)


        reloj1.tick(120)
        pygame.display.update()
    motor.salirJuego = True
    pygame.quit()

main()
