mayus = input("Ingrese una palabra Capitalizada: ")

pal = input("ingrese la misma palabra en minusculas: ")

def compararPalabras(palMayus, pal):
    if palMayus == pal.upper():
        return True
    else:
        return False


if compararPalabras(mayus,pal) == True:
    print("Son la misma palabra.")
else:
    print("Son palabras distintas.")
