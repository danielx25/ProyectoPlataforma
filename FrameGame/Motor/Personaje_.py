
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
        self.id = uuid.uuid1().hex

        self._x = 0
        self._y = 0
        self.ancho = 0
        self.largo = 0

        self.x_inicial = 0
        self.y_inicial = 0

        self.x_antes = 0
        self.y_antes = 0

        self.sistema_cerradox = [0, 0]
        self.sistema_cerradoy = [0, 0]

        self.enviarGanancia_x = 0
        self.enviarGanancia_y = 0
        self.recibirGanancia_x = 0
        self.recibirGanancia_y = 0

        # estado del personaje
        self.saltar = False
        self.correr= False
        self.caminar = False

        #sentido
        self.sentido = False

        self.inerciaGanancia = False #la inercia es una fuerza que produce al principio pero queda actuando
        #por un tiempo indefinido, en este caso dice si al saltar se debe aplicar la ganacia de la plataforma desde donde salto
        self.activarGanancia = True

        self.protagonista = False
        self.iA = False
        self.agente = None

        #el personaje esta compuesto por cuatro rectangulos
        self.rectangulo = Rect(0,0,0,0)#cuerpo completo
        self.rec1 = Rect(0, 0, 0, 0)#bajo
        self.rec2 = Rect(0, 0, 0, 0)#izquierda
        self.rec3 = Rect(0, 0, 0, 0)#derecha
        self.rec4 = Rect(0, 0, 0, 0)#arriba

        self.ady_left = False
        self.ady_right = False
        self.ady_down = False
        self.ady_up = False

        self.tic = Tiempo()
        self.status={}
        self.status["angulo"] = 0
        self.status["velocidad"]=0
        self.status["velocidad x"] = 0
        self.status["velocidad y"] = 0
        self.status["gravedad"] = 9.8
        self.status["parabola"] = (90, 88)#velocidad inicial, angulo inicial
        self.status["caida"]=(270, 90)
        self.status["correr"] = (23, 1)#velocidad, aceleracion
        self.status["caminar"] = 30 #velocidad

    def runGanancia1(self):
        self.enviarGanancia_x = self._x - self.x_antes
        self.enviarGanancia_y = self._y - self.y_antes
        self._x += self.recibirGanancia_x
        self._y += self.recibirGanancia_y

    def runGanancia2(self):
        self._x += self.sistema_cerradox[1] - self.sistema_cerradox[0]
        self._y += self.sistema_cerradoy[1] - self.sistema_cerradoy[0]
        if self.activarGanancia:
            self._x += self.recibirGanancia_x
            self._y += self.recibirGanancia_y
        self.enviarGanancia_x = self._x - self.x_antes
        self.enviarGanancia_y = self._y - self.y_antes

        if self.inerciaGanancia:
            self.recibirGanancia_x = 0
            self.recibirGanancia_y = 0

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
        self.rectangulo.width, self.rectangulo.height = (rec_size[0], rec_size[1])
        self.rec1.width, self.rec1.height = (rec_size[0] / 2.0, rec_size[1] / 4.0)
        self.rec2.width, self.rec2.height = (rec_size[0] / 4.0, rec_size[1] / 2.0)
        self.rec3.width, self.rec3.height = (rec_size[0] / 4.0, rec_size[1] / 2.0)
        self.rec4.width, self.rec4.height = (rec_size[0] / 2.0, rec_size[1] / 4.0)

    def pos_rectangulos(self, coor, tam):
        x, y = coor
        ancho, largo = tam
        self.rectangulo.left, self.rectangulo.top = (x, y)
        (self.rec1.left, self.rec1.top) = (x + (ancho / 4.0),y + largo - self.rec1.height)  # + 3*(largo/4.0))#abajo
        (self.rec2.left, self.rec2.top) = (x, y + (largo / 4.0))
        (self.rec3.left, self.rec3.top) = (x + ancho - self.rec3.width,y + (largo / 4.0))
        (self.rec4.left, self.rec4.top) = (x + (ancho / 4.0), y)

    def actualizacionRec(self):
        self.pos_rectangulos((self._x, self._y),(self.ancho, self.largo))

    def setXY(self, x, y):
        self._x = self.x_antes = x
        self._y = self.y_antes = y
        self.actualizacionRec()

    def getXY(self):
        return (self._x, self._y)


    def saltando(self,):
        self.x_antes = self._x
        self.y_antes = self._y


        if self.saltar == False and self.correr == False and self.caminar == False:
            self.tic.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y

            self.sistema_cerradox[0] = self.sistema_cerradox[1]= 0
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1]= 0

        if self.saltar == True and self.correr == False and self.caminar == False:
            self.tiempo = self.tic.cronometroC()
            self.sistema_cerradox[0] = self.sistema_cerradox[1]
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1]
            velocidad_inicial = self.status["parabola"][0]
            angulo_disparo = self.status["parabola"][1]
            gravedad = self.status["gravedad"]
            tupla = mov_parabolico1(velocidad_inicial ,angulo_disparo, self.tiempo, gravedad)
            (x, y) = tupla
            self.sistema_cerradox[1] = x
            self.sistema_cerradoy[1] = y

            self.status["velocidad x"],self.status["velocidad y"]=velocidad_InstanteXY(velocidad_inicial,angulo_disparo,self.tiempo,gravedad)
            self.status["velocidad"]=velocidad_Instante(self.status["velocidad x"],self.status["velocidad y"])
            self.status["angulo"]=angulo_actual(self.status["velocidad x"],self.status["velocidad y"])
            self.record = self.tiempo

    def corriendo(self,):
        self.x_antes = self._x
        self.y_antes = self._y

        if self.saltar == False and self.correr == False and self.caminar == False:
            self.tic.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y

            self.sistema_cerradox[0] = self.sistema_cerradox[1] = 0
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1] = 0

        if self.correr == True and self.saltar == False and self.caminar == False:
            t = self.tic.cronometroC()

            self.sistema_cerradox[0] = self.sistema_cerradox[1]
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1]
            velocidad = self.status["correr"][0]
            aceleracion =self.status["correr"][1]

            if self.sentido == True:
                self.status["angulo"] = 0
            else:
                self.status["angulo"] = 180
                velocidad *= -1
                aceleracion *= -1

            vel_t = vel_movRecAcelerado(aceleracion,t, velocidad)
            self.status["velocidad"] = vel_t
            self.status["velocidad x"] = vel_t
            self.status["velocidad y"]  = 0
            x = mov_recAcelerado(t, aceleracion, velocidad)
            self.sistema_cerradox[1] = x

    def caminando(self,):
        self.x_antes = self._x
        self.y_antes = self._y

        if self.saltar == False and self.correr == False and self.caminar == False:
            self.tic.modPasivo()
            self.x_inicial = self._x
            self.y_inicial = self._y
            self.sistema_cerradox[0] = self.sistema_cerradox[1] = 0
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1] = 0

        if self.caminar == True and self.saltar == False and self.correr == False:  # aceleracion |            disancia inicial | velocidad inicial
            t = self.tic.cronometroC()
            self.sistema_cerradox[0] = self.sistema_cerradox[1]
            self.sistema_cerradoy[0] = self.sistema_cerradoy[1]

            velocidad = self.status["caminar"]
            self.status["velocidad"] = velocidad

            if self.sentido == True:
                self.angulo = 0
            else:
                self.angulo = 180
                velocidad *= -1
            self.status["angulo"] = self.angulo

            x = mov_recUniforme(t, velocidad)
            self.sistema_cerradox[1]=x

    def getEjeX(self):
        return self._x

    def getEjeY(self):
        return self._y

    def getCoordenadas(self):
        return (self._x, self._y)

    def setSalto(self, salto):
        self.saltar = salto
        self.status["angulo"] = self.status["parabola"][1]

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
        self.sistema_cerradox[0] = self.sistema_cerradox[1] = 0
        self.sistema_cerradoy[0] = self.sistema_cerradoy[1] = 0
        self.actualizacionRec()
        self.tic.modPasivo()
