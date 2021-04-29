def mostrarSiglas(cadena):
    """Recibe una cadena de caracteres y
       devuelve solo la primera letra de cada palabra"""
       
    siglas = ""
    lista = cadena.split()
    for letra in lista:
        siglas += letra[0]
    return siglas


def convertirLetras(cadena):
    """Recibe una cadena de caracteres y
       Convierte la primera letra de cada
       palabra en mayuscula"""
       
    lista = cadena.split()
    oracion = ""
    for i in lista:
        oracion = oracion + i.capitalize() + " "
    return oracion


def mostrarPlabrasCon(cadena,letra):
    """Recibe una cadena de caracteres y una letra
    y muestra solo las palabras que empiecen con la
    letra ingresada."""
    
    lista = cadena.split()
    palabras = ""
    for palabra in lista:
        if palabra[0] == letra or palabra[0] == letra:
            palabras += palabra + " "
    return palabras


cadena = input("Ingrese una cadena: ")

opcion = int(input("""Ingrese lo que desea hacer: 
1. Devolver las siglas de una cadena
2. La cadena con la primera letra de cada palabra en mayúscula
3. Devolver solo las palabras que empiezan con determinada letra
"""))

if opcion == 1:
    print("Las siglas de su cadena son: ", mostrarSiglas(cadena))

if opcion == 2:
    print(convertirLetras(cadena))

if opcion == 3:
    letra = ""
    while letra == "" or letra.isdigit():
        letra = input("Ingrese la letra: ")
    print(mostrarPlabrasCon(cadena,letra))
