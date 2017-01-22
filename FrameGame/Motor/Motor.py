import Personaje
import Plataforma
import AdminRecursos
import Eventos
import DeteccionColisiones
import EjecucionActividades
import Camara

from pygame import Rect
import threading

class MotorVideojuego(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.salirJuego = False

        self.tablaImagenes = {}
        self.tablaSonidos = {}
        self.tablaMusica = {}
        self.tablaColisiones = {}

        self.diccionarioScripts = []

        self.universoPersonajes = {}
        self.universoPlataformas = []
        self.conjuntoPersonajes = []
        self.conjuntoPlataformas = []
        self.protagonista = None

        self.reloj = None
        self.tiempoLimite = 10 #10 minutos

        self.campoAccion = Rect(0, 0, 800, 600)
        self.eventosUsuario = None
        self.controlEventos = Eventos.Eventos_Protagonista()
        self.camara = Camara.Camara(self.campoAccion)

    def run(self):
        pass

    def cicloVideojuego(self):

        while self.reloj < self.tiempoLimite and self.salirJuego == False:
            AdminRecursos.AdministrarRecursosPersonaje(self.universoPersonajes)
            AdminRecursos.AdministrarRecursosPlataformas(self.universoPlataformas)
            self.controlEventos.eventos(self.eventosUsuario)
            self.controlEventos.comportamientoPRO(self.protagonista)
            DeteccionColisiones.deteccionColisiones(self.conjuntoPersonajes, self.conjuntoPlataformas, self.tablaColisiones)
            EjecucionActividades.ejecutarScripts(self.diccionarioScripts)#falta tabla de colisones, personajes etc
            EjecucionActividades.ejecutarPersonajes(self.conjuntoPersonajes)
            EjecucionActividades.ejecutarSonidos(self.tablaSonidos)#falta musica
            self.camara.centrado(self.conjuntoPersonajes, self.conjuntoPlataformas)


    def entradaPersonajes(self, personajes):
        self.universoPersonajes = personajes

    def entradaProtaganista(self, protagonista):
        self.protagonista = protagonista

    def entradaPlataformas(self, plataformas):
        self.universoPlataformas = plataformas

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