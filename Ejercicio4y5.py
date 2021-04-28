def farenheitacelscius(farenheit):
    """Calcula grados Celscius"""
    celscius = (farenheit - 32) * 5/9
    return celscius

def celsciusafarenheit(celscius):
    """Calcula grados farenheit"""
    farenheit = (9/5 * celscius) + 32
    return farenheit 

def tablaFarenaCel():
    "Imprime una tabla con los grados farenheit (0° a 120°) en Celscius "
    f = 0
    while f <= 120:
        print(str(f)," |", str(farenheitacelscius(f)))
        f += 10

opcion = int(input("""Ingrese un numero según lo que desee:
1.Pasar grados farenheit a Celscius
2.Pasar grados Celscius a Farenheit:
3.Mostrar una tabla de conversión de Farenheit a Celscius de 10° en 10°: """))

if opcion == 1:
    far = float(input("Ingrese los grados Farenheit que desea convertir: "))
    print(far,"° F equivalen a",farenheitacelscius(far),"° C")

if opcion == 2:
    cel = float(input("Ingrese los grados Celsius que desea convertir: "))
    print(cel,"° C equivalen a",celsciusafarenheit(cel),"° F")

if opcion == 3:
    tablaFarenaCel()

