def menu():
    opcion = int(input("Dame una opción entre 0 y 2:\n0: Salir\n1: 10 impares y salir\n2: Impares divisibles entre 3 o entre 7 y repetir\n"))
    while opcion < 0 or opcion > 2:
        print("Error, opción no válida")
        opcion = int(input("Dame una opción entre 0 y 2: "))
    return opcion


def divisibles(num):
    lista2 = []
    num_ini = 300
    while num_ini > 0:
        if num_ini % num == 0:
            lista2.append(num_ini)
        num_ini -= 1
    return lista2


def impares():
    lista1 = []
    i = 1
    while len(lista1) < 10:
        if i % 2:  # impar
            lista1.append(i)
        i += 1
    return lista1


def main():
    opcion = 2
    while opcion == 2:
        opcion = menu()
        if opcion == 0:
            print("Salir")
        elif opcion == 1:
            impares_positivos = impares()
            print("Los 10 primeros números positivos impares son:", impares_positivos)
            break  # salir del bucle
        else:
            divisibles_por_3 = divisibles(3)
            print("Los números menores de 300 divisibles entre 3 son:", divisibles_por_3)
            divisibles_por_7 = divisibles(7)
            print("Los números menores de 300 divisibles entre 7 son:", divisibles_por_7)


if __name__ == '__main__':
    main()
