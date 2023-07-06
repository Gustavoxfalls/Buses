import numpy as np
from pasajero import *
from funciones import *

arreglo=np.full((8,4),'--')
lista_pasajeros=[]

ciclo = True
llenar(arreglo)


def validarRut():
    while True:
        try:
            rut = int(input("Ingrese Rut:"))
            if str(rut).isdigit() and len(str(rut)) == 8:
                return rut
            else:
                print("el rut ingresado es incorrecto")
        except BaseException as error:
            print(f"error:{error}")


def validarEdad():
    while True:
        try:
            edad = int(input("Ingrese Edad:"))
            if edad >=2:
                return edad
            else:
                print("la edad debe ser mayor a 2 ")
        except BaseException as error:
            print(f"error:{error}")


def ingresarPasajero(lista_pasajeros, num_asiento):
    pasa = Pasajero()
    pasa.rut = validarRut()
    pasa.nombre = input("Ingrese Nombre:")
    pasa.apellido = input("Ingrese Apellido:")
    pasa.edad = validarEdad()
    pasa.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=12:
        pasa.valor = 5600
    if num_asiento>=13 and num_asiento<=20:
        pasa.valor =4500
    if num_asiento>=21 and num_asiento<=32:
        pasa.valor = 4000
    lista_pasajeros.append(pasa)

def listarPasajeros(lista_pasajeros):
    print("Listado de pasajeros")
    print("--------------------")
    for pasa in lista_pasajeros:
        print(f"Rut:{pasa.rut} Nombre:{pasa.nombre} Valor:{pasa.valor} Asiento:{pasa.num_asiento}")

def TotalPasajeros(lista_pasajeros):
    print("Totales")
    print("-------")
    vip = 0
    med = 0
    fin = 0
    for pasa in lista_pasajeros:
        if int(pasa.valor) == 5600:
            vip = vip + 1
        if int(pasa.valor) == 4500:
            med = med + 1
        if int(pasa.valor) == 4000:
            fin = fin + 1
    print(f"Total Frente : {vip} Valor:{vip*5600}")
    print(f"Total Medio  : {med} Valor:{med*4500}")
    print(f"Total Fondo  : {fin} Valor:{fin*4000}")
    total_pasajeros = vip + med + fin
    total_pesos = (vip*5600) + (med*4500) + (fin*4000)
    print(f"Total Pasajeros:{total_pasajeros}")
    print(f"Total Pesos: {total_pesos}")

def comprarUnAsiento(arreglo,lista_pasajeros):
    compra = 0
    try:
        cantidad = int(input("Ingrese Numero de asientos a comprar (1-5): "))
        if cantidad>=1 and cantidad<=5:
            while compra<cantidad:
                mostrar(arreglo)
                try:
                    num_asiento = int(input("Numero Asiento:"))
                    if num_asiento>=1 and num_asiento<=32:
                        resp=verificarAsiento(arreglo,num_asiento)
                        if resp == True:
                            marcarAsiento(arreglo,num_asiento)
                            ingresarPasajero(lista_pasajeros,num_asiento)
                            compra = compra + 1
                        else:
                            print("asiento no disponible, no sea simio")
                except BaseException as error:
                    print(f"error:{error}")
        else:
            print("la cantidad debe estar entre 1 y 5")
    except BaseException as error:
        print(f"error:{error}")

while ciclo:
    print("Menu Buses")
    print("1) Comprar Asiento")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Listado de pasajeros")
    print("4) Gananciacias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione:"))
        match op:
            case 1:
                comprarUnAsiento(arreglo,lista_pasajeros)
            case 2:
                mostrar(arreglo)
            case 3:
                listarPasajeros(lista_pasajeros)
            case 4:
                TotalPasajeros(lista_pasajeros)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")
