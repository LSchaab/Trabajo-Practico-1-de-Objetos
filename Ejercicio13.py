def compararPalabras(palMayus, pal):
    """Recibe:
            palMayus: <str>
            pal: <str>
       compara si la palabra en minuscula
       es igual a la ingresada en maysucula
       y devuelve un valor booleano."""
       
    if palMayus == pal.upper():
        return True
    else:
        return False


mayus = input("Ingrese una palabra Capitalizada: ")
pal = input("ingrese la misma palabra en minusculas: ")

if compararPalabras(mayus,pal) == True:
    print("Son la misma palabra.")
else:
    print("Son palabras distintas.")
