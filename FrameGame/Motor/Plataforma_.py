import uuid
from pygame import Rect

class Plataforma(object):
    def __init__(self):
        # identinficacion
        self.id = uuid.uuid1().hex

        self._x = 0
        self._y = 0
        self.x_antes = 0
        self.y_antes = 0

        self.ancho = 0
        self.largo = 0

        self.visible = True
        self.colisionable = True

        self.rectangulo = Rect(0,0,0,0)

        self.enviarGanancia_x = 0
        self.enviarGanancia_y = 0

    def setTamRect(self, ancho, largo):
        self.rectangulo.width = ancho
        self.rectangulo.height = largo
        self.ancho=ancho
        self.largo=largo

    def setPosRect(self, x, y):
        self.rectangulo.left = x
        self.rectangulo.top = y

    def estado(self):
        self.enviarGanancia_x = self._x - self.x_antes
        self.enviarGanancia_y = self._y - self.y_antes

    def getGananciaXY(self):
        return self.enviarGanancia_x, self.enviarGanancia_y

    def setXY(self, x, y):
        self._x = self.x_antes = x
        self._y = self.y_antes = y
        self.setPosRect(self._x,self._y)

    def getEjeX(self):
        return self._x

    def getEjeY(self):
        return self._y

    def getCoordenadas(self):
        return (self._x, self._y)

    def setVisible(self, valor):
        self.visible = valor

    def getVisible(self):
        return self.visible

    def setColision(self, valor):
        self.colisionable = valor

    def getColision(self):
        return self.colisionable