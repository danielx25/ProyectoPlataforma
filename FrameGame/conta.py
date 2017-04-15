l1="""caja
fondo fijo o caja chica
banco
documentos por cobrar
clientes nacionales
inventario mercancias
retiros personales
iva credito fiscal
prestamos al personal
terrenos
edificios e instalaciones
herramientas
muebles y utiles
maquinarias y equipos
equipo de computacion
vehiculos
depreciaciones acumuladas
cuentas x cobrar e.relac.
seguros anticipados
arriendos anticipados
anticipos a proveedores
inventario prod.terminados
inventario materia primas
inventario repuestos
otras cuentas por cobrar
derechos de llaves
patentes y marcas de fabrica
g. origanizacion pta marcha"""

l2 = """proveedores nacionales
proveedores extreanjeros
cuentas por pagar
letras por pagar
leyes sociales x pagar
honorarios por pagar
sueldo por pagar
iva debito fiscal
otros impuestos por pagar
arriendos por pagar
cuentas x pagar e.relac.c.p
prestamos bancarios l.p
provisiones x pagar l.p
acreedores extranjeros l.p
capital social
cuentas x pagar e.relac.c.p
fondo rev. capital propio
reservas sociales
cuentas x pagar e.relac.l.p
resultados x distribuir
otras cuentas x pagar
provisiones y retenciones
prov.a indemniz x pagar
otros ingresos anticipados"""

l3 = """costos de ventas
gastos generales
suedos pagados
aportes patronales
impuestos pagados
intereses pagados
arreindos pagados
honorarios pagados
gastos de administracion
gastos financieros
correccion monetaria(-)
diferencias de cambios
perdida vta activos fijo"""

l4="""ventas nacionales
exportaciones
intereses cobrados
diferecias de cambio
correccion monetaria(+)
otras ventas
ingresos propios
utilidad vta activo fijo"""

l1 = l1.split("\n")
l2 = l2.split("\n")
l3 = l3.split("\n")
l4 = l4.split("\n")
import random

diccionario = {"activos":l1, "pasivo y patrimonio": l2, "resultado perdidas": l3, "resultado ganancias": l4}
def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 < = j <= i-1
        items[j], items[i] = items[i], items[j]
    return items
megaLista = l1+l2+l3+l4
megaLista = sattoloCycle(megaLista)
rango = len(megaLista)
contador = 0
for i in range(rango):
    aleatorio = random.randint(0,len(megaLista)-1)
    adivina = megaLista[aleatorio]

    print "\n1: activos \n2: pasivo y patrimonio"
    print "3: resultado perdida \n4: resultado ganancia\n"
    print i, adivina
    try:
        opcion = int(input(": "))
    except ValueError:
        print "casi :D"
        continue

    categoria = "None"
    if adivina in diccionario["activos"]:
        categoria = "activos"
    if adivina in diccionario["pasivo y patrimonio"]:
        categoria = "pasivo y patrimonio"
    if adivina in diccionario["resultado perdidas"]:
        categoria = "resultado perdidas"
    if adivina in diccionario["resultado ganancias"]:
        categoria = "resultado ganancias"

    if opcion == 1:
        if adivina in diccionario["activos"]:
            print "buena"
            contador+=1
        else:
            print "mal: "+categoria
    if opcion == 2:
        if adivina in diccionario["pasivo y patrimonio"]:
            print "buena"
            contador += 1
        else:
            print "mal: " + categoria
    if opcion == 3:
        if adivina in diccionario["resultado perdidas"]:
            print "buena"
            contador += 1
        else:
            print "mal: " + categoria
    if opcion == 4:
        if adivina in diccionario["resultado ganancias"]:
            print "buena"
            contador += 1
        else:
            print "mal: " + categoria
    if opcion > 4 or opcion<1:
        break
    megaLista.pop(megaLista.index(adivina))
print
print "puntaje: "+str(contador)+ " de "+str(rango)
print "contestadas: ", i
print "buenas: ",contador
print "malas: ", i-contador




