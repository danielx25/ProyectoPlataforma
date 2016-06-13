"""
Esta clase interactua el jugador con el protagonista del juego, tiene atributos y metodos importantes.
Metodos:
Saltar (): metodo que le permite al protagonista hacer un movimiento parabolico
Correr ():  se explica por si mismo

Tambien este paquete contiene funciones que son necesarios para poder hacer que funcione la clase monito
Funciones:
Radianes (): convierte angulo a radianes
mov_parabolico (): se pasan los parametros necesario para dibujar la parabola
InstanAng(): retorna en cada instante que angulo tiene cualquier objeto

"""
import uuid
import sys
from ..Imagenes.Sprites import *

#from Imagenes.Sprites import Sprites
from Fisica import*
from ..Game.Animacion import*
from pygame import Rect



VELOCIDAD = sys.argv[0]

from tiempo import Tiempo

Con_Comportamiento = 1#


class Personaje(object):#con la clase imagen esta clases interctua con el entorno

    def __init__(self, *arg, **argv):#name = None, link = ""):# imagen, sprite, path, objeto animacion
        self.rec1= Rect(0,0,0,0)
        self.rec2= Rect(0,0,0,0)
        self.rec3= Rect(0,0,0,0)
        self.rec4= Rect(0,0,0,0)
        self.animacion = None

        if isinstance(arg[0], AnimaPersonaje):
            self.conAnimacion = True
            self.animacion = arg[0]
            self.imagen = self.animacion.imagActual
        else:
            name = "default"
            link = arg[0]
            self.imagen = Sprites(link)



        self.rec_size = self.imagen.sprite.rect.size
        self.tam_rectangulos()
        self.pos_rectangulos()

        self.id = uuid.uuid1()

        #self.var_correr = (0.1, 70, 180, 0)#velocidad_tiempo, velocidad, aceleracion
        #self.var_caminar = (0.1, 30, 0, 0)#velocidad constante
        self.x_impr = 0
        self.y_impr = 0


        self.coorx = self.coory = 0
        self.salto = False
        self.correr= False
        self.caminar = False
        self.masa = 30
        self.tiempo = 0 #tiempo trancurso
        self.var_salto = (VELOCIDAD, 40, 45, 9.8)# velocidad_tiempo, velocidad, angulo, gravedad 0.0025
        self.fail_salto = (0.006, 50.0, 270, 15.8)
        self.condicion = self.var_salto
        self.direccion = True
        self.angulo = None
        self.choco_con_algo = False

        self.cronometro = Tiempo()


        self.Info = [[],None, None, None]#primer guarda coordenadas segunda algulo tercera la velocidades | la cuarta es la velocidad vectorial

        '''
        INPRIM: comportamiento primitivo interno que lo genera el entorno o un personaje

        OUTPRIM: comportamiento primitivo externo que genera a otro personaje

        PROPCOMP: comportamiento de propagacion es una funcion que se traspasa a otro personaje o entorno atravez de una colision o evento

        RECIVCOMP: es la recepcion o no de un comportamiento
        '''
        self.list_comp = [True, False, False, False]#este es comportamiento canonico de un personaje cualquiera
        self.colisionando = [False, False, False, False]# abajo, izq, derecha, arriba

        self.ady_left = False
        self.ady_right = False
        self.ady_down = False
        self.ady_up = False

        self.compActual = None
        self.compEstatico = None
        self.compDinaminco = None

        self.comportamiento = None #   funcion de comportamiento
        self.pasivaComp = False # activar o desactivar el comportamineto

        self.contexto ="default"
    def getID(self):
        return self.id

    def clsColision(self):
