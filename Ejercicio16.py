vocales = ["a","e","i","o","u"]
vocalesMayus = ["A", "E", "I", "O", "U"]

def sacarVocales(cadena):
    """Recibe una cadena de caracteres,
       la recorre y quita todas las vocales."""

    resultado = ""
    for i in cadena:
        if not i in vocales:
            resultado += i
    return resultado


def sacarConsonantes(cadena):
    """Recibe una cadena de caracteres,
    la recorre y quita todas las consonantes."""
    
    resultado = ""
    for i in cadena:
        if i in vocales:
            resultado += i 
    return resultado


def siguienteVocal(cadena):
    """Recibe una cadena de caracteres,
       la recorre y reemplaza cada vocal
       por la vocal que le sigue."""
       
    for letra in cadena:
        if letra in vocales:
            for i in range(0,5):
                if letra == vocales[i]:
                    cadena = cadena.replace(letra, vocales[i+1])

    return cadena

def esCapicua(cadena):
    """Recibe una cadena de caracteres,
       la invierte y devuelve un valor
       booleano dependiendo de si es o 
       no capicua."""
       
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
 