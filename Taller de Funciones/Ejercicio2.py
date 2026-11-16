def pares_al_cuadrado(lista):
    """
    Funcion recursiva que filtra numeros pares y los eleva al cuadrado
    """
    if len(lista) == 0:
        return []
    else:
        if lista[0] % 2 == 0:
            return [lista[0] ** 2] + pares_al_cuadrado(lista[1:])
        else:
            return pares_al_cuadrado(lista[1:])
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6,7,8,9,10]
    pares_cuadrados = pares_al_cuadrado(numeros)
    print("La lista original es:", numeros)
    print("Los pares elevados al cuadrado son:", pares_cuadrados)