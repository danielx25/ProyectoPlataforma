"""
#Esta clase maneja muchos atributos que importan lo que son los juegos
#y que no tiene la clase imagen. La clase sprite hereda de la sprites para poder manejar imagenes
#Los metodos propios de la clase sprite son:

#Coordenadas(): recibe las coordenadas donde tiene que ubicarse sino recibe nada retorna
#Las coordenadas actuales del sprite

#Imprimir(): recibe la pantalla para poder ser imprimido el sprite
#y los atributos que son propios de los sprites

#top, left, bottom, right
#topleft, bottomleft, topright, bottomright
#midtop, midleft, midbottom, midright
#center, centerx, center
#size, width, height
"""

from Imagen import Imagen
from pygame.sprite import Sprite

class Sprites(Imagen):
    def __init__(self,ruta , tostring = None):
        Imagen.__init__(self,ruta,tostring)
        self.nombre = "default"
        self.ruta = ruta
        self.sprite = Sprite()
        self.sprite.image = self.T_imagen
        self.sprite.rect = self.tam #tamano sprite
        self.sprite.rect.left = self.sprite.rect.top = 0
        self.canFprint = True

    def coordenadas(self,(x,y) = (None,None)):
        if x != None:
            self.sprite.rect.left = x
            self.sprite.rect.top = y
        return (self.sprite.rect.left, self.sprite.rect.top)


    def imprimir(self, pantalla):
        if self.canFprint == True:
            pantalla.blit(self.sprite.image, self.sprite.rect)

    def __str__(self):
        mensaje = "nombre: "+self.nombre+"\nruta: "+self.ruta+"\ntamanio: "+str (self.tam)
        return mensaje
