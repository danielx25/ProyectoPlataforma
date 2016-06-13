from pygame import mixer


class entornoMusic(object):

    def __init__(self):

        mixer.init()
        self.musicaJuego = {}
        self.MxProtagonista = {}
        self.MxOtrosPersonajes = {}
        self.MxEnotorno = {}

    def playMixProtagonista(self,nombre):

        if self.MxProtagonista.has_key(nombre):
            sonido = self.MxProtagonista[nombre]
            sonido.play()
            return True
        return False

    def playMixOtroPersonaje(self,nombre):

        if self.MxOtrosPersonajes.has_key(nombre):
            sonido = self.MxOtrosPersonajes[nombre]
            sonido.play()
            return True
        return False

    def playMixEntorno(self,nombre):

        if self.MxEnotorno.has_key(nombre):
            sonido = self.MxEnotorno[nombre]
            sonido.play()
            return True
        return False

    def playMusica(self, nombre):
        if self.musicaJuego.has_key(nombre):
            sonido = self.musicaJuego[nombre]
            mixer.music.load(sonido)
            mixer.music.set_volume(0.05)
            mixer.music.play()
            return True
        return False



    def addMixProtagonista(self, clave, nombre):
        sonido = mixer.Sound(nombre)
        sonido.set_volume(0.3)
        self.MxProtagonista[clave] = sonido

    def addmusica(self, clave, nombre):
        self.musicaJuego[clave] = nombre



def main():
    musica = entornoMusic()
    musica.addMixProtagonista("golpe", "mariog.wav")
    musica.playMixProtagonista("golpe")
    #musica.addmusica("mus", "pixel.mp3")
    #musica.playMusica("mus")
    #sonido = mixer.Sound("mario.wav")
    #sonido.play()

if __name__ == '__main__':
    main()
