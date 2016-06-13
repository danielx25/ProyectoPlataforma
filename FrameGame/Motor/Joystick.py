import pygame.locals
import sys
VELOCIDAD = sys.argv[0]
VELO = 75
GRAVEDAD = 15.8
import music
import math

class Joystick(object):

    def __init__(self, id):

        self.id = id
        self.saltar1 = False
        self.caminar1 = False
        self.correr1 = False

        self.orden = True #         True: derecha || False: izquierda quien manda
        self.derecha = False
        self.izquierda = False
        self._DEcaminar1 = True #   dejar de caminar
        self._right = False #       derecha en salto
        self._left  = False#        izquie en salto

        self.velocidad = VELOCIDAD

        self.musica = music.entornoMusic()
        """self.arriba = False
        self.abajo = False
        self.izquierda = False
        self.derecha = False"""
        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()

    def eventos(self, lista):

        for event in lista:
            if event.type == pygame.JOYBUTTONDOWN:#presiona cualquier tecla
                if self.joystick.get_button(0):# k_z
                    print "SALTAR"
                    self.saltar1 = True

                if self.joystick.get_button(2):# k_x
                    self.correr1 = True
                    self._DEcaminar1 = True

            if event.type == pygame.JOYBUTTONUP:#despresiona cualquier tecla
                if self.joystick.get_button(0) == False:
                    self.saltar1 = False

                if self.joystick.get_button(2) == False:# k_x
                    self.correr1 = True
                    self._DEcaminar1 = True

        direccion = self.joystick.get_hat(0)
        if direccion == (1,0):#derecha
            self.caminar1 = True
            self.derecha = True
            self.orden = True

            self.izquierda = False
            self._left = False

        if direccion == (-1,0):#izquierda
            self.caminar1 = True
            self.izquierda = True
            self.orden = False

            self.derecha = False
            self._right = False

        if direccion == (0,0):#no precionado
            self.derecha = False
            self.izquierda = False
            self._left = self._right = False


    def comportamientoPRO(self , protagonista):
##        if self.saltar1 == True:
##            if protagonista.getSalto()==False:
##                protagonista.setSalto(True)
##                protagonista.condicion=(None, 60, 90, 9.8)
##                protagonista.reseteo()

        if self.caminar1:
            if protagonista.getSalto() == False and protagonista.getCorrer() == False:
                if self.derecha == False and self.izquierda == False:
                    protagonista.setCaminar(False)
                    self.caminar1 = False
                else:

                    if self.derecha == False or  self.izquierda == False:

                        if self.derecha:

                            if protagonista.getDirec() == False and protagonista.getCaminar() == True:
                                protagonista.setCaminar(False)

                            if protagonista.getCaminar() == False:
                                protagonista.reseteo()
                                protagonista.setCaminar(True, True)
                        else:
                            if protagonista.getDirec() == True and protagonista.getCaminar() == True:
                                protagonista.setCaminar(False)

                            if protagonista.getCaminar() == False:
                                protagonista.reseteo()
                                protagonista.setCaminar(True, False)
                    else:
                        if self.orden:#primero derecha
                            if protagonista.getDirec() == False and protagonista.getCaminar() == True:
                                protagonista.setCaminar(False)

                            if protagonista.getCaminar() == False:
                                protagonista.reseteo()
                                protagonista.setCaminar(True, True)
                        else:
                            if protagonista.getDirec() == True and protagonista.getCaminar() == True:
                                protagonista.setCaminar(False)

                            if protagonista.getCaminar() == False:
                                protagonista.reseteo()
                                protagonista.setCaminar(True, False)


        if self.correr1:
            if protagonista.getCaminar():
                protagonista.setCaminar(False)

            if protagonista.getSalto() == False and protagonista.getCaminar() == False:
                if self._DEcaminar1 == False:
                    protagonista.setCorrer(False,False)
                    self.correr1 = False
                    return None

                if self.derecha == False and self.izquierda == False:
                    protagonista.setCorrer(False,False)

                else:
                    if self.derecha == False or  self.izquierda == False:

                        if self.derecha:

                            if protagonista.getDirec() == False and protagonista.getCorrer() == True:
                                protagonista.setCorrer(False)

                            if protagonista.getCorrer() == False:
                                protagonista.reseteo()
                                protagonista.setCorrer(True, True)
                        else:
                            if protagonista.getDirec() == True and protagonista.getCorrer() == True:
                                protagonista.setCorrer(False)

                            if protagonista.getCorrer() == False:
                                protagonista.reseteo()
                                protagonista.setCorrer(True, False)
                    else:
                        if self.orden:#primero derecha
                            if protagonista.getDirec() == False and protagonista.getCorrer() == True:
                                protagonista.setCorrer(False)

                            if protagonista.getCorrer() == False:
                                protagonista.reseteo()
                                protagonista.setCorrer(True, True)
                        else:
                            if protagonista.getDirec() == True and protagonista.getCorrer() == True:
                                protagonista.setCorrer(False)

                            if protagonista.getCorrer() == False:
                                protagonista.reseteo()
                                protagonista.setCorrer(True, False)


        if protagonista.getSalto():
            if self.derecha == True or  self.izquierda == True:
                (p1vx, p1vy) = protagonista.Info[3]
                angulo1 = math.degrees(math.atan2(p1vy, p1vx))
                velo_p1 = math.sqrt(math.pow(p1vx,2)+math.pow(p1vy,2))
                if self.derecha and self._right==False:
                    print "1"
                    self._right = True
                    if p1vy > 0:
                        protagonista.condicion=(None, velo_p1, 65, 9.8)
                    else:
                        protagonista.condicion=(None, velo_p1, 295, 9.8)

                    protagonista.reseteo()
                if self.izquierda == True and self._left == False:
                    print "2"
                    self._left = True
                    if p1vy > 0:
                        protagonista.condicion=(None, velo_p1, 115, 9.8)
                    else:
                        protagonista.condicion=(None, velo_p1, 245, 9.8)

                    protagonista.reseteo()
                    #protagonista.condicion=(None, 40, 245, 9.8)


        if self.saltar1:
            if protagonista.getSalto() == False:
                if protagonista.getCorrer() == True or protagonista.getCaminar() == True:
                    protagonista.setCorrer(False)
                    protagonista.setCaminar(False)

                if self.derecha == False and self.izquierda == False:
                    protagonista.setSalto(True)
                    protagonista.reseteo()
                    protagonista.condicion=(None, 60, 90, 9.8)
                else:
                    if self.derecha == False or  self.izquierda == False:
                        if self.derecha:
                            protagonista.setSalto(True)
                            protagonista.reseteo()
                            protagonista.condicion=(None, 60, 65, 9.8)
                        else:
                            protagonista.setSalto(True)
                            protagonista.reseteo()
                            protagonista.condicion=(None, 60, 115, 9.8)
                    else:
                        if self.orden:#primero derecha
                            protagonista.setSalto(True)
                            protagonista.reseteo()
                            protagonista.condicion=(None, 60, 65, 9.8)
                        else:
                            protagonista.setSalto(True)
                            protagonista.reseteo()
                            protagonista.condicion=(None, 60, 115, 9.8)


