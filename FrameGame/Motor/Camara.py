from tiempo import Tiempo
from ..Interfaz.Fisica import*

MOVAUTONOMO = "autonomo"
MOVAUTONOMO_DERECHA = "derecha"
MOVAUTONOMO_IZQ = "izquierda"
MOVAUTONOMO_ARRIBA = "arriba"
MOVAUTONOMO_ABAJO = "abajo"
MOVAUTONOMO_ACELERADO = "acelerado"
MOVAUTONOMO_CONSTANTE = "constante"


MOVPERSONAJE = "personaje"
MOVPERSONAJE_CENTRADO = "centrado"
MOVPERSONAJE_BORDES = "bordes"


class Camara (object):
    def __init__(self,campoAccion, dimen = 3):
        self.monito = None
        self.campoAccion=campoAccion
        self.horizontal = 0
        self.vertical = 0
        self.moverse = False #actividad de la ventana
        self.tiempo = Tiempo()

        #------------estilo
        self.estilo = MOVAUTONOMO
        #------------autonomo
        self.tipoMOVAUT = MOVAUTONOMO_CONSTANTE
        self.velocidad = 10
        self.aceleracion = 2
        self.direccion = MOVAUTONOMO_DERECHA
        #------------personaje
        self.tipoMOVPER = MOVPERSONAJE_CENTRADO
        self.enfocar_personaje = False
        self.fueraRango = False

        self.angulo = 0
        self.altura = 0
        self.eje_x = 0
        self.eje_y = 0

        if dimen == 1:
            self.arriba = 50
            self.abajo = 565
            self.derecha = 790
            self.izquierda = 10
        if dimen == 2:
            self.arriba = 10
            self.abajo = 590
            self.derecha =  750
            self.izquierda =  50
        if dimen == 3:
            self.arriba = 150
            self.abajo = 450
            self.derecha = 580
            self.izquierda = 220

    def setMov(self, mov):
        self.moverse = mov

    def getMov(self):
        return self.moverse

    def setEstilo(self, estilo):
        self.estilo = estilo

    def setMovAutonomo(self, direccion, tipoMOV, velocidad = 20, aceleracion = 2):
        self.direccion = direccion
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.tipoMOVAUT = tipoMOV

    def setMovPersonaje(self, tipoMov):
        self.tipoMOVPER = tipoMov

    def setPersonaje(self, personaje):
        self.enfocar_personaje = True
        self.monito = personaje
        self.tipoMOVPER = MOVPERSONAJE_CENTRADO


    def centrado(self, personajes, entornos):
        self.campoAccion.left = personajes.x*-1
        if self.moverse == False:
            self.tiempo.modPasivo()
            self.horizontal = personajes.x
            self.vertical = personajes.y
        else:
            if self.estilo == MOVAUTONOMO:
                t = self.tiempo.cronometroC()

                if self.tipoMOVAUT == MOVAUTONOMO_ACELERADO:
                    if self.direccion == MOVAUTONOMO_DERECHA:
                        ejex =mov_recAcelerado(t, self.aceleracion, self.velocidad, self.horizontal)
                        personajes.x = ejex
                        entornos.x= ejex
                    elif self.direccion == MOVAUTONOMO_IZQ:
                        ejex =mov_recAcelerado(t, self.aceleracion*-1, self.velocidad*-1, self.horizontal)
                        personajes.x = ejex
                        entornos.x= ejex
                    elif self.direccion == MOVAUTONOMO_ABAJO:
                        pass#construccion
                    elif self.direccion == MOVAUTONOMO_ARRIBA:
                        pass


                elif self.tipoMOVAUT == MOVAUTONOMO_CONSTANTE:

                    if self.direccion == MOVAUTONOMO_DERECHA:
                        ejex = mov_recUniforme(t, self.velocidad, self.horizontal)
                        personajes.x = ejex
                        entornos.x= ejex

                    elif self.direccion == MOVAUTONOMO_IZQ:
                        ejex = mov_recUniforme(t, self.velocidad*-1, self.horizontal)
                        personajes.x = ejex
                        entornos.x= ejex

            elif self.estilo == MOVPERSONAJE:
                if self.tipoMOVPER == MOVPERSONAJE_CENTRADO:
                    coorx, coory = self.monito.coordenadas()
                    tamx, tamy = self.monito.imagen.tam.size


                    if self.enfocar_personaje == True:
                        self.enfocar_personaje = False
                        self.fueraRango = True
                        #self.altura = coory + personajes.y
                        self.eje_x = coorx
                        self.eje_y = coory
                        self.tiempo.modPasivo()
                        self.horizontal = personajes.x
                        self.vertical = personajes.y

                        origen = (coorx+self.horizontal, coory+self.vertical)
                        destino = (400-tamx,300-tamy)
                        self.angulo = instanAng2(origen,destino)

                        print self.altura
                        print "ORIGEN : "+str(origen)
                        print "DESTINO: "+str(destino)
                        print "ANGULO : "+str(self.angulo)


                    if self.fueraRango == True:
                        t = self.tiempo.cronometroC()
                        ejex ,ejey = mov_parabolico(None, 30,0,self.angulo*-1,t, 0)#V_inicial,altura, angulo, tiempo, gravedad)
                        #print ejex, ejey

                        limitx = ejex+self.eje_x+tamx+self.horizontal
                        limity = ejey+self.eje_y+tamy+self.vertical

                        if 395<limitx<405 and 295 <limity<305:
                            self.fueraRango = False
                            self.tipoMOVPER = MOVPERSONAJE_BORDES

                        personajes.x= ejex+self.horizontal
                        #personajes.y= ejey+self.vertical

                        entornos.x =self.horizontal + ejex
                        #entornos.y = self.vertical +ejey
                        #print personajes.x, personajes.y

                elif self.tipoMOVPER == MOVPERSONAJE_BORDES:
                    coorx, coory = self.monito.coordenadas()
                    tamx, tamy = self.monito.imagen.tam.size

                    if self.enfocar_personaje == False:
                        self.enfocar_personaje = True
                        self.eje_x = coorx
                        self.eje_y = coory
                    else:
                        if self.eje_x != coorx:
                            personajes.x-= coorx -self.eje_x
                            entornos.x-=coorx -self.eje_x
                            self.eje_x = coorx



def lados_del_rectangulo(tam, lados, x, y):

    dis = 5
    if lados[0] != None:
        lados[0].move_ip(x, y+dis)

    if lados[1] != None:
        lados[1].move_ip(x+dis, y+tam[1])

    if lados[2] != None:
        lados[2].move_ip(x+tam[0], y+dis)

    if lados[3] != None:
        lados[3].top,lados[3].left = x+dis, y#lados[3].move_ip(x+dis, y)

    return lados