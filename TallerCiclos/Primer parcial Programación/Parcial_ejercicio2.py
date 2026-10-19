total_pagar = 0
continuar = 'si'
#Ciclo principal para registrar a los clientes
while continuar == 'si':
    print('Ingrese la edad de cliente')
    edad = int(input())
#Determino el valor de la entrada según la edad del cliente
    if edad < 5:
        precio = 0
        print('El cliente tiene menos de 5 años. Entrada gratis ($0).')
    elif edad >= 5 and edad <= 18:
        precio = 5
        print('El valor de la entrada es de $5.')
    else:
        precio = 10
        print('El valor de la entrada es de $10.')
# Acumulo el valor de la entrada al total a pagar
    total_pagar = total_pagar + precio
    print('¿Desea ingresar otra persona a la sala de juego? (si/no) ')
    continuar = input().lower().strip()
# Muestro el valor total a pagar por todas las entradas
print('El valor total a pagar por todas las entradas es: $', total_pagar)