mayus = input("Ingrese una palabra Capitalizada: ")

pal = input("ingrese la misma palabra en minusculas: ")

def compararPalabras(palMayus, pal):
    """Compara las palabras y devuelve True si son la misma"""
    if palMayus == pal.upper():
        return True
    else:
        return False


if compararPalabras(mayus,pal) == True:
    print("Son la misma palabra.")
else:
    print("Son palabras distintas.")
