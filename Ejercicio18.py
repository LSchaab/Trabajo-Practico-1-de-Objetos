def listaInversaAux(cadena):
    lista = cadena.split()
    lista2 = []
    for palabra in lista:
        lista2.insert(0, palabra)
    return lista2

def listaInversa(cadena):
    lista = cadena.split()
    largo = len(lista)
    for palabra in range(largo):
        lista.append(lista[largo-palabra-1])
        lista.remove(lista[largo-palabra-1])
    return lista


cadena =  input("Ingrese una cadena para mi paz mental: ")

opcion = int(input("""Elija como quiere hacerlo
1. Invertir una lista con una lista auxiliar
2. Invertir una lista sin una lista auxiliar: """))

if opcion == 1:
    print(listaInversaAux(cadena))
else: 
    print(listaInversa(cadena))



    