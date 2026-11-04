def suma_recursiva(lista):
    """
    Funcion recursiva que calcula la suma total
 """
    if not lista:
        return 0
    return lista[0] + suma_recursiva(lista[1:])
if __name__ == "__main__":
    numeros = [5, 10, 15, 20]
    resultado = suma_recursiva(numeros)
    print("La lista es:", numeros)
    print("La suma total es:", resultado)