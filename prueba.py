import random 

def validarNum(numero, funcion):
    """"Funcion = 1, valida los numeros que ingresa el usuario
    Funcion = 2, valida los numeros que se generan de manera random
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
    """Pide un numero de 4 cifras distintas"""
    numeroPedido = ""
    while validarNum(numeroPedido, 1) == False:
        numeroPedido = str(input("Ingrese un numero de 4 cifras distintas: "))
    return numeroPedido
    
    
    
def generarNum():
    """Genera un numero aleatorio de 4 cifras"""
    numeroGenerado = ""
    while validarNum(numeroGenerado, 2) == False:
            numeroGenerado = str(random.randint(1000 , 9999))
    return numeroGenerado



def juego():
    """Guarda los numeros en dos listas y llama a las
    funciones para verificar si son validos y compararlos"""
    numerosGenerados = []
    numeroGenerado = generarNum()
    aciertos = 0
    for i in range(4):
        numerosGenerados.append(numeroGenerado[i])
    print(numerosGenerados)
    while aciertos != 4:
        numerosDados = []
        numeroPedido = pedirNum()
        for i in range(4):
            numerosDados.append(numeroPedido[i])
        print(numerosDados)
        aciertos = cantAciertos(numerosGenerados,numerosDados)
        coincidencias = cantCoincidencias(numerosDados,numerosGenerados)
        if aciertos == 4:
            return f"Ganaste este bello juego tan sereno que me llevo toda una mañana de mi vida."
        else:
            print(f"Hay {aciertos} aciertos y {coincidencias} coincidencias") 
            continue

    
def cantAciertos(numerosGenerados,numerosDados):
    """Cuenta los aciertos"""
    aciertos = 0
    for i in range(len(numerosGenerados)):
        if numerosGenerados[i] == numerosDados[i]:
            aciertos += 1
    return aciertos
    

def preguntarSiEsNumero(numero):
    """Pregunta si es un numero"""
    if numero.isdigit():
        return True
    else:
        return False
    
def cantCoincidencias(numerosGenerados,numerosDados):
    """Cuenta las coincidencias"""
    coincidencias = 0
    todosNumeros = numerosGenerados + numerosDados
    for i in range(0,3):
        x = todosNumeros.count(todosNumeros[i])
        if x > 1:
            coincidencias += 1
    return coincidencias - cantAciertos(numerosGenerados,numerosDados)
        
    

print(juego())








