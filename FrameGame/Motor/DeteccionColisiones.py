

def deteccionColisiones(personajes, plataformas, TablaColsiones):
    for personaje in  personajes:
        angulo = personaje.status["angulo"]
        x = personaje._x
        y = personaje._y
        for plataforma in  plataformas:

            if angulo < 0 and angulo >= -90:
                if personaje.rec1.top < plataforma._y:
                    if plataforma.rectangulo.colliderect(personaje.rec1):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._y = plataforma._y - personaje.largo

                if personaje.rec3.left < plataforma._x:
                    if plataforma.rectangulo.colliderect(personaje.rec3):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._x = plataforma._x - personaje.ancho

            if (angulo <-90 and angulo >= -180) or angulo == 180:
                if personaje.rec1.top < plataforma._y:
                    if plataforma.rectangulo.colliderect(personaje.rec1):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._y = plataforma._y - personaje.largo

                if personaje.rec2.left+personaje.rec2.width > plataforma._x+plataforma.ancho:
                    if plataforma.rectangulo.colliderect(personaje.rec2):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._x = plataforma._x + plataforma.ancho


            if angulo < 180 and angulo >=90:
                if personaje.rec2.left + personaje.rec2.width > plataforma._x + plataforma.ancho:
                    if plataforma.rectangulo.colliderect(personaje.rec2):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._x = plataforma._x + plataforma.ancho

                if personaje.rec4.top+personaje.rec4.height>plataforma._y+plataforma.largo:
                    if plataforma.rectangulo.colliderect(personaje.rec4):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._y = plataforma._Y+plataforma.largo

            if angulo < 90 and angulo >=0:
                if personaje.rec4.top + personaje.rec4.height > plataforma._y + plataforma.largo:
                    if plataforma.rectangulo.colliderect(personaje.rec4):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._y = plataforma._y + plataforma.largo

                if personaje.rec3.left < plataforma._x:
                    if plataforma.rectangulo.colliderect(personaje.rec3):
                        personaje.setSalto(False)
                        personaje.setCorrer(False)
                        personaje.setCaminar(False)
                        #personaje._x = plataforma._x - personaje.ancho
            """
            if plataforma.rectangulo.colliderect(personaje.rec1):
                personaje.setSalto(False)
                personaje._y = plataforma._y - personaje.largo

            if plataforma.rectangulo.colliderect(personaje.rec2):
                personaje.setSalto(False)
                personaje._x = plataforma._x+plataforma.ancho

            if plataforma.rectangulo.colliderect(personaje.rec3):
                personaje.setSalto(False)
                personaje.x = plataforma.x-personaje.ancho

            if plataforma.rectangulo.colliderect(personaje.rec4):
                pass"""


def restituir_pos(p, entorno, _lado, sentido=False):

    if sentido == True:
        if _lado == 1:
            _lado = 4

        elif _lado == 2:
            _lado = 3

        elif _lado == 3:
            _lado = 2

        elif _lado == 4:
            _lado = 1

    if _lado == 1:
        p._y = entorno._y - p.largo
    elif _lado == 2:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left + entorno.imagen.sprite.rect.size[0] + 3
    elif _lado == 3:
        p.imagen.sprite.rect.left = entorno.imagen.sprite.rect.left - p.imagen.sprite.rect.size[0] - 3
    elif _lado == 4:
        p.imagen.sprite.rect.top  = entorno.imagen.sprite.rect.top + entorno.imagen.sprite.rect.size[1] + 2
    p.pos_rectangulos()