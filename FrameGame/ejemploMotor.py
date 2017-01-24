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
    p1._x = 300
    p1._y = 300
    p1.tam_rectangulos((70, 70))
    p1.actualizacionRec()

    p2 = Personaje()
    p2._x = 100
    p2._y = 200
    p2.tam_rectangulos((100, 100))
    p2.actualizacionRec()

    motor = MotorVideojuego()
    motor.conjuntoPersonajes = [p1, p2]
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
                    p1.setSalto(True)
                    print "SAlta"
        pantalla.fill((0,0,240))
        if pygame.time.get_ticks()>limit:
            print iter
            limit+=1000
            iter=0
        iter+=1
        pygame.draw.rect(pantalla, red, p1.rectangulo)
        reloj1.tick(120)
        pygame.display.update()
    motor.salirJuego = True
    pygame.quit()

main()