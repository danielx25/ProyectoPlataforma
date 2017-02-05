from Personaje_ import Personaje
from Plataforma_ import Plataforma


def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):

    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        for objeto in lista_objetos:
            if isinstance(objeto[0], Personaje):
                personaje.setSalto(False)
                personaje.setCaminar(False)
                personaje.setCorrer(False)
            if isinstance(objeto[0], Plataforma):
                if personaje.ady_left == True and personaje.getSentido() == False:
                    personaje.setCaminar(False)
                    personaje.setCorrer(False)
                if personaje.ady_right == True and personaje.getSentido() == True:
                    personaje.setCaminar(False)
                    personaje.setCorrer(False)
                if personaje.ady_down == True or personaje.ady_up == True:
                    if 180<personaje.status["angulo"]<360 or -180<personaje.status["angulo"]<0:
                        personaje.setSalto(False)



def ejecutarScripts(diccionarioScripts):
    pass

def ejecutarActividadesPersonajes(conjuntoPersonajes):
    for p in conjuntoPersonajes:
        p.saltando()
        p.corriendo()
        p.caminando()
        p.runGanancia2()
        p.actualizacionRec()

def ejecutarSonidos(tablaSonidos):
    pass