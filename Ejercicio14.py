import random 


def validarNum(numero, funcion):
    """"Recibe:
            numero: <str>
            funcion: <int>
       funcion = 1 agrega el numero que ingreso
       el usuario a una lista digito por digito.
       funcion = 2 agrega el numero que se generó
       aleatoriamente a una lista.
       En ambos casos se comprueba que un digito no
       esté en un numero más de una vez devolviendo un valor 
       booleano.
    """
    
    hacer = funcion
    numerosGenerados = []
    numerosDados = []
    if hacer == 1:
        if preguntarSiEsNumero(numero) == True:
            for i in range(4):
                numerosDados.append(numero[i])
            for i in numerosDados:
                numD1 = numerosDados.count(numero[0])
                numD2 = numerosDados.count(numero[1])
                numD3 = numerosDados.count(numero[2])
                numD4 = numerosDados.count(numero[3])
            if numD1 != 1 or numD2 != 1 or numD3 != 1 or numD4 != 1:
                return False
            else:
                return True
        else:
            return False
    
    else: 
        if preguntarSiEsNumero(numero) == True:
            for i in range(4):
                numerosGenerados.append(numero[i])
            for i in numerosGenerados:
                numG1 = numerosGenerados.count(numero[0])
                numG2 = numerosGenerados.count(numero[1])
                numG3 = numerosGenerados.count(numero[2])
                numG4 = numerosGenerados.count(numero[3])
            if numG1 != 1 or numG2 != 1 or numG3 != 1 or numG4 != 1:
                return False
            else:
                return True
        else:
            return False
        
    
def pedirNum():
    """Pide un numero de 4 cifras distintas,
       lo valida y lo devuelve."""

    numeroPedido = ""
    while validarNum(numeroPedido, 1) == False:
        numeroPedido = str(input("Ingrese un numero de 4 cifras distintas: "))
    return numeroPedido
    
    
def generarNum():
    """Genera un numero aleatorio de 4 cifras,
       lo valida y lo devuelve."""
    numeroGenerado = ""
    while validarNum(numeroGenerado, 2) == False:
            numeroGenerado = str(random.randint(1000 , 9999))
    return numeroGenerado


def juego():
    """Guarda los numeros en dos listas y llama a las
    funciones para verificar si son validos y compararlos.
    Puede devolver la cantidad de aciertos o coincdencias
    o un mensaje que indica que el usuario ganó."""
    
    numerosGenerados = []
    numeroGenerado = generarNum()
    aciertos = 0
    
    for i in range(4):
        numerosGenerados.append(numeroGenerado[i])
    
    while aciertos != 4:
        numerosDados = []
        numeroPedido = pedirNum()
        for i in range(4):
            numerosDados.append(numeroPedido[i])
        
        aciertos = cantAciertos(numerosGenerados,numerosDados)
        coincidencias = cantCoincidencias(numerosDados,numerosGenerados)
        
        if aciertos == 4:
            return f"Ganaste este bello juego tan sereno que me llevo toda una mañana de mi vida."
        else:
            print(f"Hay {aciertos} aciertos y {coincidencias} coincidencias") 
            continue

    
def cantAciertos(numerosGenerados,numerosDados):
    """Recibe la lista de numeros generados 
       aleatoriamente y la lista de numeros
       que dio el usuario, las compara y
       por cada numero que se encuentre en
       la misma posisición que en el 
       número generado se suma un acierto."""
       
    aciertos = 0
    
    for i in range(len(numerosGenerados)):
        if numerosGenerados[i] == numerosDados[i]:
            aciertos += 1
    return aciertos
    

def preguntarSiEsNumero(numero):
    """Recibe:
            numero: <str>
       comprueba si es un numero
       devuelve un valor booleano."""
       
    if numero.isdigit():
        return True
    else:
        return False
    
    
def cantCoincidencias(numerosGenerados,numerosDados):
    """Recibe la lista de numeros generados 
       aleatoriamente y la lista de numeros
       que dio el usuario, las suma y
       por cada numero que se encuentre dos veces
       en la lista se suma una coincidencia."""
       
    coincidencias = 0
    todosNumeros = numerosGenerados + numerosDados

    for i in range(0,3):
        x = todosNumeros.count(todosNumeros[i])
        if x > 1:
            coincidencias += 1
    return coincidencias - cantAciertos(numerosGenerados,numerosDados)
        

print(juego())