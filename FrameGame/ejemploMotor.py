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
    p1._x = 400
    p1._y = 100
    p1.tam_rectangulos((70, 70))
    p1.actualizacionRec()

    p2 = Personaje()
    p2._x = 100
    p2._y = 200
    p2.tam_rectangulos((100, 100))
    p2.actualizacionRec()

    plataforma = Plataforma()
    plataforma.setXY(0, 554)
    plataforma.setTamRect(800, 70)

    plataforma1 = Plataforma()
    plataforma1.setXY(300, 400)
    plataforma1.setTamRect(800, 2)

    motor = MotorVideojuego()
    motor.entradaPersonajes([p1, p2,Personaje(),Personaje(),Personaje(),Personaje(),Personaje(),Personaje(),Personaje()])
    motor.conjuntoPersonajes = [p1, p2]
    motor.conjuntoPlataformas = [plataforma, plataforma1]
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
                    #p1.setSalto(True)
                    p1.setCaminar(True, False)
                    print "SAlta"
                if event.button == 2:
                    motor.conjuntoPlataformas[1].setXY(400,400)


        motor.controlEventos.eventos(lista)
        pantalla.fill((0,0,240))
        if pygame.time.get_ticks()>limit:
            print iter
            limit+=1000
            iter=0
        iter+=1


        pygame.draw.rect(pantalla, red, plataforma.rectangulo)
        pygame.draw.rect(pantalla, red, plataforma1.rectangulo)
        for p in motor.conjuntoPersonajes:
            if p.ady_down == True:
                pygame.draw.rect(pantalla, white, p.rectangulo)
            else:
                pygame.draw.rect(pantalla, green, p.rectangulo)
        reloj1.tick(60)
        pygame.display.update()
    motor.salirJuego = True
    pygame.quit()

main()