import time

class Gif(object):
    def __init__(self):
        self.contador = 0
        self.diccionario = {}
        self.listaActual = []
        self.velocidad_tiempo = 100
        self.progreso_tiempo = self.velocidad_tiempo

        self.imagenACtual = None

    def iniciar(self):
        self.progreso_tiempo = int(round(time.time() * 1000)) + self.velocidad_tiempo

    def load(self, dicc, velocidad):
        self.diccionario = dicc
        self.velocidad_tiempo = velocidad

    def refrescar(self):
        tiempo  = int(round(time.time() * 1000))
        if tiempo >= self.progreso_tiempo:
            #print "what's up?", self.contador
            self.imagenACtual = self.listaActual[self.contador]
            self.progreso_tiempo+=self.velocidad_tiempo
            self.contador+=1

            if self.contador >= len(self.listaActual):
                self.contador = 0


class Animacion(object):

    def __init__(self):
        pass



def main():
    pass

if __name__ == '__main__':
    main()
