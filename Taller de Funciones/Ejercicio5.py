def encontrar_maximo(lista):
    """
    Funcion recursiva que encuentra el numero mayor de una lista comparando elementos uno a uno sin usar max().
    """
    if len(lista) == 1:
        return lista[0]
    maximo_resto = encontrar_maximo(lista[1:])
    if lista[0] > maximo_resto:
        return lista[0]
    else:
        return maximo_resto
    if __name__ == "__main__":
        numeros = [3, 8, 2, 15, 9, 4]
        mayor = encontrar_maximo(numeros)
        print('La lista es:', numeros)
        print('El número más grande es:', mayor)