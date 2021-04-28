vocales = ["a","e","i","o","u"]

def sacarVocales(cadena):
    """Saca las vocales"""
    resultado = ""
    for i in cadena:
        if not i in vocales:
            resultado += i
    return resultado


def sacarConsonantes(cadena):
    """Saca las consonantes"""
    resultado = ""
    for i in cadena:
        if i in vocales:
            resultado += i 
    return resultado


def siguienteVocal(cadena):
    """Reemplaza las vocales de una cadena por la vocal que le sigue"""
    for letra in cadena:
        if letra in vocales:
            for i in range(0,4):
                if letra == vocales[i]:
                    cadena = cadena.replace(letra, vocales[i+1])
    for letra in cadena:
        if letra == "u":
            cadena = cadena.replace("u", "a")

    return cadena

def esCapicua(cadena):
    """Comprueba si la palabra ess capicua"""
    if cadena == cadena[::-1]:
        return True
    else:
        return False

cadena = input("Ingrese una cadena de texto: ")

opcion = int(input("""Ingrese lo que desea hacer: 
1. Sacar las vocales de la cadena
2. Sacar las consonantes de la cadena
3. Reemplazar las vocales por su siguiente
4. Saber si una palabra es capicua o no
"""))

if opcion == 1:
    print(sacarVocales(cadena))

if opcion == 2:
    print(sacarConsonantes(cadena))

if opcion == 3:
    print(siguienteVocal(cadena))

if opcion == 4:
    if esCapicua(cadena) == True:
        print("Si es")
    else:
        print("No es")
 