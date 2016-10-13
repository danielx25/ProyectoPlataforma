import math

def radianes(x): # convierte angulo a radianes
    x = math.radians(x)
    return x


#tan a = Vy/Vx = (vo.sen a ?g.t)/ (vo.cos a)= vo.sen a / (vo.cos a) - g.t /(vo.cos a) = tan a   - g.t /(vo.cos a)



def mov_parabolico(Info, V_inicial,altura, angulo, tiempo, gravedad):#Esto indica la trayectoria parabolica del objeto
    x = V_inicial* math.cos(radianes(angulo))*tiempo*1.0
    y = altura + V_inicial * math.sin(radianes(angulo)) * tiempo - 0.5 * gravedad* tiempo*tiempo
    if Info != None:
        Info[3] = (Vx, Vy) = (V_inicial*math.cos(radianes(angulo)), V_inicial*math.sin(radianes(angulo))-gravedad*tiempo)#velocidades
        Info[2] = math.sqrt(math.pow(Vx,2)+math.pow(Vy,2))#velocidad en cada instante

        angulo = math.atan2(Vy, Vx)#+0.5*math.pi
        #print "Vx: "+str(Vx)+" Vy: "+str(Vy)+" Velocidad: "+str(Info[2])+"   angulo: "+str(math.degrees(angulo))

        if len(Info[0]) == 0:#si no hay ninguna coordenada
            Info[0] = [None, (x,y)]
        else:
            aux = Info[0][1]#coordenada anterior
            Info[0]= [aux, (x, y)]#tenemos de coor la auntigua y la nueva
            #las coordenadas entregadas en este info no sirven mucho, si no tienen una verdadera conversion de datos porque primero el ejey se invierte los polos
            #para que se vea efectos bien de los movieminetos de la parabola y el ejex se configura fuera de este metodo
            if Info[0][0] != Info[0][1]:
                Info[1]= instanAng(Info[0][0],Info[0][1])#angulo de inclinacion la se encuentra
                #print "angulo rec  : "+str(Info[1])
                #print "angulo Vy/Vx: "+str(math.degrees(Vx/Vy))

def mov_parabolico1(V_inicial, angulo, tiempo, gravedad):
    x = V_inicial * math.cos(radianes(angulo)) * tiempo * 1.0
    y = V_inicial * math.sin(radianes(angulo)) * tiempo - 0.5 * gravedad * tiempo * tiempo
    y = -y
    return x,y

def max_altura(velo, angulo, gravedad):
    lm = math.pow(velo, 2) * math.pow(math.sin(radianes(angulo)), 2)
    return (lm) / (2 * gravedad)

def velocidad_InstanteXY(V_inicial, angulo, tiempo, gravedad):
    return (V_inicial*math.cos(radianes(angulo)), V_inicial*math.sin(radianes(angulo))-gravedad*tiempo)

def velocidad_Instante(Vx ,Vy):
    return math.sqrt(math.pow(Vx,2)+math.pow(Vy,2))

def angulo_actual(Vx ,Vy):
    return math.atan2(Vy, Vx)* (180.0 / math.pi)



##    if Info[1] != None and Info[1] != 270.0:
##        print Info[1]

    y = altura - (y - altura)#por coordenadas y
    return (x,y)

def mov_recAcelerado(tiempo, aceler_, veloci_inic):
    x = 0.5*aceler_*tiempo**2 +veloci_inic*tiempo
    return x

def vel_movRecAcelerado(aceleracion, t, velocidad_inicial):
    return aceleracion * t + velocidad_inicial


def mov_recUniforme(tiempo, velocidad):
    x = velocidad*tiempo*1.0
    return x

def instanAng2((x1, y1), (x2, y2)):
    xDiff = x2 - x1
    yDiff = y2 - y1
    return math.degrees(math.atan2(yDiff, xDiff))

#print GetAngleOfLineBetweenTwoPoints( (400,300),(52,371))

def instanAng((x1, y1),(x2, y2)):
    if x1 == x2 and y1 == y2:
        #print "Esto es un punto!!!\n"
        return None

    if x1 == x2:#perpendicular al eje x
        if y1 < y2:
            return 90
        return 270

    if y1 == y2:#perpendicular al eje y
        if x1 < x2:
            return 0
        return 180

    pendiente = (y2- y1)/float(x2 - x1)
    pendiente = math.atan(pendiente)
    pendiente = math.degrees(pendiente)

    if pendiente < 0:
        pendiente = pendiente + 180

    if y2 < y1:
        pendiente  = pendiente + 180
    return pendiente
