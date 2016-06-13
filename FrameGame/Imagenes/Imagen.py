"""
#Esta es una clase base que nos permitira manejar imagenes o una secuencia de
#imagenes para poder hacer efecto de movimiento (gif)

#Esta recibe tres parametros de los cuales dos son opcionales
#1.- es el nombre de la imagen
#2.- la direccion de la imagen (opcional)
#3.- si la imagen esta compuesta dentro de una coleccion (opcional)
"""

from pygame import image

class Imagen(object):
    def __init__(self,ruta, tostring = None):
        self.nombre = "default"
        self.ruta = ruta

        if tostring == None:
            print ruta
            self.T_imagen = image.load(self.ruta).convert_alpha()
        else:
            self.T_imagen = Tostada
        self.tam = self.T_imagen.get_rect()

