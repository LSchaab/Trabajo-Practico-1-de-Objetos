meses= ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dias= [31,28,31,30,31,30,31,31,30,31,30,31]


def mesValido(unMes):
    esNumero=preguntar_si_es_un_numero_o_no(unMes)
    if esNumero==True:
        if int(unMes) < 13 and int(unMes) > 0:
            return True
    else:
        for i in range(len(meses)):
            if meses[i] == unMes:
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
    esBisiesto = bisiestoSiNo(año)
    if esValido == True:
        if esNumero == True:
            mes = int(mes)
            if mes == 2 and esBisiesto == True:
                return (dias[mes-1])+1
            else: 
                return dias[mes-1]
        else:
            for i in range(len(meses)):
                if meses[i] == mes:
                    if mes == "febrero" and esBisiesto == True:
                        return (dias[i]) + 1
                    else:
                        return dias[i]
    else:
        return 1


def fechaValida(dia,mes,año):
    if int(año) > 1:
            if mesValido(mes) == True:
                if dia > diasmes(mes,año) or dia < 1:
                    return False
                else:
                    return True
            else:
                return False


def diasFinMes(dia,mes,año):
    diasFinMes = diasmes(mes,año) - dia
    return diasFinMes


def diasFinAño(dia,mes,año): 
    finAño=diasFinMes(dia,mes,año)
    if fechaValida(dia,mes,año):
        if preguntar_si_es_un_numero_o_no(mes) == True:
            mes = int(mes)
            for i in range(mes,12):
                finAño = finAño + dias[i]
            return finAño
        else: 
            mes = meses.index(mes) + 1
            for i in range(mes,12):
                finAño = finAño + dias[i]
            return finAño

def diasTranscurridos(dia,mes,año):
    diasTrans = dias
    if fechaValida == True:
        for i in range
        




opcion=int(input("""Ingrese lo que desea realizar:
1. Saber si un año es bisiesto o no.
2. Saber la cantidad de dìas de un mes.
3. Validar una fecha.
4. Calcular días faltantes hasta fin de mes.
5. Calcular días faltantes hasta fin de año.
6. Calcular días transcurridos en el año dada una fecha.
"""))


if opcion == 1:
    año = int(input("Ingrese un año: "))
    if bisiestoSiNo(año)==False:
        print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")


if opcion == 2:
    año = int(input("Ingrese el año: "))
    mes = input("Ingrese su mes: ")
    if diasmes(mes,año) != 1:
        print("La cantidad de días del mes ingresado son: ", diasmes(mes,año))
    else:
        print("Datos ingresados no validos.")


if opcion==3:
    año = int(input("Ingrese el año: "))
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el dia: "))
    if fechaValida(dia,mes,año) == True:
        print("La fecha es valida.")
    else:
        print("La fecha es invalida.")

if opcion == 4:
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el día: "))
    print("Faltan", diasFinMes(dia,mes,año), "días para fin de mes.")


if opcion == 5:
    año = int(input("Ingrese el año: "))
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el dia: "))
    if diasFinAño(dia,mes,año) == 0:
        print("Feliz año nuevo :D")
    else: 
        print("La cantidad de días que faltan para fin de año es: ", diasFinAño(dia,mes,año))