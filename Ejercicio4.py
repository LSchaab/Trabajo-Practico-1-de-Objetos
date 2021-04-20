def farenheitacelscius(farenheit):
    celscius= (farenheit-32)*5/9
    return celscius

def celsciusafarenheit(celscius):
    farenheit= (9/5*celscius) + 32
    return farenheit 

def tablaFarenaCel():
    f = 0
    while f <= 120:
        print(str(f)," |", str(farenheitacelscius(f)))
        f += 10

Hacer=int(input("""Ingrese un numero según lo que desee:
1.Pasar grados farenheit a Celscius
2.Pasar grados Celscius a Farenheit:
3.Mostrar una tabla de conversión de Farenheit a Celscius de 10° en 10°: """))

if Hacer==1:
    far=float(input("Ingrese los grados Farenheit que desea convertir: "))
    print(far,"° F equivalen a",farenheitacelscius(far),"° C")

if Hacer==2:
    cel=float(input("Ingrese los grados Celsius que desea convertir: "))
    print(cel,"° C equivalen a",celsciusafarenheit(cel),"° F")

if Hacer==3:
    tablaFarenaCel()