##        if self.list_comp[0] == False and self.list_comp[1] == True:
##            self.colisionando[0] = True
##            self.colisionando[1] = True
##            self.colisionando[2] = True
##            self.colisionando[3] = True
##        else:
        self.colisionando[0] = False
        self.colisionando[1] = False
        self.colisionando[2] = False
        self.colisionando[3] = False

    def getLColl(self, _lado):
        return self.colisionando[i]

    def estado(self):

        if self.pasivaComp:
            self.comportamiento(self)
    def tam_rectangulos(self):
        self.rec1.width, self.rec1.height = (self.rec_size[0]/2.0, self.rec_size[1]/4.0)
        self.rec2.width, self.rec2.height = (self.rec_size[0]/4.0, self.rec_size[1]/2.0)
        self.rec3.width, self.rec3.height = (self.rec_size[0]/4.0, self.rec_size[1]/2.0)
        self.rec4.width, self.rec4.height = (self.rec_size[0]/2.0, self.rec_size[1]/4.0)


    def pos_rectangulos(self):
        (self.rec1.left, self.rec1.top) = (self.imagen.sprite.rect.left+(self.rec_size[0]/4.0), self.imagen.sprite.rect.top + self.imagen.sprite.rect.height - self.rec1.height)#+ 3*(self.rec_size[1]/4.0))#abajo
        (self.rec2.left, self.rec2.top) = (self.imagen.sprite.rect.left, self.imagen.sprite.rect.top+(self.rec_size[1]/4.0))
        (self.rec3.left, self.rec3.top) = (self.imagen.sprite.rect.left + self.imagen.sprite.rect.width- self.rec3.width, self.imagen.sprite.rect.top+(self.rec_size[1]/4.0))
        (self.rec4.left, self.rec4.top) = (self.imagen.sprite.rect.left+(self.rec_size[0]/4.0), self.imagen.sprite.rect.top)


    def imprimir(self, pantalla):
        if self.canFprint == True:
            pantalla.blit(self.imagen.sprite.image, self.imagen.sprite.rect)
            self.canFprint  = False

    def saltando(self,):
        if self.salto == False and self.correr== False and self.caminar== False:
            """EL CAMBIO DE DIRECCION AFECTA LA FUNCIONALIDAD
            velocidad inic: 55
            angulo        : 90
            tiempo        : 1419806606.77
            gravedad      : 15.8
            coordenadas   : (4.781594445060046e-06, 1.5925221246802495e+19)"""
            self.cronometro.modPasivo()
            self.coorx =  self.imagen.sprite.rect.left
            self.coory =  self.imagen.sprite.rect.top
            self.Info[3] = (0.0,0.0)

        if self.salto == True and self.correr == False  and self.caminar == False:
            t = self.cronometro.cronometroC()
            #if t != None:
            self.tiempo = t#self.tiempo + self.condicion[0]
            try:
                tupla =  mov_parabolico(self.Info ,self.condicion[1],self.coory,self.condicion[2],self.tiempo,self.condicion[3])
                (h,self.imagen.sprite.rect.top) = tupla
            except TypeError:
                print "velocidad inic: "+ str(self.condicion[1])
                print "angulo        : "+ str(self.condicion[2])
                print "tiempo        : "+ str(self.tiempo)
                print "gravedad      : "+ str(self.condicion[3])
                print "info[0]       : "+ str(self.Info[0])
                print "mov_parabolico   : "+ str(tupla)
            self.imagen.sprite.rect.left = self.coorx + h
            self.record = self.tiempo
            self.angulo = self.Info[1]

    def corriendo(self,):
        if self.salto == False and self.correr== False and self.caminar== False:
            self.cronometro.modPasivo()
            self.coorx =  self.imagen.sprite.rect.left
            self.coory =  self.imagen.sprite.rect.top

        if self.correr== True and self.salto == False and self.caminar== False:#           aceleracion |            disancia inicial | velocidad inicial
            t = self.cronometro.cronometroC()


            velocidad = 20
            aceleracion = 6

            if self.direccion == True:
                #self.imagen.sprite.rect.left = x
                self.angulo = 0
            else:
                #self.imagen.sprite.rect.left = self.coorx -(x-self.coorx)
                self.angulo = 180
                velocidad*=-1
                aceleracion*=-1

            vel_t = aceleracion*t + velocidad
            self.Info[1] = vel_t
            self.Info[2] = self.angulo
            x = mov_recAcelerado(t, aceleracion, velocidad, self.coorx)#mov_recUniforme(t, 20, self.coorx)#0.5* 20* self.tiempo*self.tiempo + self.coorx + 60*self.tiempo
            self.imagen.sprite.rect.left = x

    def caminando(self):
        if self.salto == False and self.correr== False and self.caminar== False:
            self.cronometro.modPasivo()
            self.coorx =  self.imagen.sprite.rect.left
            self.coory =  self.imagen.sprite.rect.top

        if self.caminar== True and self.salto == False and self.correr == False:#           aceleracion |            disancia inicial | velocidad inicial
            t = self.cronometro.cronometroC()
            velocidad = 20
            self.Info[1] = velocidad

            if self.direccion == True:
                #self.imagen.sprite.rect.left = x
                self.angulo = 0
            else:
                #self.imagen.sprite.rect.left = self.coorx -(x-self.coorx)
                self.angulo = 180
                velocidad*=-1
            self.Info[2] = self.angulo

            x = mov_recUniforme(t, velocidad, self.coorx)#0.5* 20* self.tiempo*self.tiempo + self.coorx + 60*self.tiempo
            self.imagen.sprite.rect.left = x

    def reseteo(self):
        self.tiempo = 0
        self.cronometro.modPasivo()
        self.coorx =  self.imagen.sprite.rect.left
        self.coory =  self.imagen.sprite.rect.top

    def setSalto(self, salto):
        self.salto = salto
##        if salto:
##            self.imagen.sprite.rect.top-=1

    def getSalto(self):
        return self.salto

    def getCorrer(self):
        return self.correr

    def setCorrer(self, correr, dic = True):
        self.correr = correr
        self.direccion = dic

    def getCaminar(self):
        return self.caminar

    def setCaminar(self, caminar, dic = True):
        self.caminar = caminar
        self.direccion = dic

    def getDirec(self):
        return self.direccion

    def getActivo(self):
        if self.caminar == True or self.correr == True or self.salto == True:
            return True
        else:
            return False

    def coordenadas(self,(x,y) = (None,None)):
        if x != None:
            self.imagen.sprite.rect.left = x
            self.imagen.sprite.rect.top = y
        return (self.imagen.sprite.rect.left, self.imagen.sprite.rect.top)