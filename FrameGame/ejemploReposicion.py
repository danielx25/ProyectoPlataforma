
from pygame import Rect

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

    if a != 0:
        y2 = funciony(a,b,c,d,x2)
        y4 = funciony(a,b,c,d,x4)


    if rectangulo._x<=x1<=rectangulo._x+rectangulo.ancho or rectangulo._x<=x1+ancho<=rectangulo._x+rectangulo.ancho:
        cuadros[0] = distanciaEntre2Puntos(x1, y1, x_antes, y_antes)
    if rectangulo._y<=y2<=rectangulo._y+rectangulo.largo or rectangulo._y<=y2+largo<=rectangulo._y+rectangulo.largo:
        cuadros[1] = distanciaEntre2Puntos(x2, y2, x_antes, y_antes)
    if rectangulo._x<=x3<=rectangulo._x+rectangulo.ancho or rectangulo._x<=x3+ancho<=rectangulo._x+rectangulo.ancho:
        cuadros[2] = distanciaEntre2Puntos(x3, y3, x_antes, y_antes)
    if rectangulo._y<=y4<=rectangulo._y+rectangulo.largo or rectangulo._y<=y4+largo<=rectangulo._y+rectangulo.largo:
        cuadros[3] = distanciaEntre2Puntos(x4, y4, x_antes, y_antes)
    cuadro = cuadros.index(min(cuadros))

    l = []
    l.append(Rect(x1, y1, ancho, largo))
    l.append(Rect(x2, y2, ancho, largo))
    l.append(Rect(x3, y3, ancho, largo))
    l.append(Rect(x4, y4, ancho, largo))
    return [l[cuadro]]
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
    p1._x = 253
    p1._y = 273
    p1.x_antes = 263
    p1.y_antes = 300
    p1.tam_rectangulos((100, 100))
    p1.actualizacionRec()

    p2 = Personaje()
    p2._x = 243
    p2._y = 2
    p2.tam_rectangulos((20, 800))
    p2.actualizacionRec()

    plataforma2 = Plataforma()
    plataforma2._x = 243
    plataforma2._y = 2
    plataforma2.x_antes = 246
    plataforma2.y_antes = 2
    plataforma2.actualizacionRec()
    plataforma2.setTamRect(20, 800)

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
                pass
                #xy=pygame.mouse.get_pos()
                #p1.x_antes = xy[0]
                #p1.y_antes = xy[1]
                #p1_antes.left = xy[0]
                #p1_antes.top = xy[1]
                #l = reposicion(p1, plataforma2)

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
