# -*- coding: utf-8 -*-

"""
Módulo main.py  No cambiar el nombre del módulo
Dni: *Introducir Dni*
Apellidos, Nombre: *Introducir apellidos, nombre*
Grupo: *Introducir grupo*
"""

# -*- coding: utf-8 -*-

"""
Módulo main.py  No cambiar el nombre del módulo
Dni: *Introducir Dni*
Apellidos, Nombre: *Introducir apellidos, nombre*
Grupo: *Introducir grupo*
"""

import matplotlib.pyplot as plt
import numpy as np 

# Importaciones correctas
from polinomios import leer_datos_polinomio, polinomio

def dame_grado():
    while True:
        grado = int(input('Introduce el grado del polinomio: '))
        if grado >= 0:
            return grado
        print('ERROR: debes introducir un grado >=0')
            

def grafica(x, y, coeficientes, num_valores=100):

    min_x = min(x)
    max_x = max(x)

    # generar puntos equidistantes
    xs = np.linspace(min_x, max_x, num_valores)

    # valores del polinomio
    ys = polinomio(coeficientes, xs)

    # puntos del fichero
    plt.plot(x, y, 'b.')

    # curva del polinomio
    plt.plot(xs, ys, 'r')
  
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Ajuste polinomico")
    plt.grid(True)
    plt.show()


def main():

    nomFich = input("Introduce el nombre del fichero: ")

    lista_x, lista_y = leer_datos_polinomio(nomFich)

    grado = dame_grado()

    # cálculo polinomio mejor ajuste
    coeficientes = np.polyfit(lista_x, lista_y, grado)

    print(f"Polinomio de ajuste con coeficientes: {coeficientes}")

    # graficar
    grafica(lista_x, lista_y, coeficientes)


if __name__ == "__main__":
    main()
