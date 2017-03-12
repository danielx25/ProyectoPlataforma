from Personaje_ import Personaje
from Plataforma_ import Plataforma
import time

def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):
    #adyacencia(personajes, tablaColisiones)
    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        xGanancia = 0
        yGanancia = 0
        for objeto in lista_objetos:
            if isinstance(objeto[0], Personaje):
                pass
            if isinstance(objeto[0], Plataforma):
                plataforma = objeto[0]
                lado = objeto[1]
                if lado == 0:
                    xGanancia+= plataforma.getGananciaXY()[0]
                    yGanancia += plataforma.getGananciaXY()[1]
        if len(lista_objetos) > 0:
            personaje.setGananciaXY((xGanancia, yGanancia))
        #    print "PRIMERO"
        #else:
        #    print "SEGUNDO: ",personaje.recibirGanancia_x, personaje.recibirGanancia_y
        """
        if personaje.ady_left == True or personaje.ady_right == True:
            personaje.setCaminar(False)
            personaje.setCorrer(False)
        if personaje.ady_down == True or personaje.ady_up == True:
            if 180<personaje.status["angulo"]<360 or -180<personaje.status["angulo"]<0:
                personaje.setSalto(False)
        """



def adyacencia(personajes, tablaColisiones):
    for personaje in personajes:
        personaje.ady_down = recursion(personaje, tablaColisiones, 0)
        personaje.ady_left = recursion(personaje, tablaColisiones,1)
        personaje.ady_up = recursion(personaje, tablaColisiones,2)
        personaje.ady_right = recursion(personaje, tablaColisiones,3)


def recursion(personaje, tablaColisiones, lado):
    lista_objetos = tablaColisiones[personaje.id]
    for objeto in lista_objetos:
        if objeto[1] == lado:
            #print str(personaje.id)
            #print len(lista_objetos), " ============== ", objeto[1]
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
        p.saltando()
        p.corriendo()
        p.caminando()
        p.runGanancia2()
        p.actualizacionRec()

def ejecutarSonidos(tablaSonidos):
    pass