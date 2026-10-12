print('Digite una palabra')
palabra = input()
n = len(palabra)
for tam in range(1, n + 1):
    for i in range(n - tam + 1):
        subcadena = palabra[i:i + tam]
        print(subcadena)

