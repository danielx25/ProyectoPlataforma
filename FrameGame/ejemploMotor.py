import pygame
from Motor import*

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


def ejemploScript(plataforma):
    #pass
    #return 1
    plataforma.x_antes = plataforma._x
    plataforma._x+=1

    plataforma.y_antes = plataforma._y
    plataforma._y += -3

    if plataforma._y < 20:
        plataforma.setXY(plataforma._x, 400)



def main():

    pygame.init()
    pantalla=pygame.display.set_mode((1000,800))
    pygame.FULLSCREEN


    pygame.display.set_caption("ProyectoPygame")
    reloj1=pygame.time.Clock()
    salir=False

    p1 = Personaje()
    p1.setXY(300, 300)
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
    plataforma.setTamRect(800, 20)

    plataforma1 = Plataforma()
    plataforma1.setXY(300, 400)
    plataforma1.setTamRect(50, 50)
    plataforma1.id = "cuadrado"

    plataforma3 = Plataforma()
    plataforma3.setXY(0, 2)
    plataforma3.setTamRect(20, 800)

    motor = MotorVideojuego()
    motor.entradaPersonajes([p1, p2,p3,Personaje(),Personaje(),Personaje(),Personaje(),Personaje(),Personaje()])
    motor.entradaPlataformas([plataforma1, plataforma, plataforma3])
    motor.conjuntoPersonajes = [p1]#, p2, p3]
    motor.conjuntoPlataformas = [ plataforma1, plataforma, plataforma3]
    #motor.start()
    start = pygame.time.get_ticks()/1000

    #==============
    motor.diccionarioScripts[plataforma1.id].append(ejemploScript)
    motor.protagonista = motor.conjuntoPersonajes[0]
    iter=0
    limit=1000
    contador =0
    while salir == False:

        lista=pygame.event.get()#((pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT, pygame.MOUSEBUTTONDOWN))
        for event in lista:
            #----------Escuchando Eventos del Usuario-#
            if event.type == pygame.QUIT:
                salir = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    motor.procesoVideoJuego()
                    contador+=1
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
                pass
                #plataforma1.x_antes = plataforma1._x
                #plataforma1.y_antes = plataforma1._y
                #x, y = pygame.mouse.get_pos()
                #plataforma1._x = x
                #plataforma1._y = y
        motor.controlEventos.eventos(lista)
        #if contador < 180:
        motor.procesoVideoJuego()
        #contador+=1
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
            desmarcar = 200
            des = 100
            pygame.draw.rect(pantalla, red, (desmarcar + 402.0 ,-13.0+des, 100, 100))
            pygame.draw.rect(pantalla, green, (desmarcar + 403.0 ,15.0+des, 100, 100),3)
            pygame.draw.rect(pantalla, green, (desmarcar + 405.0 ,85.0+des, 50, 50),3)
            pygame.draw.rect(pantalla, black, (desmarcar + 404 ,88+des, 50, 50))
        reloj1.tick(60)
        pygame.display.update()
    motor.salirJuego = True
    pygame.quit()

main()
