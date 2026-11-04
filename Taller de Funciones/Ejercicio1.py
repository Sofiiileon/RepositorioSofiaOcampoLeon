def factorial(n):
    """
    funcion que calcula el factorial de un numero n
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
if __name__ == "__main__":
    print('por favor, digite un número entero')
    n = int(input())
    res = factorial(n)
    print('El factorial de', n, 'es:', res)
   