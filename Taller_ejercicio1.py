total_pagar = 0
contador = 0
pedido = True 
x= int(input('Cuántos pedidos va a realizar:'))
while pedido:
    if x == 0:
        break
    print('\n---Menu de helados---')
    print('1. Sin topping ($1.90)')
    print('2. Topping de Frutas ($0.50 adicionales)')
    print('3. Topping de Granola ($1.50 adicionales)')
    print('4. Topping de Oreo ($1.00 adicional)')
    print('5. Topping de Brownie ($0.75 adicionales)')
    opcion = input('Elija una opcion de topping (1-5):')
    precio_helado = 1.90
        if opcion == '1':
        total_pedido = precio_helado
        print('Elegiste helado sin topping. Valor: $1.90')
        elif opcion == '2':
        total_pedido = precio_helado + 0.50
        print('Elegiste topping de Frutas: Valor: $2.40')
        elif opcion == '3':
        total_pedido = precio_helado + 1.50
        print('Elegiste topping de Granola. Valor: $3.40')
        elif opcion == '4':
        total_pedido = precio_helado + 1.00
        print('Elegiste topping de Oreo. Valor: $2.90')
        elif opcion == '5':
        total_pedido = precio_helado + 0.75
        print('Elegiste topping de Brownie. Valor: $2.65')
        else:
        total_pedido = 0
        print('Lo sentimos, no contamos con ese topping en nuestro menu.')
    total_pagar = total_pagar + total_pedido
    contador = contador + 1
    if contador == x:
        break 
print('Gracias por su compra, el valor total a pagar es: $', total_pagar)
    
