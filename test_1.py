# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:08:31 2025

@author:Pedro Miguel Pardo Ramos    
"""
# ATENCIÓN: no modificar los nombres de las funciones ni sus parámetros si estos se proporcionan


def numElemLista(mensajePeticion):  # 1 Pto
    while True:
        n = int(input(mensajePeticion))
        if n > 1:
            return n
        else:
            print("ERROR: el número debe ser mayor que 1")


# ATENCIÓN: la función pideIntervalo() no necesita parámetros
def pideIntervalo():  # 1 Pto
    sup = int(input("Introduce el valor superior del intervalo: "))
    inf = int(input("Introduce el valor inferior del intervalo: "))
    if inf <= sup:
        return (inf, sup)
    else:
        print(f"ERROR: no se cumple que {inf} <= {sup}")

        
       


def introduceLista(numElementos, intervalo):  # 1 pto
    inf, sup = intervalo
    lista = []
    print(f"Introduce {numElementos} valores comprendidos en el intervalo cerrado [{inf}, {sup}]")
    for i in range(numElementos):
        while True:
            val = int(input(f"Lista[{i}]: "))
            if inf <= val <= sup:
                lista.append(val)
                break
            else:
                print(f"El valor {val} introducido no pertenece al intervalo cerrado [{inf}, {sup}]")
    return lista


# ATENCIÓN: la función calculaListaIntermedia() puede necesitar parámetros
def calculaListaIntermedia(lista):  # 2 Ptos
    listaIntermedia = []
    for x in lista:
        if x % 2 != 0:   # impar
            listaIntermedia.append((x + 1) // 2)
        else:
            listaIntermedia.append(x // 2)
    return listaIntermedia


# ATENCIÓN: la función listaParesImparesSinRepetir() puede necesitar parámetros
def listaParesImparesSinRepetir(listaintermedia):  # 2 Ptos
    impares = []
    pares = []

    for x in listaintermedia:
        if x % 2 != 0:
            
                impares.append(x)
        else:
           
                pares.append(x)

    return impares + pares


def main():  # 3 Ptos
    

        n = numElemLista("Introduce número de elementos de la lista mayor que 1: ")

        intervalo = pideIntervalo()

        lista1 = introduceLista(n, intervalo)

        listaIntermedia = calculaListaIntermedia(lista1)
        print(f"listaIntermedia = {listaIntermedia}")

        listaFinal = listaParesImparesSinRepetir(listaIntermedia)
        print(f"listaFinal = {listaFinal}")

      

if __name__ == '__main__':
    main()
