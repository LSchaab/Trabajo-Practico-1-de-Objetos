def farenheitACelscius(farenheit):
    """Recibe:
            farenheit: <float>
       Devuelve los grados convertidos a celscius """
       
    celscius = (farenheit - 32) * 5/9
    return round(celscius,2)

def celsciusAFarenheit(celscius):
    """Recibe:
            celscius: <float>
       Devuelve los grados convertidos a farenheit """
       
    farenheit = (9/5 * celscius) + 32
    return round(farenheit,2) 

def tablaFarenaCel():
    """Imprime una tabla de conversion
       de grados Farenheit a Celscius"""
       
    f = 0
    while f <= 120:
        print(str(f)," |", str(farenheitACelscius(f)))
        f += 10

opcion = int(input("""Ingrese un numero según lo que desee:
1.Pasar grados farenheit a Celscius
2.Pasar grados Celscius a Farenheit:
3.Mostrar una tabla de conversión de Farenheit a Celscius de 10° en 10°: """))

if opcion == 1:
    far = float(input("Ingrese los grados Farenheit que desea convertir: "))
    print(far,"° F equivalen a",farenheitACelscius(far),"° C")

if opcion == 2:
    cel = float(input("Ingrese los grados Celsius que desea convertir: "))
    print(cel,"° C equivalen a",celsciusAFarenheit(cel),"° F")

if opcion == 3:
    tablaFarenaCel()

