meses= ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dias= [31,28,31,30,31,30,31,31,30,31,30,31]


def mesValido(unMes):
    """Recibe: 
            unMes: <str>
       comprueba si el mes es un número, si lo es lo hace integer y lo valida
       si no lo es recorre la lista meses[] y revisa si está ahí."""
       
    esNumero=preguntar_si_es_un_numero_o_no(unMes)
    if esNumero==True:
        if int(unMes) < 13 and int(unMes) > 0:
            return True
    else:
        for i in range(len(meses)):
            if meses[i] == unMes:
                return True


def preguntar_si_es_un_numero_o_no(unMes):
    """Recibe:
            unMes: <str>
       y comprueba si es un numero o no
       devolviendo un valor booleano"""
       
    if unMes.isdigit():
        return True
    else:
        return False


def bisiestoSiNo(anio):
    """Recibe:
            anio: <int>
       comprueba si es bisiesto y
       devuelve un valor booleano."""
       
    if anio % 4 != 0:
        return False
    else:
        if anio % 100 != 0:
            return True
        elif anio % 400 == 0:
            return True
        else:
            return False


def diasMes(mes,anio):
    """Recibe:
            anio: <int>
            mes: <str>
       valida el mes, pregunta si es un numero
       pregunta si el año es bisiesto y dependiendo
       de las respuestas de esas funciones devuelve 
       los días del mes ingresado. 
    """
    
    esNumero = preguntar_si_es_un_numero_o_no(mes)
    esValido = mesValido(mes)
    esBisiesto = bisiestoSiNo(anio)
    
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


def fechaValida(dia,mes,anio):
    """Recibe:
            dia: <int>
            mes: <str>
            anio: <int>
       valida el mes, el año y los días
       y devuelve un valor booleano."""
       
    if int(anio) > 1:
            if mesValido(mes) == True:
                if dia > diasMes(mes,anio) or dia < 1:
                    return False
                else:
                    return True
            else:
                return False


def diasFinMes(dia,mes,anio):
    """Recibe: 
            dia: <int>
            mes: <str>
            anio: <int>
       Devuelve los dias que faltan para fin de mes."""
    diasFinMes = diasMes(mes,anio) - dia
    return diasFinMes


def diasFinAnio(dia,mes,anio): 
    """Recibe: 
            dia: <int>
            mes: <str>
            anio: <int>
       valida la fecha, pregunta si el mes
       es un numero o no y devuelve los 
       dias que faltan hasta fin de año."""

    finAnio = diasFinMes(dia,mes,anio)
    if fechaValida(dia,mes,anio):
        if preguntar_si_es_un_numero_o_no(mes) == True:
            mes = int(mes)
            for i in range(mes,12):
                finAnio = finAnio + dias[i]
            return finAnio
        else: 
            mes = meses.index(mes) + 1
            for i in range(mes,12):
                finAnio = finAnio + dias[i]
            return finAnio

def diasTranscurridos(dia,mes,anio):
    """Recibe: 
            dia: <int>
            mes: <str>
            anio: <int>
       valida la fecha, pregunta si el mes
       es un numero o no y devuelve los dias
       transcurridos hasta la fecha ingresada."""
       
    if fechaValida(dia,mes,anio) == True:
        if bisiestoSiNo(anio) == True:
            dias[1] = 29
        else:
            dias[1] = 28

        diasTrans = dia

        if preguntar_si_es_un_numero_o_no(mes) == True:
            mes = int(mes)
        else: 
            mes = meses.index(mes) + 1
        for i in range(0,mes-1):
            diasTrans = diasTrans + dias[i]
        return diasTrans
        


opcion = int(input("""Ingrese lo que desea realizar:
1. Saber si un año es bisiesto o no.
2. Saber la cantidad de dìas de un mes.
3. Validar una fecha.
4. Calcular días faltantes hasta fin de mes.
5. Calcular días faltantes hasta fin de año.
6. Calcular días transcurridos en el año dada una fecha.
"""))


if opcion == 1:
    anio = int(input("Ingrese un año: "))
    
    if bisiestoSiNo(anio)==False:
        print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")


if opcion == 2:
    anio = int(input("Ingrese el año: "))
    mes = input("Ingrese su mes: ")
    
    if diasMes(mes,anio) != 1:
        print("La cantidad de días del mes ingresado son: ", diasMes(mes,anio))
    else:
        print("Datos ingresados no validos.")


if opcion==3:
    anio = int(input("Ingrese el año: "))
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el día: "))
    
    if fechaValida(dia,mes,anio) == True:
        print("La fecha es valida.")
    else:
        print("La fecha es invalida.")

if opcion == 4:
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el día: "))
    anio = int(input("Ingrese el año: "))
    print("Faltan", diasFinMes(dia,mes,anio), "días para fin de mes.")


if opcion == 5:
    anio = int(input("Ingrese el año: "))
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el día: "))
    
    if diasFinAnio(dia,mes,anio) == 0:
        print("Feliz año nuevo :D")
    else: 
        print("La cantidad de días que faltan para fin de año es: ", diasFinAnio(dia,mes,anio))

if opcion == 6:
    anio = int(input("Ingrese el año: "))
    mes = input("Ingrese el mes: ")
    dia = int(input("Ingrese el día: "))
    
    print("Los días ya transcurridos del año son: ", diasTranscurridos(dia,mes,anio))