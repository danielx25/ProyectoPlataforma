import uuid


class plataforma(object):
    def __init__(self):
        # identinficacion
        self.id = uuid.uuid1()

        self._x = 0
        self._y = 0
        self.ancho = 0
        self.largo = 0

        self.visible = True
        self.colisionable = True

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