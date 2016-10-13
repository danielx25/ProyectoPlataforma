

def deteccionColisiones(personajes, plataformas, TablaColsiones):
    for personaje in  personajes:
        for plataforma in  plataformas:

            if plataforma.rectangulo.colliderect(personaje.rec1):
                personaje.setSalto(False)
                personaje._y = plataforma._y - personaje.largo

            if plataforma.rectangulo.colliderect(personaje.rec2):
                pass

            if plataforma.rectangulo.colliderect(personaje.rec3):
                pass

            if plataforma.rectangulo.colliderect(personaje.rec4):
                pass


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