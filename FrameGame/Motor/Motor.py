import Personaje_
import Plataforma_
import AdminRecursos
import Eventos
import DeteccionColisiones
import EjecucionActividades
import Camara

from pygame import Rect
from pygame import time
import threading

class MotorVideojuego(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.salirJuego = False

        self.tablaImagenes = {}
        self.tablaSonidos = {}
        self.tablaMusica = {}
        self.tablaColisiones = {}#id personaje:[]

        self.diccionarioScripts = {}

        self.universoPersonajes = {}
        self.universoPlataformas = {}
        self.conjuntoPersonajes = []
        self.conjuntoPlataformas = []
        self.protagonista = None

        self.reloj = None
        self.tiempoLimite = 30000 #en milisegundos

        self.campoAccion = Rect(0, 0, 800, 600)
        self.eventosUsuario = []
        self.controlEventos = Eventos.Eventos_Protagonista()
        self.camara = Camara.Camara(self.campoAccion)
        self.gestionColisiones = DeteccionColisiones.GestionDeteccionColisiones(self.tablaColisiones)

    def run(self):
        self.protagonista = self.conjuntoPersonajes[0]
        self.cicloVideojuego()

    def cicloVideojuego(self):

        while self.reloj < self.tiempoLimite and self.salirJuego == False:
            AdminRecursos.AdministrarRecursosPersonaje(self.universoPersonajes)
            AdminRecursos.AdministrarRecursosPlataformas(self.universoPlataformas)
            #self.controlEventos.eventos(self.eventosUsuario)
            self.controlEventos.comportamientoPRO(self.protagonista)
            #DeteccionColisiones.deteccionColisiones(self.conjuntoPersonajes, self.conjuntoPlataformas, self.tablaColisiones)
            self.gestionColisiones.deteccionColisiones(self.conjuntoPersonajes, self.conjuntoPlataformas, self.tablaColisiones)
            #EjecucionActividades.ejecutarAccionesColisionesDetectadas(self.conjuntoPersonajes, self.tablaColisiones)
            EjecucionActividades.ejecutarScripts(self.diccionarioScripts, self.universoPersonajes, self.universoPlataformas)#falta tabla de colisones, personajes etc
            EjecucionActividades.ejecutarActividadesPlataformas(self.conjuntoPlataformas)
            EjecucionActividades.ejecutarActividadesPersonajes(self.conjuntoPersonajes)
            ##EjecucionActividades.ejecutarSonidos(self.tablaSonidos)#falta musica
            #self.camara.centrado(self.conjuntoPersonajes, self.conjuntoPlataformas)
            self.reloj = time.get_ticks()

            for i in self.conjuntoPersonajes:
                if i.ady_left:
                    #print "ady_left"
                    pass
            #print "reloj: ",self.reloj
        print "termino"

    def procesoVideoJuego(self):

        if self.reloj < self.tiempoLimite and self.salirJuego == False:
            AdminRecursos.AdministrarRecursosPersonaje(self.universoPersonajes)
            AdminRecursos.AdministrarRecursosPlataformas(self.universoPlataformas)
            # self.controlEventos.eventos(self.eventosUsuario)
            self.controlEventos.comportamientoPRO(self.protagonista)
            # DeteccionColisiones.deteccionColisiones(self.conjuntoPersonajes, self.conjuntoPlataformas, self.tablaColisiones)
            # EjecucionActividades.ejecutarAccionesColisionesDetectadas(self.conjuntoPersonajes, self.tablaColisiones)
            self.gestionColisiones.deteccionColisiones(self.conjuntoPersonajes, self.conjuntoPlataformas,
                                                       self.tablaColisiones)
            EjecucionActividades.ejecutarScripts(self.diccionarioScripts, self.universoPersonajes,
                                                 self.universoPlataformas)  # falta tabla de colisones, personajes etc
            EjecucionActividades.ejecutarActividadesPlataformas(self.conjuntoPlataformas)


            EjecucionActividades.ejecutarActividadesPersonajes(self.conjuntoPersonajes)
            ##EjecucionActividades.ejecutarSonidos(self.tablaSonidos)#falta musica
            # self.camara.centrado(self.conjuntoPersonajes, self.conjuntoPlataformas)
            self.reloj = time.get_ticks()


    def entradaPersonajes(self, personajes):
        for p in personajes:
            self.tablaColisiones[p.id] = []
            self.universoPersonajes[p.id] = p

    def entradaProtaganista(self, protagonista):
        self.protagonista = protagonista

    def entradaPlataformas(self, plataformas):
        for p in plataformas:
            self.universoPlataformas[p.id] = p
            self.diccionarioScripts[p.id] = []
        #self.universoPlataformas = plataformas

    def entradaImagenes(self, imagenes):
        self.tablaImagenes = imagenes

    def entradaSonidos(self, sonidos):
        self.tablaSonidos = sonidos

    def entradaMusica(self, musica):
        self.tablaMusica = musica

    def entradaTiempo(self, tiempo):
        self.tiempoLimite = tiempo

    def entradaEventosUsuario(self, eventos):
        self.eventosUsuario = eventos