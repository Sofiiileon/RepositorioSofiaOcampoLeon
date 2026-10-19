import random
x = 0
y = 0
print('Punto de partida:', (x, y))
for paso in range(100):
    direccion = random.randint(1, 4)
    if direccion == 1:
        y = y + 1
    elif direccion == 2:
        y = y - 1
    elif direccion == 3:
        x = x + 1
    else:
        x = x - 1
    print('Paso' , paso + 1, 'Ubicación', (x, y))
print('Ubicación final del borracho:',(x, y))