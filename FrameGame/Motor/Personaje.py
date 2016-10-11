
import uuid
from pygame import Rect
from tiempo import Tiempo
from Fisica import *

"""
Los personajes seran los que podran interactuar con el entorno teniedo como base
ciertos atributos como salto, caminar y correr
"""


class Personaje(object):

    def __init__(self):

        #identinficacion
        self.id = uuid.uuid1()

        self._x = 0
        self._y = 0
        self.ancho = 0
        self.largo = 0

        self.x_inicial = 0
        self.y_inicial = 0

        self.x_antes = 0
        self.y_antes = 0

        self.enviarGanancia_x = 0
        self.enviarGanancia_y = 0
        self.recibirGanancia_x = 0
        self.recibirGanancia_y = 0

        # estado del personaje
        self.saltar = False
        self.correr= False
        self.caminar = False

        #sentido
        self.sentido = 0

        self.protagonista = False
        self.iA = False
        self.agente = None

        #el personaje esta compuesto por cuatro rectangulos
        self.rec1 = Rect(0, 0, 0, 0)#bajo
        self.rec2 = Rect(0, 0, 0, 0)#izquierda
        self.rec3 = Rect(0, 0, 0, 0)#derecha
        self.rec4 = Rect(0, 0, 0, 0)#arriba

        self.tic = Tiempo()
        self.status={}
        self.status["angulo"] = 0
        self.status["velocidad"]=0
        self.status["velocidad x"] = 0
        self.status["velocidad y"] = 0
        self.status["gravedad"] = 9.8
        self.status["parabola"] = (90, 75)#velocidad inicial, angulo inicial
        self.status["caida"]=(270, 90)
        self.status["coor antes"] = (0,0)

    def runGanancia1(self):
        self.enviarGanancia_x = self._x - self.x_antes
        self.enviarGanancia_y = self._y - self.y_antes


    def runGanancia2(self):
        self._x+=self.recibirGanancia_x
        self._y+=self.recibirGanancia_y


    def getDiferenciaXY(self):
        x = self._x - self.x_antes
        y = self._y - self.y_antes
        return x,y


    def setGananciaXY(self, g):
        self.recibirGanancia_x=g[0]
        self.recibirGanancia_y=g[1]

    def getGananciaXY(self):
        return self.enviarGanancia_x, self.enviarGanancia_y
    
    def getStatus(self, valor):
        return self.status[valor]

    def tam_rectangulos(self, rec_size):
        self.ancho, self.largo=rec_size
        self.rec1.width, self.rec1.height = (rec_size[0] / 2.0, rec_size[1] / 4.0)
        self.rec2.width, self.rec2.height = (rec_size[0] / 4.0, rec_size[1] / 2.0)
        self.rec3.width, self.rec3.height = (rec_size[0] / 4.0, rec_size[1] / 2.0)
        self.rec4.width, self.rec4.height = (rec_size[0] / 2.0, rec_size[1] / 4.0)

    def pos_rectangulos(self, coor, tam):
        x, y = coor
        ancho, alto = tam
        (self.rec1.left, self.rec1.top) = (x + (ancho / 4.0),y + alto - self.rec1.height)  # + 3*(alto/4.0))#abajo
        (self.rec2.left, self.rec2.top) = (x, y + (alto / 4.0))
        (self.rec3.left, self.rec3.top) = (x + ancho - self.rec3.width,y + (alto / 4.0))
        (self.rec4.left, self.rec4.top) = (x + (ancho / 4.0), y)

    def actualizacionRec(self):
        self.pos_rectangulos((self._x, self._y),(self.ancho, self.largo))

    def saltando(self,):
        self.x_antes = self._x
        self.y_antes = self._y

        if self.saltar == False and self.correr == False and self.caminar == False:
            self.tic.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y

        if self.saltar == True and self.correr == False and self.caminar == False:
            self.tiempo = self.tic.cronometroC()  # self.tiempo + self.condicion[0]

            velocidad_inicial = self.status["parabola"][0]
            angulo_disparo = self.status["parabola"][1]
            gravedad = self.status["gravedad"]
            tupla = mov_parabolico1(velocidad_inicial, self.y_inicial,angulo_disparo, self.tiempo, gravedad)
            (h, self._y) = tupla
            self._x = self.x_inicial + h
            self.status["velocidad x"],self.status["velocidad y"]=velocidad_InstanteXY(velocidad_inicial,angulo_disparo,self.tiempo,gravedad)
            self.status["velocidad"]=velocidad_Instante(self.status["velocidad x"],self.status["velocidad y"])
            self.status["angulo"]=angulo_actual(self.status["velocidad x"],self.status["velocidad y"])
            self.record = self.tiempo

    def corriendo(self,):
        if self.saltar == False and self.correr == False and self.caminar == False:
            self.cronometro.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y

        if self.correr == True and self.saltar == False and self.caminar == False:  # aceleracion |            disancia inicial | velocidad inicial
            t = self.cronometro.cronometroC()

            velocidad = 20
            aceleracion = 6

            if self.direccion == True:
                # self._x = x
                self.angulo = 0
            else:
                # self._x = self.x_inicial -(x-self.x_inicial)
                self.angulo = 180
                velocidad *= -1
                aceleracion *= -1

            vel_t = aceleracion * t + velocidad
            self.Info[1] = vel_t
            self.Info[2] = self.angulo
            x = mov_recAcelerado(t, aceleracion, velocidad,
                                 self.x_inicial)  # mov_recUniforme(t, 20, self.x_inicial)#0.5* 20* self.tiempo*self.tiempo + self.x_inicial + 60*self.tiempo
            self._x = x
    def caminando(self,):
        if self.saltar == False and self.correr == False and self.caminar == False:
            self.cronometro.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y

        if self.caminar == True and self.saltar == False and self.correr == False:  # aceleracion |            disancia inicial | velocidad inicial
            t = self.cronometro.cronometroC()
            velocidad = 20
            self.Info[1] = velocidad

            if self.direccion == True:
                # self._x = x
                self.angulo = 0
            else:
                # self._x = self.x_inicial -(x-self.x_inicial)
                self.angulo = 180
                velocidad *= -1
            self.Info[2] = self.angulo

            x = mov_recUniforme(t, velocidad,self.x_inicial)  # 0.5* 20* self.tiempo*self.tiempo + self.x_inicial + 60*self.tiempo
            self._x = x

    def getEjeX(self):
        return self._x

    def getEjeY(self):
        return self._y

    def getCoordenadas(self):
        return (self._x, self._y)

    def setSalto(self, salto):
        self.saltar = salto

    def getSalto(self):
        return self.saltar

    def getCorrer(self):
        return self.correr

    def setCorrer(self, correr, dic = True):
        self.correr = correr
        self.sentido = dic

    def getCaminar(self):
        return self.caminar

    def setCaminar(self, caminar, dic = True):
        self.caminar = caminar
        self.sentido = dic

    def getSentido(self):
        return self.sentido

    def getStatus(self, status):
        return self.status[status]

    def reseteo(self):
        self.tiempo=0
        self.x_inicial=self._x
        self.y_inicial=self._y
        self.tic.modPasivo()
