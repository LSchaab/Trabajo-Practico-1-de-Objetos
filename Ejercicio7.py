meses= ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dias= [31,28,31,30,31,30,31,31,30,31,30,31]

def mesValido(unMes):
    esNumero=preguntar_si_es_un_numero_o_no(unMes)
    if esNumero==True:
        if int(unMes) < 13 and int(unMes) > 0:
            return True
    else:
        for i in range(len(meses)):
            if meses[i]==unMes:
                return True



def preguntar_si_es_un_numero_o_no(unMes):
    if unMes.isdigit():
        return True
    else:
        return False

def bisiestoSiNo(año):
    if año % 4 != 0:
        return False
    else:
        if año % 100 != 0:
            return True
        elif año % 400 == 0:
            return True
        else:
            return False

def diasmes(mes,año):
    esNumero = preguntar_si_es_un_numero_o_no(mes)
    esValido = mesValido(mes)
    esBisiesto= bisiestoSiNo(año)
    if esValido==True:
        if esNumero==True:
            mes=int(mes)
            if mes==2 and esBisiesto==True:
                return (dias[mes-1])+1
            else: 
                return dias[mes-1]
        else:
            for i in range(len(meses)):
                if meses[i]==mes:
                    if mes=="febrero" and esBisiesto==True:
                        return (dias[i])+1
                    else:
                        return dias[i]
    else:
        return 1




opcion=int(input("""Ingrese lo que desea realizar:
1. Saber si un año es bisiesto o no.
2. Saber la cantidad de dìas de un mes.
3. Validar una fecha.
"""))

if opcion== 1:
    año=int(input("Ingrese un año: "))
    if bisiestoSiNo(año)==False:
        print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")
if opcion==2:
    año=int(input("Ingrese el año: "))
    mes=input("Ingrese su mes: ")
    if diasmes(mes,año) != 1:
        print("La cantidad de días del mes ingresado son: ", diasmes(mes,año))
    else:
        print("Datos ingresados no validos.")
