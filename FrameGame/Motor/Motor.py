import math
#from pygame.sprite import Group
from pygame import Rect
#from pygame import time as pygameWait
import pygame
from Eventos import* # eventos propios del usuario
import time
import copy
import threading
import time
from dimension import*
from Joystick import*
import math
from ..Game.Monito import Monito

ABJ = 0

COM_AND_COM = 0# tiene comportamiento y tambien le afectan otros comportamientos
COM_AND_SIN = 1# tiene comportamiento pero no le afectan otros comportamiento
SIN_AND_COM = 2# no tiene comportamiento pero si le afectan otros comportamiento
SIN_AND_SIN = 3# no tiene comportamiento y tampoco le afecton otros

class Group(object):
    def __init__(self):
        self.lista = []
        self.x = 0
        self.y = 0

    def add(self, obj):
        self.lista.append(obj)

    def remove(self, obj):
        self.lista.remove(obj)

    def inList(self, obj):
        if obj in self.lista:
            return True
        else:
            return False
    def draw(self, pantalla):
        for i in self.lista:
            pantalla.blit(i.imagen.sprite.image, (i.imagen.sprite.rect.left+self.x, i.imagen.sprite.rect.top+self.y))

class MotorJuego(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
        self.campoAccion = Rect(0,0,800,600)
        self.terminar = False
        self.offColision = False

        self.grupoRectangulos = Group()
        self.grupoSujetos = Group()

        self.universoEntorno = [] #entorno de rectangulos
        self.universoPersonajes = []
        self.Personajes = []
        self.dimension = Dimension(self.campoAccion)#movimiento del entorno
        self.entornoActivo = []
        self.person_Entorno =[]# es la suma de las dos listas activas del juego personaje y entorno
        self.sincronizacion = None

        self.joysticks = {}#numero de manillas

        self.eventosUsuario = Eventos_Protagonista()
        import os
        self.eventosUsuario.musica.addMixProtagonista("saltar", "sonido\saltarMario.wav")
        self.eventosUsuario.musica.addmusica("pixel","daniel.mp3")

        #self.eventosUsuario.musica.playMusica("pixel")
        self.listaEvento = []

        self.contador = 0
        self.tiempo = 0.0005
        #-----------------------------------------------------------------------
        #--------------------------------
        #-----------------------------------------------------------------------
        self.velocidad_tiempo = 30
        self.progreso_tiempo = self.velocidad_tiempo
        self.cont = 0
        self.debug = False
        self.nuevo_rect = None

    def addjoystick(self,idpersonaje, idjoystick=0):
        if self.joysticks.has_key(idjoystick):
            if type(idpersonaje) == list:
                lista = self.joysticks[idjoystick][1]
                lista.extend(idpersonaje)
            else:
                self.joysticks[idjoystick][1].append(idpersonaje)
        else:

            if type(idpersonaje) == list:
                self.joysticks[idjoystick]= (Joystick(idjoystick),idpersonaje)
            else:
                self.joysticks[idjoystick]= (Joystick(idjoystick),[idpersonaje])

    def setListener(self, lista):
        self.eventosUsuario.eventos(lista)
        for manilla in self.joysticks:
            self.joysticks[manilla][0].eventos(lista)

    def prosecarEventos(self):
        if len(self.Personajes)>0:
            self.eventosUsuario.comportamientoPRO(self.Personajes[self.eventP])

        for key in self.joysticks:

            (manilla, personajes1) = self.joysticks[key]
            for i in personajes1:
                manilla.comportamientoPRO(i)


    def colisiones(self):
        self.extenderLista()
        #print
        #print "EMPEZANDO ANALISIS DE COLICION"

        self.cont+=1

        for p in self.Personajes: # recorre todos los personajes activos
            #print "*** "+ p.nombre+" ***"
            p.ady_left = False
            p.ady_right = False
            p.ady_down = False
            p.ady_up = False

            p.choco_con_algo = False
            p.clsColision()
            self.__colision_entorno(p)
            p.pos_rectangulos()




        for p in self.Personajes:
            if p.ady_down == False:
                self.__colision_adyacencia(p, 1)
            if p.ady_left == False:
                self.__colision_adyacencia(p, 2)
            if p.ady_right == False:
                self.__colision_adyacencia(p, 3)
            if p.ady_up == False:
                self.__colision_adyacencia(p, 4)

        if self.debug == True:
            print "\n**************"
            print "despues del ENTORNO de colision"

            print self.Personajes[0].colisionando
            print self.Personajes[1].colisionando
            print self.Personajes[2].colisionando


        for p in self.Personajes:

            p.corriendo()
            p.saltando()
            p.caminando()
            p.pos_rectangulos()
            self.__colision_personaje(p)
            p.pos_rectangulos()
            p.estado()

        if self.debug == True:
            self.debug = False
            print "\n**************"
            print "despues del ALCANCE de colision"

            print self.Personajes[0].colisionando
            print self.Personajes[1].colisionando
            print self.Personajes[2].colisionando

    def __colision_entorno(self, p):
        (x,y) = p.coordenadas()
        self.nuevo_rect = p.imagen.sprite.rect.inflate(6,6)
        self.nuevo_rect.top = y-3#.move_ip(x, y)
        self.nuevo_rect.left = x-3
        if len(self.Personajes) > 0:
            """- problemas derivados con el break
            con breas el problemas es que no ahi un corte para que no ocurra una despenalizacion
            ---> otra es que con un break no se puelve a introducir el personaje dentro la lista"""
            #self.person_Entorno.pop(0)#problema de break push

            p.c1 = (200,100,200)
            p.c2 = (100,200,200)
            p.c3 = (100,100,200)
            p.c4 = (100,200,100)
            #----------------------------------colision con el entorno------------------------------------
            for entorno in self.entornoActivo:

                _isColision = False
                _lados = None
                _up = False
                _down = False
                _left = False
                _right = False

                if not self.nuevo_rect.colliderect(entorno.imagen.sprite.rect):#not collide_rect(nuevo_rect, entorno.imagen.sprite):
                    continue

                """esto del preambulo de la colision"""
                #caso raro de colision exclusivp del lado derecho del objeto
                rectangulo = entorno.lados[0]
                if rectangulo != None:#"colicion con el lado derecho del Personaje"
                    if rectangulo.colliderect(p.rec3):
                        _right= True
                        _isColision = True
                        _lados = 3
                    else:
                        #if self.ady_right == False:
                        if alcance(p, entorno, 3):
                            p.ady_right = True
                            p.colisionando[2] = True
                            p.c3 = (255, 0, 0)
##                        else:
##                            p.colisionando[2] = False


                #-----------------------------------------------------------
                rectangulo = entorno.lados[2]
                if rectangulo != None:#"colicion con el lado izquierdo del Personaje"
                    if rectangulo.colliderect(p.rec2):
                        _left = True
                        _isColision = True
                        _lados = 2
                    else:
                        if alcance(p, entorno, 2):
                            p.colisionando[1] = True
                            p.c2 = (255, 0, 0)
                            p.ady_left = True
##                        else:
##                            p.colisionando[1] = False



                #-----------------------------------------------------------
                rectangulo = entorno.lados[1]
                if rectangulo != None:#"colicion con el lado de arriba del Personaje"
                    if rectangulo.colliderect(p.rec4):
                        _up   = True
                        _isColision = True
                        _lados = 4
                    else:
                        if alcance(p, entorno, 4):
                            p.ady_up = True
                            p.colisionando[3] = True
                            p.c4 = (255, 0, 0)
##                        else:
##                            p.colisionando[3] = False


                #-----------------------------------------------------------
                rectangulo = entorno.lados[3]
                if rectangulo != None:#"colicion con el lado de abajo del Personaje"

                    if rectangulo.colliderect(p.rec1):
                        p.colisionando[0] = True
                        p.choco_con_algo = True
                        _down = True
                        _isColision = True
                        _lados = 1
                    else:
                        if alcance(p, entorno, 1):
                            p.ady_down = True
                            p.choco_con_algo = True
                            p.colisionando[0] = True
                            p.c1 = (255, 0, 0)
##                        else:
##                            p.colisionando[0] = False


                if _isColision == True:
                    lis1 = p.list_comp
                    lis2 = entorno.list_comp

                    if p.contexto == "default":
                        if _down == True:
                            restituir_pos(p,entorno,_lados)
                            p.setSalto(False)


                        if _left == True or  _right == True:
                            restituir_pos(p,entorno,_lados)
                            p.setCaminar(False)
                            p.setCorrer(False)
                            p.setSalto(False)
                            p.condicion = p.fail_salto
                            p.reseteo()

                        if _up == True:
                            restituir_pos(p,entorno,_lados)
                            #p.setSalto(False)
                            p.condicion = p.fail_salto
                            p.reseteo()


                    elif "Colision Elastica":
                        restituir_pos(p,entorno,_lados)
                        coliision_elastica(p, entorno, _lados)



    def __colision_adyacencia(self, p, _lados):
        for entorno in self.Personajes:

            if id(p) == id(entorno):
                continue

            if alcance(p, entorno, 1) and _lados == 1:#por debajo
                if entorno.ady_down == False:
                    self.__colision_adyacencia(entorno, 1)

                p.colisionando[0] = entorno.colisionando[0]
                p.ady_down = True


                if p.colisionando[0]:
                    p.choco_con_algo = True
                    p.c1 = (255, 0, 0)
                    return True

            #-----------------------------------------------------------

            if alcance(p, entorno, 2) and _lados == 2:
                if entorno.ady_left == False:
                    self.__colision_adyacencia(entorno, 2)

                p.colisionando[1] = entorno.colisionando[1]
                p.ady_left = True


                if p.colisionando[1]:
                    p.c2 = (255, 0, 0)
                    return True

            #-----------------------------------------------------------

            if alcance(p, entorno, 3) and _lados == 3:
                if entorno.ady_right ==  False:
                    self.__colision_adyacencia(entorno, 3)

                p.colisionando[2] = entorno.colisionando[2]
                p.ady_right = True

                if p.colisionando[2]:
                    p.c3 = (255, 0, 0)
                    return True

            #-----------------------------------------------------------

            if alcance(p, entorno, 4) and _lados == 4:
                if entorno.ady_up == False:
                    self.__colision_adyacencia(entorno, 4)

                p.colisionando[3] = entorno.colisionando[3]
                p.ady_up = True

                if p.colisionando[3]:
                    p.c4 = (255, 0, 0)
                    return True


        if _lados == 1:
            p.colisionando[0] = False
            p.ady_down = True

        elif _lados == 2:
            p.colisionando[1] = False
            p.ady_left = True

        elif _lados == 3:
            p.colisionando[2] = False
            p.ady_right = True

        elif _lados == 4:
            p.colisionando[3] = False
            p.ady_up = True

        return False



            #self.person_Entorno.append(p)

    def __colision_personaje(self, p):
        for entorno in self.Personajes:

            _isColision = False
            _lados = None
            _up = False
            _down = False
            _left = False
            _right = False

            if id(p) == id(entorno):
                continue


            if p.rec1.colliderect(entorno.rec4):#por debajo
                p.choco_con_algo = True
                _down = True
                _isColision = True
                _lados = 1

            #-----------------------------------------------------------


            if p.rec2.colliderect(entorno.rec3):#por izquierda
                _left = True
                _isColision = True
                _lados = 2

            #-----------------------------------------------------------

            if p.rec3.colliderect(entorno.rec2):#por derecha
                _right= True
                _isColision = True
                _lados = 3

            #-----------------------------------------------------------

            if p.rec4.colliderect(entorno.rec1) :#por arriba
                _up   = True
                _isColision = True
                _lados = 4


            if _isColision == True:
                lis1 = p.list_comp
                lis2 = entorno.list_comp

                if p.contexto == "default":
                    #---------------------------colision primitivo------------------------------------
                    if (lis1[0] == True and lis2[1] == True) or (lis1[1] == True and lis2[0] == True):

                        if (lis1[0] == True and lis2[1] == True) and (lis1[1] == True and lis2[0] == True):
                                """el problema consiste en qu cuando el obejto sale de la pila la gravedad actua sobre este objeto vigente
                                """
                                #print "ahora se que no deveria"
                                if _down == True:
                                    restituir_pos(p, entorno,_lados)
                                    #caminar por la superficie de otro personaje
                                    p.setSalto(False)

                                if _up == True:
                                    if not isMuro(p, 1):
                                        restituir_pos(p, entorno, _lados)
                                        p.setSalto(True)
                                        p.condicion = p.fail_salto
                                        p.reseteo()
                                    else:
                                        restituir_pos(entorno, p, _lados, True)
                                        entorno.setSalto(False)


                                if _left == True or _right == True:
                                    restituir_pos(p, entorno, _lados)
                                    p.setCaminar(False)
                                    p.setSalto(False)
                                    p.condicion = p.fail_salto
                                    p.reseteo()
                        else:

                            move, quien = quienSemueve(lis1, lis2)

                            if move:
                                if quien == 1:
                                    if _up == True:
                                        if not isMuro(p, 1):
                                            restituir_pos(p, entorno, _lados)
                                            p.setSalto(True)
                                            p.condicion = p.fail_salto
                                            p.reseteo()
                                        else:
                                            restituir_pos(entorno, p, _lados, True)
                                            entorno.setSalto(False)


                                    if _down == True:

                                        restituir_pos(p, entorno, _lados)
                                        p.setSalto(False)


                                    if _left == True:
                                        if not isMuro(p, 3):
                                            restituir_pos(p,entorno,_lados)
                                            p.setCaminar(False)
                                            p.setCorrer(False)
                                            if p.ady_down == False:
                                                p.setSalto(True)
                                            p.condicion = p.fail_salto
                                            p.reseteo()
                                        else:
                                            restituir_pos(entorno, p, _lados, True)
                                            entorno.setCaminar(False)
                                            entorno.setCorrer(False)
                                            entorno.reseteo()

                                    if _right == True:
                                        if not isMuro(p, 2):
                                            restituir_pos(p,entorno,_lados)
                                            p.setCaminar(False)
                                            p.setCorrer(False)
                                            if p.ady_down == False:
                                                p.setSalto(True)
                                            p.condicion = p.fail_salto
                                            p.reseteo()
                                        else:
                                            restituir_pos(entorno, p, _lados, True)
                                            entorno.setCaminar(False)
                                            entorno.setCorrer(False)
                                            entorno.reseteo()
                                elif quien == 2:
                                    pass

                            """el problema es que entra en los dos if porque yo modifique el modelo para que se pregunte dos veces
                            dos mismos objetos, en tal caso ahi invariacion"""




                    if (lis1[2] == True and lis2[3] == True) or (lis1[3] == True and lis2[2] == True):
                        pass

                elif "Colision Elastica":
                    restituir_pos(p,entorno,_lados)
                    restituir_pos(entorno,p,_lados, True)
                    coliision_elastica(p, entorno,_lados)

        if p.contexto == "default":
            gravedadActua(p.choco_con_algo, p)
    def extenderLista(self):
        self.person_Entorno = []
        self.person_Entorno.extend(self.entornoActivo)
        self.person_Entorno.extend(self.Personajes)



#   esto solo maneja universo del entorno
    def metodo1(self):
        #self.entornoActivo = []
        #self.grupoRectangulos.empty()
        #self.grupoRectangulos.update()
        for i in self.universoEntorno:
            if self.campoAccion.colliderect(i.imagen.sprite):
                if  self.grupoRectangulos.inList(i) == False:
                    self.entornoActivo.append(i)
                    self.grupoRectangulos.add(i)
            else:
                if i in self.entornoActivo:
                    self.grupoRectangulos.remove(i)
                    self.entornoActivo.remove(i)



#   esto maneja sujetos pero no trabaja con protagonista
    def metodo2(self):
        #self.Personajes = []
        #self.grupoSujetos.empty()
        #self.grupoSujetos.update()
        for i in self.universoPersonajes:
            if self.campoAccion.colliderect(i.imagen.sprite):#optimizar
                if self.grupoSujetos.inList(i) == False:
                    self.grupoSujetos.add(i)
                    self.Personajes.append(i)
            else:
                if i in self.Personajes:
                    self.grupoSujetos.remove(i)
                    self.Personajes.remove(i)


    def modelo_experimenal_1(self):
        #persoanje_temp = self.universoPersonajes# personajes temporales
##        #self.dimension.setEstilo("personaje")
##        self.dimension.setPersonaje(self.universoPersonajes[1])
##        #self.dimension.setMovAutonomo("izquierda", "acelerado")
##        self.dimension.setEstilo("autonomo")
##        self.dimension.setMovAutonomo("izquierda", "constante")
        self.numero = 0
        print "INICIO EL PROCESO HERMANO"
        start_time = time.time()


        self.eventP = 0
        while(self.terminar == False):
            self.metodo1()#pregunta quien esta afuera y adentro
            self.metodo2()

            self.prosecarEventos()

            self.colisiones()
            #self.dimension.centrado(self.grupoSujetos, self.grupoRectangulos)
            self.numero +=1
            pygame.time.wait(16)
            #pygameWait.wait(1/120.0)
            #time.sleep(1/120.0)
            #persoanje_temp[1].comportamiento()

##            for i in persoanje_temp:
##                i.estado()
##                if self.offColision == False:
##                    DinamismoEntorno(i,self.entornoActivo)
        time1 = time.time() - start_time
        print "TIEMPO FINALIZADO: "+str(time1)
    def modelo_experimenal_2(self):

        if self.contador == 0:
            print "INICIO EL PROCESO HERMANO"
            self.start_time = time.time()

        self.eventP = 0
        self.metodo1()#pregunta quien esta afuera y adentro
        self.metodo2()
        self.prosecarEventos()
        self.colisiones()
        self.dimension.centrado(self.grupoSujetos, self.grupoRectangulos)
        self.contador+=1
        if self.contador >=100:
            time1 = time.time() - self.start_time
            #print "TIEMPO FINALIZADO: "+str(time1)



    def run(self):
        self.modelo_experimenal_1()

    def addRectangulo(self,rectangulo):
        self.universoEntorno.append(rectangulo)

    def addListRec(self,listaRec):
        self.universoEntorno = listaRec

    def addListPersonajes(self, listPer):
        self.universoPersonajes = listPer

    def addPersonaje(self, personaje):
        self.universoPersonajes.append(personaje)

    def getEventos(self, listaE):
        self.listaEvento = listaE

    def imprimirEntorno(self,pantalla):
        self.grupoRectangulos.draw(pantalla)

    def imprimirPersonaje(self,pantalla):
        self.grupoSujetos.draw(pantalla)

    def imprimirPoligonoPersonaje(self, pantalla):
        for i in self.Personajes:
            pygame.draw.rect(pantalla, i.c1, i.rec1) #abajo
            pygame.draw.rect(pantalla, i.c2, i.rec2)
            pygame.draw.rect(pantalla, i.c3, i.rec3)
            pygame.draw.rect(pantalla, i.c4, i.rec4)#arriba


    def imprimirPoligonoEntorno(self, pantalla):

        for l in self.entornoActivo:
            for i in l.lados:
                if i != None:
                    pygame.draw.rect(pantalla, (200,200,200),i)

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
        p.imagen.sprite.rect.top = entorno.imagen.sprite.rect.top - p.rec_size[1]+ABJ
    elif _lado == 2:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left + entorno.imagen.sprite.rect.size[0] + 3
    elif _lado == 3:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left - p.imagen.sprite.rect.size[0] - 3
    elif _lado == 4:
        p.imagen.sprite.rect.top  = entorno.imagen.sprite.rect.top + entorno.imagen.sprite.rect.size[1] + 2
    p.pos_rectangulos()




def alcance (p, entorno, lado):
    if issubclass(type(entorno), Monito):# entorno.__class__.__name__ == "Personaje" or entorno.__class__.__name__ == "Monito":
        if lado == 1:
            rectangulo = entorno.rec4
        elif lado == 2:
            rectangulo = entorno.rec3
        elif lado == 3:
            rectangulo = entorno.rec2
        elif lado == 4:
            rectangulo = entorno.rec1

    else:
        if lado == 1:
            rectangulo = entorno.lados[3]
        elif lado == 2:
            rectangulo = entorno.lados[2]
        elif lado == 3:
            rectangulo = entorno.lados[0]
        elif lado == 4:
            rectangulo = entorno.lados[1]

    colision = False

    if lado == 1:
        p.rec1.top = p.rec1.top + 1
        if p.rec1.colliderect(rectangulo):#por debajo
            colision = True
        p.rec1.top = p.rec1.top - 1

    elif lado == 2:
        p.rec2.left-=4
        if p.rec2.colliderect(rectangulo):#por izquierd
            colision = True
        p.rec2.left+=4

    elif lado == 3:
        p.rec3.left+=4
        if p.rec3.colliderect(rectangulo):#por derecha
            colision = True
        p.rec3.left-=4

    elif lado == 4:
        p.rec4.left-=1
        if p.rec4.colliderect(rectangulo):#por arriba
            colision = True
        p.rec4.left+=1

    return colision

def quienSemueve(lis1, lis2):

     if lis1[0] and  lis1[1] and lis2[0] and not lis2[1]:
        return True, 2

     if lis1[0] and  lis1[1] and not lis2[0] and lis2[1]:
        return True, 1

     if lis1[0] and  not lis1[1] and lis2[0] and lis2[1]:
        return True, 1

     if lis1[0] and not lis1[1] and not lis2[0] and lis2[1]:
        return True, 1

     if not lis1[0] and  lis1[1] and lis2[0] and lis2[1]:
        return True, 2

     if not lis1[0] and  lis1[1] and lis2[0] and not lis2[1]:
        return True, 2

     return False, 0

def Sistema_inteligente_choque():
    pass



def gravedadActua(choco_con_algo, DinaP):
    if choco_con_algo == False:#osea que no choco con nada
        if DinaP.salto == False:
            DinaP.setSalto(True)
            DinaP.setCaminar(False)
            DinaP.setCorrer(False)
            DinaP.condicion = DinaP.fail_salto
            DinaP.reseteo()

def coliision_elastica(objeto1, objeto2, _lados, sinperdida = False):
    if objeto1.Info[3] == None:
        return None
    (p1vx, p1vy) = objeto1.Info[3]
    paredes = False

    if objeto2.__class__.__name__ == "rectangulos":
        paredes = True
        (p2vx, p2vy) = (0.0, 0.0)
        if _lados == 1:
            p1vy = -p1vy
        elif _lados == 2:
            p1vx = -p1vx
        elif _lados == 3:
            p1vx = -p1vx
        elif _lados == 4:
            p1vy = -p1vy

        masa_p2 = objeto2.imagen.tam[2] * objeto2.imagen.tam[3]

    else:
        (p2vx, p2vy) = objeto2.Info[3]
        masa_p2 = objeto2.masa

    masa_p1 =  objeto1.masa#objeto1.imagen.tam[2] * objeto1.imagen.tam[3]


    newV_p1x = funcion_velocidad(p1vx, masa_p1, p2vx, masa_p2)
    newV_p1y = funcion_velocidad(p1vy, masa_p1, p2vy, masa_p2)

    newV_p2x = funcion_velocidad(p2vx, masa_p2, p1vx, masa_p1)
    newV_p2y = funcion_velocidad(p2vy, masa_p2, p1vy, masa_p1)

    print "masa1  : "+str(masa_p1)
    print "velo1x : "+str(newV_p1x)
    print "velo1y : "+str(newV_p1y)


    if paredes == True:
        angulo1 = math.degrees(math.atan2(p1vy, p1vx))

    else:
        angulo1 = math.degrees(math.atan2(newV_p1y, newV_p1x))

    if sinperdida == True:
        velo_p1 = math.sqrt(math.pow(p1vx,2)+math.pow(p1vy,2))
    else:
        velo_p1 = math.sqrt(math.pow(newV_p1x,2)+math.pow(newV_p1y,2))

    print "velocidad : "+str(velo_p1)
    print "angulo    : "+str(angulo1)
    #if angulo1 < 0:
    #    angulo1 = 360+angulo1
    #angulo1 = 360-angulo1
    objeto1.setSalto(True)
    objeto1.reseteo()

    objeto1.condicion=(None, velo_p1, angulo1, 9.8)

    if objeto2.__class__.__name__ == "Personaje":
        if sinperdida:
            velo_p2 = math.sqrt(math.pow(p2vx,2)+math.pow(p2vy,2))
        else:
            velo_p2 = math.sqrt(math.pow(newV_p2x,2)+math.pow(newV_p2y,2))
        angulo2 = math.degrees(math.atan2(newV_p2y, newV_p2x))
        objeto2.setSalto(True)
        objeto2.reseteo()
        objeto2.condicion=(None, velo_p2, angulo2, 9.8)


def funcion_velocidad(xSpeedFirst, xMassFirst, ySpeedSecond, yMassSecond):
    newVelX = (xSpeedFirst *(xMassFirst- yMassSecond) + (2 * yMassSecond * ySpeedSecond)) / (xMassFirst + yMassSecond)
    return newVelX

def isMuro(p, lado):
    if p.__class__.__name__ == "rectangulos":
        return True
    return p.colisionando[lado-1]
