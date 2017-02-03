from Personaje_ import Personaje
from Plataforma_ import Plataforma

def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):
    #adyacencia(personajes, tablaColisiones)
    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        for objeto in lista_objetos:
            if isinstance(objeto[0], Personaje):
                """
                se necesita mas informacion para tomar una desicion para esto se necesita la informacion que probenga de deteccion
                """
                #personaje.setGananciaXY(objeto.getGananciaXY())
                pass
            if isinstance(objeto[0], Plataforma):
                if personaje.ady_left == True or personaje.ady_right == True:
                    personaje.setCaminar(False)
                    personaje.setCorrer(False)
                if personaje.ady_down == True or personaje.ady_up == True:
                    personaje.setSalto(False)

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
            if isinstance(objeto[0], Plataforma):
                return True
            else:
                return recursion(objeto[0], tablaColisiones, lado)
    return False

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