def procesamientoTelegramas(texto, longMax, costoLargas, costoCortas ):
    """Recibe:
            texto: <str>
            longMax: <int>
            costoLargas: <float>
            costoCortas: <float>
       guarda las palabras del texto en una lista, recorre la lista
       y si la palabra supera la longitud maxima definida por el usuario
       (longMax) se reemplaza el sobrante de la palabra por un @,
       los puntos se reemplazan por un stop y el punto final por un STOPSTOP.
       Se devuelve el costo total del telegrama y este mismo con
       los cambios especificados anteriormente."""
       
    listaPalabras = texto.split(" ")
    listaPalabras[-1] = listaPalabras[-1].rstrip(".")
    telegrama = ""
    contCortas = 0
    contLargas = 0

    for i in range(len(listaPalabras)):
        if len(listaPalabras[i]) > longMax:
            telegrama += listaPalabras[i][0:longMax] + "@" + " "
            contLargas += 1
            for letra in listaPalabras[i]:
                if letra == ".":
                    telegrama = f"{telegrama.strip()}{listaPalabras[i].replace(listaPalabras[i], ' STOP ')}" 
        else:
            telegrama += listaPalabras[i] + " "
            contCortas += 1
            for letra in listaPalabras[i]:
                if letra == ".":
                    telegrama = f"{listaPalabras[i].replace(listaPalabras[i][-1], ' STOP ')}" 
    
    telegrama = telegrama.rstrip( ) + " " + "STOPSTOP"
    total = (costoCortas * contCortas) + (costoLargas * contLargas)
    
    return telegrama, total

texto = input("Ingrese su telegrama: ")
longMax = int(input("Longitud maxima de una palabra: "))
costoL = float(input("Ingrese el costo de las palabras largas: "))
costoC = float(input("Ingrese el costo de las palabras cortas: "))
telegrama, total = procesamientoTelegramas(texto,longMax,costoL,costoC)
print(telegrama, "el total es:", total)