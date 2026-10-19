#Se inicia la lista para la caja de almacenamiento
caja = []
continuar = 'si'
numero_bolsa = 1
while continuar == 'si':
    print('Hay una bolsa lista en la máquina? (si/no)')
    hay_bolsa = input().lower().strip()
    if hay_bolsa == 'si':
        print('1. Verificando bolsa... Bolsa detectada.')
        print('2. Vaciando el arroz en la bolsa...')
        print('3. Sellando la bolsa termicamente...')
        bolsa_nombre = 'Bolsa_' + str(numero_bolsa)
# Agrego la bolsa a la lista (caja) usando .append()
        caja.append(bolsa_nombre)
        print('4. Empacando', bolsa_nombre, 'en la caja de almacenamiento.')
        numero_bolsa = numero_bolsa + 1
    else:
        print('No hay bolsa lista en la máquina. Por favor, coloque una bolsa para continuar vaciando el arroz.')
    print('Desea que la maquina siga funcionando? (si/no)')
    continuar = input().lower().strip()
print('    Proceso finalizado    ')
# Imprimo la lista completa de la caja
print('Caja de distribución', caja)
print('Total de bolsas empacadas:', len(caja))
