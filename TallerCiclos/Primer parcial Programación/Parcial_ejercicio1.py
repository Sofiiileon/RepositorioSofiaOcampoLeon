total_pagar=0
continuar= 'si'
#Ciclo principal para registrar los pedidos de comida rápida    
while continuar=='si':
    print('   Menú comida rápida   ')
    print('1. Hamburguesa Sencilla $16.500')
    print('2. Hamburguesa Doble $21.500')
    print('3. Hamburguesa Especial $18.000')
    print('4. Perro caliente $15.000')
    print('5. Pizza personal $12.500')
    print('6. Salchipapa $14.500')
    print('7. Desgranado de pollo/carne $24.500')
    print('8. Gaseosa Postobon $6.500')
    print('Ingrese el producto que desea pedir')
    opcion = input().lower().strip()
    #Valido la opción ingresada y acumulo el valor del pedido al total a pagar
    if 'hamburguesa sencilla' in opcion:
        total_pagar = total_pagar + 16500
        print('Usted ha pedido una hamburguesa sencilla, el valor es de $16.500')
    elif 'hamburguesa doble' in opcion:
        total_pagar = total_pagar + 21500
        print('Usted ha pedido una hamburguesa doble, el valor es de $21.500')  
    elif 'hamburguesa especial' in opcion:
        total_pagar = total_pagar + 18000
        print('Usted ha pedido una hamburguesa especial, el valor es de $18.000')
    elif 'perro caliente' in opcion:
        total_pagar = total_pagar + 15000
        print('Usted ha pedido un perro caliente, el valor es de $15.000')  
    elif 'pizza personal' in opcion:
        total_pagar = total_pagar + 12500
        print('Usted ha pedido una pizza personal, el valor es de $12.500')
    elif 'salchipapa' in opcion:
        total_pagar = total_pagar + 14500
        print('Usted ha pedido una salchipapa, el valor es de $14.500')
    elif 'desgranado de pollo/carne' in opcion:
        total_pagar = total_pagar + 24500
        print('Usted ha pedido un desgranado de pollo/carne, el valor es de $24.500')
    elif 'gaseosa postobon' in opcion:
        total_pagar = total_pagar + 6500
        print('Usted ha pedido una gaseosa postobon, el valor es de $6.500')
    else:
#Mensaje de error en caso de que el usuario ingrese un producto que no esté en el menú
        print('Omg, ese plato aún no esta en nuestro menú, pronto lo tendremos disponible, Puedes elegir otra de las deliciosas opciones que tenemos en nuestro menú :D')
    continuar=  input('Desea pedir otro producto? (si/no)').lower().strip()
#Muestro el valor total a pagar por todos los pedidos realizados
print('Gracías por su compra, el valor total a pagar es: $', total_pagar)



   