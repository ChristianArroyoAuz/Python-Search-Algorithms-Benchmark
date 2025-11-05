from colorama import Fore
import random
import time
import math
import sys


def cero():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t BUSQUEDA LINEAL y BINARIA \t\t\t')
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Busqueda Lineal.')
    print('\t 2. Ingrese "2" para Busqueda Binaria.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_ingresada_busqueda = int(input("\t  " + "¿Cual es tu opción?: "))
    tipo_busqueda(opcion_ingresada_busqueda)

def uno():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     BUSQUEDA LINEAL      \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Busqueda con 100 elementos.')
    print('\t 2. Ingrese "2" para Busqueda con 10000 elementos.')
    print('\t 3. Ingrese "0" para Volver.')
    opcion_ingresada_elementos_1 = int(input("\t  " + "¿Cual es tu opción?: "))
    numero_elementos_1(opcion_ingresada_elementos_1)

def dos():
    print("                                                   ")
    print(Fore.BLUE + "\t\t\t     BUSQUEDA BINARIA     \t\t\t")
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Busqueda con 100 elementos.')
    print('\t 2. Ingrese "2" para Busqueda con 10000 elementos.')
    print('\t 3. Ingrese "0" para Volver.')
    opcion_ingresada_elementos_2 = int(input("\t  " + "¿Cual es tu opción?: "))
    numero_elementos_2(opcion_ingresada_elementos_2)

def tres():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t BUSQUEDA LINEAL CON 100 ELEMENTOS \t\t\t' + Fore.BLACK)
    print('Lista de elementos:')
    conjunto_inicial = set()
    while len(conjunto_inicial) < 100:
        conjunto_inicial.add(random.randint(0, 1000))
    lista_ordenada = sorted(list(conjunto_inicial))
    print(lista_ordenada)
    elemento_buscar = int(input("\t  " + "¿Que estas buscando?: "))
    inicio_0 = time.time()
    inicio_1 = time.time()
    x = False
    y = False
    for i in range(len(lista_ordenada)):
        if lista_ordenada[i] == elemento_buscar:
            time.sleep(0.01)
            fin_1 = time.time()
            x = True
        else:
            time.sleep(0.01)
            y = True
    fin_0 = time.time()
    if x == True and y == True:
        print(Fore.GREEN + "Elemento " + str(elemento_buscar) + " encontrado en la posición: " + str(lista_ordenada.index(elemento_buscar)))
        print(f"Tiempo de busqueda lineal: {fin_0 - inicio_0} segundos.")
        print(f"Tiempo de busqueda elemento: {fin_1 - inicio_1} segundos.")
    if x == False and y == True:
        print(Fore.RED + "Elemento " + str(elemento_buscar) + " no encontrado. El elemento no pertenece a la lista.")
        print(f"Tiempo de busqueda lineal: {fin_0 - inicio_0} segundos.")
    cero()

def cuatro():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t BUSQUEDA LINEAL CON 10000 ELEMENTOS \t\t\t' + Fore.BLACK)
    print('Lista de elementos:')
    conjunto_inicial = set()
    while len(conjunto_inicial) < 10000:
        conjunto_inicial.add(random.randint(0, 100000))
    lista_ordenada = sorted(list(conjunto_inicial))
    print(lista_ordenada)
    elemento_buscar = int(input("\t  " + "¿Que estas buscando?: "))
    inicio_0 = time.time()
    inicio_1 = time.time()
    x = False
    y = False
    for i in range(len(lista_ordenada)):
        if lista_ordenada[i] == elemento_buscar:
            time.sleep(0.01)
            fin_1 = time.time()
            x = True
        else:
            time.sleep(0.01)
            y = True
    fin_0 = time.time()
    if x == True and y == True:
        print(Fore.GREEN + "Elemento " + str(elemento_buscar) + " encontrado en la posición: " + str(lista_ordenada.index(elemento_buscar)))
        print(f"Tiempo de busqueda lineal: {fin_0 - inicio_0} segundos.")
        print(f"Tiempo de busqueda elemento: {fin_1 - inicio_1} segundos.")
    if x == False and y == True:
        print(Fore.RED + "Elemento " + str(elemento_buscar) + " no encontrado. El elemento no pertenece a la lista.")
        print(f"Tiempo de busqueda lineal: {fin_0 - inicio_0} segundos.")
    cero()
    
def cinco():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t BUSQUEDA BINARIA CON 100 ELEMENTOS \t\t\t' + Fore.BLACK)
    print('Lista de elementos:')
    conjunto_inicial = set()
    while len(conjunto_inicial) < 100:
        conjunto_inicial.add(random.randint(0, 1000))
    lista_ordenada = sorted(list(conjunto_inicial))
    print(lista_ordenada)
    elemento_buscar = int(input("\t  " + "¿Que estas buscando?: "))
    inicio_0 = time.time()
    def busqueda_binaria(valor):
        inicio = 0
        final = len(lista_ordenada) - 1
        while inicio <= final:
            mitad = (inicio + final) // 2
            time.sleep(0.01)
            if valor == lista_ordenada[mitad]:
                time.sleep(0.01)
                return mitad
            elif valor > lista_ordenada[mitad]:
                time.sleep(0.01)
                inicio = mitad + 1
            else:
                time.sleep(0.01)
                final = mitad - 1
        return None
    def buscar_valor(valor):
        respuesta_busqueda = busqueda_binaria(valor)
        if respuesta_busqueda is None:
            fin_0 = time.time()
            print(Fore.RED + "Log(n): " + str(round(math.log2(len(lista_ordenada)), 2)) + Fore.BLACK)
            print(Fore.RED + f"Tiempo de busqueda binario: {fin_0 - inicio_0} segundos." + Fore.BLACK)
            return Fore.RED + "Elemento " + str(elemento_buscar) + " no encontrado. El elemento no pertenece a la lista."
        else:
            fin_0 = time.time()
            print(Fore.GREEN + "Log(n): " + str(round(math.log2(len(lista_ordenada)), 2)) + Fore.BLACK)
            print(Fore.GREEN + f"Tiempo de busqueda binario: {fin_0 - inicio_0} segundos." + Fore.BLACK)
            return Fore.GREEN + "Elemento " + str(elemento_buscar) + " encontrado en la posición: " + str(lista_ordenada.index(elemento_buscar))
    print(buscar_valor(elemento_buscar))
    cero()

def seis():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t BUSQUEDA BINARIA CON 10000 ELEMENTOS \t\t\t' + Fore.BLACK)
    print('Lista de elementos:')
    conjunto_inicial = set()
    while len(conjunto_inicial) < 10000:
        conjunto_inicial.add(random.randint(0, 100000))
    lista_ordenada = sorted(list(conjunto_inicial))
    print(lista_ordenada)
    elemento_buscar = int(input("\t  " + "¿Que estas buscando?: "))
    inicio_0 = time.time()
    def busqueda_binaria(valor):
        inicio = 0
        final = len(lista_ordenada) - 1
        while inicio <= final:
            mitad = (inicio + final) // 2
            time.sleep(0.01)
            if valor == lista_ordenada[mitad]:
                time.sleep(0.01)
                return mitad
            elif valor > lista_ordenada[mitad]:
                time.sleep(0.01)
                inicio = mitad + 1
            else:
                time.sleep(0.01)
                final = mitad - 1
        return None
    def buscar_valor(valor):
        respuesta_busqueda = busqueda_binaria(valor)
        if respuesta_busqueda is None:
            fin_0 = time.time()
            print(Fore.RED + "Log(n): " + str(round(math.log2(len(lista_ordenada)), 2)) + Fore.BLACK)
            print(Fore.RED + f"Tiempo de busqueda binario: {fin_0 - inicio_0} segundos." + Fore.BLACK)
            return Fore.RED + "Elemento " + str(elemento_buscar) + " no encontrado. El elemento no pertenece a la lista."
        else:
            fin_0 = time.time()
            print(Fore.GREEN + "Log(n): " + str(round(math.log2(len(lista_ordenada)), 2)) + Fore.BLACK)
            print(Fore.GREEN + f"Tiempo de busqueda binario: {fin_0 - inicio_0} segundos." + Fore.BLACK)
            return Fore.GREEN + "Elemento " + str(elemento_buscar) + " encontrado en la posición: " + str(lista_ordenada.index(elemento_buscar))
    print(buscar_valor(elemento_buscar))
    cero()

def default_1():
    print(Fore.RED + "\t  Opción Erronea.  \t\n")
    cero()

def default_2():
    print(Fore.RED + "\t  Opción Erronea.  \t\n")
    uno()
    
def default_3():
    print(Fore.RED + "\t  Opción Erronea.  \t\n")
    dos()

def tipo_busqueda(numero_0):
    return opciones_busqueda.get(numero_0, default_1)()

def numero_elementos_1(numero_1):
    return opciones_elementos_1.get(numero_1, default_2)()

def numero_elementos_2(numero_2):
    return opciones_elementos_2.get(numero_2, default_3)()

def salir():
    print("                                                     ")
    print(Fore.BLUE + '\t\t\t ADIÓS BUEN DÍA \t\t\t' + Fore.BLACK)
    sys.exit()

def volver():
    cero()

opciones_busqueda = {
    1: uno,
    2: dos,
    0: salir
    }

opciones_elementos_1 = {
    1: tres,
    2: cuatro,
    0: volver
    }

opciones_elementos_2 = {
    1: cinco,
    2: seis,
    0: volver
    }

cero()