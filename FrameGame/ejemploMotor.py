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
    p1.setXY(120, 40)
    p1.tam_rectangulos((100, 100))
    p1.actualizacionRec()

    p2 = Personaje()
    p2.setXY(20,160)
    p2.tam_rectangulos((100, 100))
    p2.actualizacionRec()

    p3 = Personaje()
    p3.setXY(20, 280)
    p3.tam_rectangulos((100, 100))
    p3.actualizacionRec()

    p1.id = "daniel"
    p2.id = "pedro"

    plataforma = Plataforma()
    plataforma.setXY(0, 554)
    plataforma.setTamRect(800, 70)

    plataforma1 = Plataforma()
    plataforma1.setXY(300, 400)
    plataforma1.setTamRect(50, 50)
    plataforma1.id = "cuadrado"

    plataforma3 = Plataforma()
    plataforma3.setXY(0, 2)
    plataforma3.setTamRect(20, 800)

    motor = MotorVideojuego()
    motor.entradaPersonajes([p1, p2,p3,Personaje(),Personaje(),Personaje(),Personaje(),Personaje(),Personaje()])
    motor.entradaPlataformas([plataforma, plataforma3, plataforma1])
    motor.conjuntoPersonajes = [p1]#, p2, p3]
    motor.conjuntoPlataformas = [plataforma, plataforma3, plataforma1]
    motor.start()
    start = pygame.time.get_ticks()/1000

    iter=0
    limit=1000
    while salir == False:

        lista=pygame.event.get()#((pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT, pygame.MOUSEBUTTONDOWN))
        for event in lista:
            #----------Escuchando Eventos del Usuario-#
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    pn = Personaje()
                    pn.setXY(x, y)
                    pn.tam_rectangulos((50, 50))
                    pn.actualizacionRec()
                    motor.conjuntoPersonajes.append(pn)
                    motor.tablaColisiones[pn.id] = []
                    #p1.setSalto(True)
                    #p1.setCaminar(True, False)
                    print "SAlta"
                if event.button == 2:
                    print "daniel: ", p1.getXY()
                    print "pedro: ", p2.getXY()
                    #motor.conjuntoPlataformas[1].setXY(400,400)
            if event.type == pygame.MOUSEMOTION:
                plataforma1.x_antes = plataforma1._x
                plataforma1.y_antes = plataforma1._y
                x, y = pygame.mouse.get_pos()
                plataforma1.setXY(x, y)


        motor.controlEventos.eventos(lista)
        pantalla.fill((0,0,240))
        if pygame.time.get_ticks()>limit:
            #print iter
            limit+=1000
            iter=0
        iter+=1


        pygame.draw.rect(pantalla, red, plataforma.rectangulo)
        pygame.draw.rect(pantalla, red, plataforma1.rectangulo)
        pygame.draw.rect(pantalla, red, plataforma3.rectangulo)
        for p in motor.conjuntoPersonajes:
            pygame.draw.rect(pantalla, green, p.rectangulo)
            lista = motor.tablaColisiones[p.id]
            """
            for elemento in lista:
                if elemento[1] == 1:
                    pygame.draw.rect(pantalla, darkBlue, p.rec2)
                if elemento[1] == 3:
                    pygame.draw.rect(pantalla, darkBlue, p.rec3)
                if elemento[1] == 0:
                    pygame.draw.rect(pantalla, darkBlue, p.rec1)
                if elemento[1] == 2:
                    pygame.draw.rect(pantalla, darkBlue, p.rec4)

            """
            if p.ady_left == True:
                pygame.draw.rect(pantalla, darkBlue, p.rec2)
            if p.ady_right == True:
                pygame.draw.rect(pantalla, darkBlue, p.rec3)
            if p.ady_down == True:
                pygame.draw.rect(pantalla, darkBlue, p.rec1)
            if p.ady_up == True:
                pygame.draw.rect(pantalla, darkBlue, p.rec4)

        reloj1.tick(60)
        pygame.display.update()
    motor.salirJuego = True
    pygame.quit()

main()