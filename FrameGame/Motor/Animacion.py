import time
import os
from pygame import image
from ..Admin.PreCompilacion import *
"""
    nose que onda esta animacion esta mala
"""
MSJERROR = "Error: esta clave no pertenece al diccionario :("

class AnimaPersonaje(object):
    def __init__(self):
        self.listkey=[]
        self.dicEventImag={}# key: tiempo, lista imagenes
        self.dicEventSong={}# key: song
        self.dicEventComp={}# key: comportamiento
        self.listImagAct = None
        self.velocidad = 0
        self.imagActual = None
        self.songActual = None
        self.compActual = None

        self.gif = Gif()
        self.gif.setAnimar(True)

    def setEventImag(self, key):
        try:
            self.velocidad, self.listImagAct = self.dicEventImag[key]
            self.gif.velocidad_tiempo = self.velocidad
            self.gif.listaActual = self.listImagAct
            self.imagActual = self.listImagAct[0]
        except KeyError:
            print MSJERROR

    def setEventSong(self, key):
        try:
            self.songActual = self.dicEventSong[key]
        except KeyError:
            print MSJERROR

    def setEventComp(self, key):
        try:
            self.compActual = self.dicEventComp[key]
        except KeyError:
            print MSJERROR

    def refrescar(self):
        self.gif.refrescar()
        if self.gif.procesado:
            self.imagActual = self.gif.getImagenActual()


def transformer(_file):#archivo_gif -> GIF -> AnimaPersonaje
    gif = Archivo_gif(_file)
    gif.abrir(_file)
    diccionario = gif.getAnimacion()

    animacion = AnimaPersonaje()
    animacion.dicEventImag = diccionario
    animacion.setEventImag("default")
    animacion.gif.iniciar()
    return animacion


class Gif(object):
    def __init__(self):
        print "DEMOSTRACION"
        self.contador = 0
        self.diccionario = {}
        self.listaActual = []
        self.velocidad_tiempo = 100
        self.progreso_tiempo = self.velocidad_tiempo
        self.animar1 = False
        self.imagenACtual = None

        self.procesado = False

    def setAnimar(self, valor):
        self.animar1 = valor

    def getAnimar(self):
        return self.animar1

    def getImagenActual(self):
        return self.imagenACtual

    def setListActual(self, lista):
        self.listaActual = lista

    def iniciar(self):
        self.progreso_tiempo = int(round(time.time() * 1000)) + self.velocidad_tiempo

    def load(self, dicc, velocidad):
        self.diccionario = dicc
        self.velocidad_tiempo = velocidad
        self.contador = 0

    def refrescar(self):
        if self.animar1 == True:
            tiempo  = int(round(time.time() * 1000))
            if tiempo >= self.progreso_tiempo:
                #print "what's up?", self.contador
                if self.contador < len(self.listaActual):
                    self.imagenACtual = self.listaActual[self.contador]
                    self.contador+=1
                    self.procesado = True
                else:
                    self.contador = 0
                self.progreso_tiempo+=self.velocidad_tiempo


                #if self.contador >= len(self.listaActual):
                #    self.contador = 0

    def listaEvento(self,lista, velo):
        self.listaActual = []
        for i in lista:
            self.listaActual.append(image.load(os.path.join(i[1],i[0])))
        if len(self.listaActual)>0:
            self.imagenACtual = self.listaActual[0]
            self.velocidad_tiempo = velo
        self.iniciar()
        self.animar = True
class Animacion(object):

    def __init__(self):
        pass



def main():
    #import pygame

    #pygame.init()
    #pantalla=pygame.display.set_mode((800,600))
    #pygame.FULLSCREEN

    image1 = image.load("mario.png").convert_alpha()

if __name__ == '__main__':
    main()
