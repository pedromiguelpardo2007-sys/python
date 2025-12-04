# -*- coding: utf-8 -*-
"""
Módulo polinomios.py  No cambiar el nombre del módulo
Dni: *Introducir Dni*
Apellidos, Nombre: *Introducir apellidos, nombre*
Grupo: *Introducir grupo*
"""

# Realiza las importaciones de módulos necesarios aquí



def val_polinomio(coeficientes, x):
    resultado=0
    grado=len(coeficientes)-1
    for i in coeficientes:
        resultado= resultado + i*(x**grado)
        grado= grado-1
    return resultado

def polinomio(coeficientes, abscisas):
    ordenadas= []
    for x in abscisas:
        ordenadas.append(val_polinomio(coeficientes, x))
    return ordenadas



def leer_datos_polinomio(nomFich):
    with open(nomFich,'r') as fich:
        lista_x= []
        lista_y=[]
        for linea in fich:
            valores= linea.split()
            lista_x.append(float(valores[0]))
            lista_y.append(float(valores[1]))
        return lista_x,lista_y
            


        
        
# Ejecutar el programa
if __name__ == "__main__":
    pass
    # Pruebas de funciones aqui
    
    
    
    # 
    # Generación de una nube de puntos de ejemplo
    # Puedes reemplazar estos datos con tus propios datos
    # x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # y = np.array([1, 1.8, 3.6, 4.2, 6.8, 7.5, 9.9, 9.7, 11.2, 12.6])


