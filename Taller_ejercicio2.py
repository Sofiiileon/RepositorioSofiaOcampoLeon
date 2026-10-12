lista = [2,4,3,1,6,7,5,8,9,10]
print('Lista original:')
print(lista)
n= len(lista)
for i in range(n):
    for j in range(0, n-1):
        if lista[j] > lista[j + 1]:
            aux = lista[j]
            lista[j]= lista[j + 1]
            lista[j + 1] = aux
print('Lista ordenada con ciclos:')
print(lista)
lista_original = [2,4,3,1,6,7,5,8,9,10]
lista_original.sort()
print('Verificación con función sort():')
print(lista_original)