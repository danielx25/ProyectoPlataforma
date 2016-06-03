
import uuid

"""
Los personajes seran los que podran interactuar con el entorno teniedo como base
ciertos atributos como salto, caminar y correr
"""


class Personaje(Object):

    def __init__(self):

        #identinficacion
        self.id = uuid.uuid1()

        self._x = 0
        self._y = 0
        self.ancho = 0
        self.largo = 0

        # estado del personaje
        self.saltar = False
        self.correr= False
        self.caminar = False

        #sentido
        self.sentido = 0



    def saltando(self,):
        if self.salto == False and self.correr== False and self.caminar== False:
            pass

        if self.salto == True and self.correr == False  and self.caminar == False:
            pass

    def corriendo(self,):
        pass

    def caminando(self,):
        pass

    def getEjeX(self):
        return self._x

    def getEjeY(self):
        return self._y

    def getCoordenadas(self):
        return (self._x, self._y)

    def setSalto(self, salto):
        self.salto = salto

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
