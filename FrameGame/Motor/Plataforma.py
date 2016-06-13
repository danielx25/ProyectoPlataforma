import sys
import os
#sys.path.append("..")

from ..Imagenes.Sprites import *
from pygame import Rect
from ..path import leer_Entorno



TAM = 2

class rectangulos(object):# clase rectangulo con atributos

    def __init__(self,name1 = "", link1 = "", coor = None, list1 = None, lis2 = None):
        #Sprites.__init__(self,name1,link1)
        self.imagen = Sprites(os.path.join(link1))
        (self.imagen.sprite.rect.left,self.imagen.sprite.rect.top) = coor#coordenadas iniciales
        self.afuera = (list1[0], list1[1], list1[2], list1[3])#atributos tupla
        self.adentro = (lis2[0], lis2[1], lis2[2], lis2[3])#atributos tupla
        self.lados = [None, None, None, None]
        self.estatico = True
        self.inicLados()

        self.compActual = None
        self.compEstatico = None
        self.compDinaminco = None

        self.list_comp = [False, True, False, False]
        self.comportamiento = None #   funcion de comportamiento
        self.pasivaComp = False #

    def estado(self):
        if self.pasivaComp:
            self.comportamiento(self)

    def pos_rectangulos(self):
        pass

    def imprimir(self, pantalla):
        if self.canFprint == True:
            pantalla.blit(self.imagen.sprite.image, self.imagen.sprite.rect)
            self.canFprint  = False


    def inicLados(self):
        dis = 2
        x , y = self.imagen.sprite.rect.left, self.imagen.sprite.rect.top
        if self.afuera[0] == True:#izquierda
            self.lados[0] = Rect(x, y+dis, TAM, self.imagen.sprite.rect.size[1]-dis*2)

        if self.afuera[1] == True:#abajo
            self.lados[1] = Rect(x+dis, y+self.imagen.sprite.rect.size[1], self.imagen.sprite.rect.size[0]-dis*2, TAM)

        if self.afuera[2] == True:#derecha
            self.lados[2] = Rect(x+self.imagen.sprite.rect.size[0], y+dis, TAM, self.imagen.sprite.rect.size[1]-dis*2)

        if self.afuera[3] == True:#arriba
            self.lados[3] = Rect(x+dis, y, self.imagen.sprite.rect.size[0]-dis*2, TAM)

def carga_rectangulos(NArchivo):#devuelve lista rectangulo y sus atributos

    lista = []
    lista_archivo = []
    lista_archivo = leer_Entorno(NArchivo)

    for x in lista_archivo:
       lista.append(rectangulos(x[0], x[1], x[2], x[3], x[4]))
    return lista

