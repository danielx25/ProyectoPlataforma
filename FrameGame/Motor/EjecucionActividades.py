from Personaje_ import Personaje
from Plataforma_ import Plataforma
import time


def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):
    # adyacencia(personajes, tablaColisiones)
    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        xGanancia = 0
        yGanancia = 0
        ladoAbajo = False
        ladoIzquierdo = False
        ladoDerecho = False
        for objeto in lista_objetos:
            if isinstance(objeto[0], Personaje):
                pass
            if isinstance(objeto[0], Plataforma):  # traspasando la ganancia en caso de la plataforma
                plataforma = objeto[0]
                lado = objeto[1]
                if lado == 0:
                    ladoAbajo = True
                    xGanancia += plataforma.getGananciaXY()[0]
                    yGanancia += plataforma.getGananciaXY()[1]

                if lado == 1:  # izquierda
                    ladoIzquierdo = True
                    if plataforma.getGananciaXY()[0] > 0:
                        xGanancia += plataforma.getGananciaXY()[0]

                if lado == 3:  # derecha
                    ladoDerecho = True
                    if plataforma.getGananciaXY()[0] < 0:
                        xGanancia += plataforma.getGananciaXY()[0]

        if len(lista_objetos) > 0:
            personaje.setGananciaXY((xGanancia, yGanancia))

        if ladoAbajo == False:
            personaje.setCaminar(False)
            personaje.setCorrer(False)
        else:
            if personaje.getSalto():
                angulo = round(personaje.status["angulo"])

                if 180< angulo< 360 or -180< angulo< 0:
                    print angulo
                    personaje.setSalto(False)



        izquierdoAbajo = False
        derechaAbajo = False
        parte1 = False
        parte2 = False
"""
        if ladoIzquierdo == True and ladoAbajo == False:
            personaje.setCaminar(False)
            personaje.setCorrer(False)
            angulo = round(personaje.status["angulo"])
            if 90 < angulo < 270 or -270 < angulo < -90:
                personaje.setSalto(True)
                velo_y = personaje.status["velocidad y"]
                if velo_y > 0:
                    velo_y = 0
                else:
                    velo_y *= -1
                personaje.status["parabola"] = (velo_y, -90)
                personaje.setReset(True)

        if ladoDerecho == True and ladoAbajo == False:
            personaje.setCaminar(False)
            personaje.setCorrer(False)
            angulo = round(personaje.status["angulo"])
            parte1 = 0 <= angulo < 90 or -270 < angulo <= -360
            parte2 = 270 < angulo <= 360 or -90 < angulo <= 0
            if parte1 or parte2:
                personaje.setSalto(True)
                velo_y = personaje.status["velocidad y"]
                if velo_y > 0:
                    velo_y = 0
                else:
                    velo_y *= -1
                personaje.status["parabola"] = (velo_y, 270)
                personaje.setReset(True)

        if ladoIzquierdo == True and ladoAbajo == True:
            if personaje.getSentido() == False:
                personaje.setCaminar(False)

            if personaje.getSalto():
                angulo = round(personaje.status["angulo"])
                if 90 < angulo < 180 or -180 < angulo < -90:
                    personaje.setSalto(False)

        if ladoDerecho == True and ladoAbajo == True:
            if personaje.getSentido() == True:
                personaje.setCaminar(False)

            if personaje.getSalto():
                angulo = round(personaje.status["angulo"])
                parte1 = 0 <= angulo < 90 or -270 < angulo <= -360
                parte2 = 270 < angulo <= 360 or -90 < angulo <= 0
                if parte1 or parte2:
                    personaje.setSalto(False)
"""

def adyacencia(personajes, tablaColisiones):
    for personaje in personajes:
        personaje.ady_down = recursion(personaje, tablaColisiones, 0)
        personaje.ady_left = recursion(personaje, tablaColisiones, 1)
        personaje.ady_up = recursion(personaje, tablaColisiones, 2)
        personaje.ady_right = recursion(personaje, tablaColisiones, 3)


def recursion(personaje, tablaColisiones, lado):
    lista_objetos = tablaColisiones[personaje.id]
    for objeto in lista_objetos:
        if objeto[1] == lado:
            # print str(personaje.id)
            # print len(lista_objetos), " ============== ", objeto[1]
            if isinstance(objeto[0], Plataforma):
                return True
            else:
                return recursion(objeto[0], tablaColisiones, lado)
    return False


def ejecutarScripts(diccionarioScripts, diccionarioPersonajes, diccionarioPlataformas):
    for clave, funciones in diccionarioScripts.items():
        for funcion in funciones:
            if diccionarioPersonajes.has_key(clave):
                personaje = diccionarioPersonajes[clave]
                funcion(personaje)
            if diccionarioPlataformas.has_key(clave):
                plataforma = diccionarioPlataformas[clave]
                funcion(plataforma)


def ejecutarActividadesPlataformas(conjuntoPlataformas):
    for p in conjuntoPlataformas:
        p.estado()
        p.actualizacionRec()


def ejecutarActividadesPersonajes(conjuntoPersonajes):
    for p in conjuntoPersonajes:
        p.reseteo()
        p.saltando()
        p.corriendo()
        p.caminando()
        p.runGanancia2()
        p.actualizacionRec()


def ejecutarSonidos(tablaSonidos):
    pass