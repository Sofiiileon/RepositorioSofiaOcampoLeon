def invertir_cadena(texto):
    """
    función recursiva que invierte una cadena de texto.
    """
    if len(texto) <= 1:
        return texto
    return invertir_cadena(texto[1:]) + texto[0]
if __name__ == "__main__":
    print('Por favor, digite un texto')
    palabra = input()
    resultado = invertir_cadena(palabra)
    print ('El texto invertido es:', resultado)