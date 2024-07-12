from random import randrange
from numpy import sum
import csv


def generar_sueldos(lista):
        nom = 'Juan Perez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Maria Gracia '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Carlos Lopez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Ana Martinez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Pedro Rodriguez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Laura Hernandez  '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Miguel Sanchez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Isabel gomez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Francisco diaz '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        nom = 'Elena Fernandez '
        sueldo = randrange(300000,2500000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)
def menu():
    m = """BIENVENIDO
**************************************
[1] Asignar Sueldos Aleatorios.
[2] Clasificar Sueldos
[3] Reporte de sueldos
[4] Salir del programa
--> """
    print(m,end="")

def validar_op():
    while True:
        try:
            op = int(input())
            if op>=1 and op<=4:
                return op
            else:
                raise ValueError
        except:
            print("Selecciona una opcion valida. --> ",end="")

def clasificar_empleados(lista):
    bajos = []
    medios = []
    altos = []

    for trabajador in lista:
        if trabajador["sueldo"]<=800000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]<=2000000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)

    print("EMPLEADOS CON SUELDO MENOR A $800.000:")
    print()

    for e in bajos:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")
    print("**************************************")

    print("EMPLEADOS CON SUELDO ENTRE $800.000 Y $2.000.000")
    print()

    for e in medios:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")
    print("**************************************")

    print("EMPLEADOS CON SUELDO MAYORES A $2.000.000:")
    print()

    for e in altos:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")

def sueldo_bajo(lista):
    bajo = lista[0]
    for empleado in lista:
        if bajo["sueldo"]>empleado["sueldo"]:
            bajo = empleado
    return bajo

def sueldo_alto(lista):
    alto = lista[0]
    for empleado in lista:
        if alto["sueldo"]<empleado["sueldo"]:
            alto = empleado
    return alto

def imprimir_estadisticas(lista):
    print(f"Sueldo más bajo: {sueldo_bajo(lista)}")
    print(f"Sueldo más alto: {sueldo_alto(lista)}")
    listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
    suma = sum(listar_sueldos)
    promedio = suma/10
    print(f"Sueldo promedio: {promedio:,.0f}")

def report_sueldos(lista):
    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto * 0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        a = {"nombre":trabajador["nombre"],"sueldo_bruto":sueldo_bruto,"afp":afp,"salud":salud,"sueldo_liquido":sueldo_liquido}
        reporte.append(a)
    
    nombre_campos = ["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
    with open('Reporte Sueldos.csv','w',newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=nombre_campos)
        escritor.writeheader()
        escritor.writerows(reporte)