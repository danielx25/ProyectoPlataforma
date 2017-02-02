from Personaje_ import Personaje
from Plataforma_ import Plataforma
def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):
    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        for objeto in lista_objetos:
            if isinstance(objeto, Personaje):
                """
                se necesita mas informacion para tomar una desicion para esto se necesita la informacion que probenga de deteccion 
                """
                personaje.setGananciaXY(objeto.getGananciaXY())
            if isinstance(objeto, Plataforma):
                personaje.setCaminar(False)
                personaje.setCorrer(False)
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